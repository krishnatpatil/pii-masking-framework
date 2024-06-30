import pytest
from src.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_fetch_data_mysql(client):
    data = {
        'database_type': 'mysql',
        'table_name': 'users'  # Replace with an actual table name from your database
    }
    response = client.post('/fetch', json=data)
    assert response.status_code == 200
    assert b'Fetched Data' in response.data
    # Add more specific assertions based on expected data format or content

def test_fetch_data_oracle(client):
    data = {
        'database_type': 'oracle',
        'table_name': 'employees'  # Replace with an actual table name from your database
    }
    response = client.post('/fetch', json=data)
    assert response.status_code == 200
    assert b'Fetched Data' in response.data
    # Add more specific assertions based on expected data format or content