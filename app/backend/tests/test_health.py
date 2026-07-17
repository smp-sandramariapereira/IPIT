"""Testes do endpoint operacional do backend."""

from fastapi.testclient import TestClient

from app.backend.main import app


client = TestClient(app)


def test_health_returns_service_metadata() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "IPIT Learning Engine",
        "version": "0.1.0",
        "environment": "development",
    }
