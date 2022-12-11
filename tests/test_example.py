from chalice.test import Client

from example.app import app


def test_index():
    with Client(app) as client:
        response = client.http.get("/")
        assert response.json_body == {"chalice": "example"}
