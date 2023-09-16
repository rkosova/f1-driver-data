import pytest
from f1_driver_data.__init__ import create_app

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app

    # clean up / reset resources here

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture() 
def runner(app):
    return app.test_cli_runner()

def test_all_drivers(client):
    response = client.get("/driver/all")
    assert response.status_code == 200
    assert b"Carlo Abate" in response.data
    assert b"Jean-Pierre Beltoise" in response.data
    assert b"Ricardo Zunino" in response.data
    assert len(response.json) == 868

def test_drivers_by_category_top(client):
    # Define query parameters
    query_parameters = {
        'category': 'wins',
        'ranking': 'top',
        'n': 5
    }
    response = client.get("/driver/all", query_string=query_parameters)

    assert response.status_code == 200
    assert len(response.json) == 5
    assert response.json[0]['name'] == 'Lewis Hamilton'

def test_drivers_by_category_bottom(client):
    # Define query parameters
    query_parameters = {
        'category': 'starts',
        'ranking': 'bottom',
        'n': 10
    }
    response = client.get("/driver/all", query_string=query_parameters)

    assert response.status_code == 200
    assert len(response.json) == 10
    assert response.json[0]['starts'] == '0.0'

    
def test_drivers_by_wrong_category(client):
    # Define query parameters
    query_parameters = {
        'category': 'name',
        'ranking': 'bottom',
        'n': 10
    }
    response = client.get("/driver/all", query_string=query_parameters)

    assert response.status_code == 400

def test_drivers_by_non_existent_category(client):
    # Define query parameters
    query_parameters = {
        'category': 'forehead',
        'ranking': 'bottom',
        'n': 10
    }
    response = client.get("/driver/all", query_string=query_parameters)

    assert response.status_code == 400

def test_drivers_by_category_invalid(client):
    # Define query parameters
    query_parameters = {
        'category': 'forehead',
        'ranking': 'bottom',
    }
    response = client.get("/driver/all", query_string=query_parameters)

    assert response.status_code == 400

def test_driver_by_name(client):
    response = client.get("/driver/lewis hamilton")

    assert response.status_code == 200
    assert response.json["nationality"] == "United Kingdom"

def test_non_existent_driver_by_name(client):
    response = client.get("/driver/louis hamilton")

    assert response.status_code == 404