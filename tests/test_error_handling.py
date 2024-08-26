import pytest
from fastapi.testclient import TestClient
from fastapi import HTTPException
from agent_backend.main import app
from agent_backend.utils.error_handlers import AppException

client = TestClient(app)


def test_app_exception():
    @app.get("/test-app-exception")
    async def test_app_exception():
        raise AppException(status_code=400, detail="Test error")

    response = client.get("/test-app-exception")
    assert response.status_code == 400
    assert response.json() == {"detail": "Test error"}


def test_http_exception():
    @app.get("/test-http-exception")
    async def test_http_exception():
        raise HTTPException(status_code=404, detail="Not found")

    response = client.get("/test-http-exception")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not found"}
