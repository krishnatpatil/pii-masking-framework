import pytest
from unittest.mock import MagicMock

@pytest.fixture
def mock_mysql_connector():
    connector = MagicMock()
    connector.get_metadata.return_value = {
        'table1': [{'name': 'name', 'type': 'STRING'}, {'name': 'email', 'type': 'STRING'}]
    }
    return connector

@pytest.fixture
def mock_oracle_connector():
    connector = MagicMock()
    connector.get_metadata.return_value = {
        'table1': [{'name': 'name', 'type': 'STRING'}, {'name': 'email', 'type': 'STRING'}]
    }
    return connector

@pytest.fixture
def mock_snowflake_connector():
    connector = MagicMock()
    connector.get_metadata.return_value = {
        'table1': [{'name': 'name', 'type': 'STRING'}, {'name': 'email', 'type': 'STRING'}]
    }
    return connector

@pytest.fixture
def mock_s3_connector():
    connector = MagicMock()
    connector.get_metadata.return_value = ['object1', 'object2']
    return connector

@pytest.fixture
def mock_pii_detector():
    detector = MagicMock()
    detector.detect_pii_columns.return_value = {
        'table1': ['name', 'email']
    }
    return detector

@pytest.fixture
def mock_masking_rule():
    rule = MagicMock()
    rule.mask_value.side_effect = lambda value, data_type: 'masked_value'
    return rule
