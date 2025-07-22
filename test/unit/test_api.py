import pytest
from fastapi.testclient import TestClient


class TestAPI:

    @pytest.fixture
    def client(self):
        from api.app import build_app
        return TestClient(build_app())

    def test_api(self, client):
        """Test the API endpoint."""
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {'status': 'healthy'}

    def test_api_not_found(self, client):
        """Test a non-existent API endpoint."""
        response = client.get("/health1")
        assert response.status_code == 404
        assert response.json() == {"detail": "Not Found"}