import os

from app import create_app

def test_health_endpoint():
    app = create_app()

    with app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
