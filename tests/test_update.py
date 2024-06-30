import pytest
from src.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_update_data_mysql(client):
    data = {
        'database_type': 'mysql',
        'table_name': 'users',
        'columns': ['email'],
        'new_values': ['test@example.com']
    }
    response = client.post('/update', json=data)
    assert response.status_code == 200
    assert b'Data updated successfully' in response.data
    # Add more specific assertions based on expected response content

def test_update_data_oracle(client):
    data = {
        'database_type': 'oracle',
        'table_name': 'employees',
        'columns': ['phone_number'],
        'new_values': ['123-456-7890']
    }
    response = client.post('/update', json=data)
    assert response.status_code == 200
    assert b'Data updated successfully' in response.data
    # Add more specific assertions based on expected response content