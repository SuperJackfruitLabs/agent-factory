import pytest
from fastapi.testclient import TestClient
from agent_backend.main import app
from agent_backend.db.database import get_db, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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


def test_create_agent():
    response = client.post(
        "/api/v1/auth/register",
        json={"username": "testuser", "password": "testpassword"},
    )
    token = response.json()["access_token"]

    agent_data = {
        "name": "Test Agent",
        "description": "A test agent",
        "agent_type": "test",
        "tools": ["tool1", "tool2"],
        "model_name": "gpt-3.5-turbo",
        "temperature": 0.7,
    }
    response = client.post(
        "/api/v1/agents", json=agent_data, headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    created_agent = response.json()
    assert created_agent["name"] == agent_data["name"]
    assert created_agent["description"] == agent_data["description"]
    assert created_agent["agent_type"] == agent_data["agent_type"]
    assert created_agent["tools"] == agent_data["tools"]
    assert created_agent["model_name"] == agent_data["model_name"]
    assert created_agent["temperature"] == agent_data["temperature"]


def test_get_agent():
    # First, create a user and an agent
    response = client.post(
        "/api/v1/auth/register",
        json={"username": "testuser", "password": "testpassword"},
    )
    token = response.json()["access_token"]
    agent_data = {
        "name": "Test Agent",
        "description": "A test agent",
        "agent_type": "test",
        "tools": ["tool1", "tool2"],
        "model_name": "gpt-3.5-turbo",
        "temperature": 0.7,
    }
    response = client.post(
        "/api/v1/agents", json=agent_data, headers={"Authorization": f"Bearer {token}"}
    )
    created_agent = response.json()

    # Now, test getting the agent
    response = client.get(
        f"/api/v1/agents/{created_agent['id']}",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    retrieved_agent = response.json()
    assert retrieved_agent == created_agent


def test_update_agent():
    # First, create a user and an agent
    response = client.post(
        "/api/v1/auth/register",
        json={"username": "testuser", "password": "testpassword"},
    )
    token = response.json()["access_token"]
    agent_data = {
        "name": "Test Agent",
        "description": "A test agent",
        "agent_type": "test",
        "tools": ["tool1", "tool2"],
        "model_name": "gpt-3.5-turbo",
        "temperature": 0.7,
    }
    response = client.post(
        "/api/v1/agents", json=agent_data, headers={"Authorization": f"Bearer {token}"}
    )
    created_agent = response.json()

    # Now, test updating the agent
    update_data = {
        "name": "Updated Agent",
        "description": "An updated test agent",
        "tools": ["tool1", "tool2", "tool3"],
        "model_name": "gpt-4",
        "temperature": 0.8,
    }
    response = client.put(
        f"/api/v1/agents/{created_agent['id']}",
        json=update_data,
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    updated_agent = response.json()
    assert updated_agent["name"] == update_data["name"]
    assert updated_agent["description"] == update_data["description"]
    assert updated_agent["tools"] == update_data["tools"]
    assert updated_agent["model_name"] == update_data["model_name"]
    assert updated_agent["temperature"] == update_data["temperature"]


def test_delete_agent():
    # First, create a user and an agent
    response = client.post(
        "/api/v1/auth/register",
        json={"username": "testuser", "password": "testpassword"},
    )
    token = response.json()["access_token"]
    agent_data = {
        "name": "Test Agent",
        "description": "A test agent",
        "agent_type": "test",
        "tools": ["tool1", "tool2"],
        "model_name": "gpt-3.5-turbo",
        "temperature": 0.7,
    }
    response = client.post(
        "/api/v1/agents", json=agent_data, headers={"Authorization": f"Bearer {token}"}
    )
    created_agent = response.json()

    # Now, test deleting the agent
    response = client.delete(
        f"/api/v1/agents/{created_agent['id']}",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Agent deleted successfully"

    # Verify that the agent is deleted
    response = client.get(
        f"/api/v1/agents/{created_agent['id']}",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 404
