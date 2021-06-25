from flask import Flask
import requests
from routes.main_routes import configure_main_routes
from routes.person_routes import configure_person_routes


def test_base_route():
    url = "http://localhost:5000/"
    response = requests.get(url)
    assert response.status_code == 200


def test_base_route2():
    app = Flask(__name__)
    configure_main_routes(app)
    client = app.test_client()
    url = "/"

    response = client.get(url)
    assert response.status_code == 200
    if response.status_code == 200:
        assert "<h1>main</h1>" in str(response.get_data())


def test_base_route3():
    app = Flask(__name__)
    configure_main_routes(app)
    configure_person_routes(app)
    client = app.test_client()
    url = "/person"

    response = client.get(url)
    assert response.status_code == 200
    if response.status_code == 200:
        assert "<h1>person</h1>" in str(response.get_data())
