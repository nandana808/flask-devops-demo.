
from app import app


def test_home_page():
    app.config["TESTING"] = True

    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
        assert b"My First DevOps Project" in response.data


def test_health_endpoint():
    app.config["TESTING"] = True

    with app.test_client() as client:
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json == {"status": "healthy"}
