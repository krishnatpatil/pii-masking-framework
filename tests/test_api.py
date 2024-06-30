import pytest
from src.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_mask_pii_data_mysql(client):
    data = {
        'database_type': 'mysql'
    }
    response = client.post('/mask_pii_data', json=data)
    assert response.status_code == 200
    assert b'PII data masked successfully' in response.data

def test_mask_pii_data_oracle(client):
    data = {
        'database_type': 'oracle'
    }
    response = client.post('/mask_pii_data', json=data)
    assert response.status_code == 200
    assert b'PII data masked successfully' in response.data

def test_mask_pii_data_snowflake(client):
    data = {
        'database_type': 'snowflake'
    }
    response = client.post('/mask_pii_data', json=data)
    assert response.status_code == 200
    assert b'PII data masked successfully' in response.data

def test_mask_pii_data_s3(client):
    data = {
        'database_type': 's3'
    }
    response = client.post('/mask_pii_data', json=data)
    assert response.status_code == 200
    assert b'PII data masked successfully' in response.data

def test_mask_pii_data_invalid(client):
    data = {
        'database_type': 'invalid'
    }
    response = client.post('/mask_pii_data', json=data)
    assert response.status_code == 400
    assert b'Unsupported database type' in response.data