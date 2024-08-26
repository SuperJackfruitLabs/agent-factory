import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from agent_backend.db.database import Base, get_db
from agent_backend.main import app
from agent_backend.utils.auth import create_access_token, get_password_hash
from agent_backend.models.user import User

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


@pytest.fixture(autouse=True)
def clean_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


def test_create_user():
    response = client.post(
        "/api/v1/auth/register",
        json={"username": "testuser", "password": "testpassword"},
    )
    assert (
        response.status_code == 200
    ), f"Expected 200, got {response.status_code}. Response: {response.json()}"
    assert "access_token" in response.json()

    # Test creating a user with an existing username
    response = client.post(
        "/api/v1/auth/register",
        json={"username": "testuser", "password": "testpassword"},
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Username already registered"


def test_login_user():
    # First, create a user
    client.post(
        "/api/v1/auth/register",
        json={"username": "testuser", "password": "testpassword"},
    )

    # Now, try to log in
    response = client.post(
        "/api/v1/auth/token", data={"username": "testuser", "password": "testpassword"}
    )
    assert (
        response.status_code == 200
    ), f"Expected 200, got {response.status_code}. Response: {response.json()}"
    assert "access_token" in response.json()


def test_login_user_wrong_password():
    response = client.post(
        "/api/v1/auth/token", data={"username": "testuser", "password": "wrongpassword"}
    )
    assert response.status_code == 401


def test_protected_route():
    # First, create a user and get a token
    client.post(
        "/api/v1/auth/register",
        json={"username": "protecteduser", "password": "testpassword"},
    )
    response = client.post(
        "/api/v1/auth/token",
        data={"username": "protecteduser", "password": "testpassword"},
    )
    token = response.json()["access_token"]

    # Test a protected route
    response = client.get(
        "/api/v1/agents", headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200


def test_protected_route_no_token():
    response = client.get("/api/v1/agents")
    assert response.status_code == 401
