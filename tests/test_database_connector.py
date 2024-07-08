import pytest
from unittest.mock import patch, MagicMock
from src.database.mysql_connector import MySQLConnector
from src.database.oracle_connector import OracleConnector
from src.database.snowflake_connector import SnowflakeConnector
from src.database.s3_connector import S3Connector

@patch('src.database.mysql_connector.create_engine')
def test_mysql_connector_get_metadata(mock_create_engine):
    mock_engine = MagicMock()
    mock_create_engine.return_value = mock_engine
    mock_inspector = MagicMock()
    mock_engine.connect.return_value.__enter__.return_value = mock_inspector
    mock_inspector.get_table_names.return_value = ['table1', 'table2']
    mock_inspector.get_columns.return_value = [{'name': 'column1'}, {'name': 'column2'}]

    connector = MySQLConnector('user', 'password', 'localhost', 3306, 'database')
    metadata = connector.get_metadata()
    
    assert metadata == {'table1': [{'name': 'column1'}, {'name': 'column2'}], 'table2': [{'name': 'column1'}, {'name': 'column2'}]}

@patch('src.database.oracle_connector.create_engine')
def test_oracle_connector_get_metadata(mock_create_engine):
    mock_engine = MagicMock()
    mock_create_engine.return_value = mock_engine
    mock_inspector = MagicMock()
    mock_engine.connect.return_value.__enter__.return_value = mock_inspector
    mock_inspector.get_table_names.return_value = ['table1', 'table2']
    mock_inspector.get_columns.return_value = [{'name': 'column1'}, {'name': 'column2'}]

    connector = OracleConnector('user', 'password', 'localhost', 1521, 'database')
    metadata = connector.get_metadata()
    
    assert metadata == {'table1': [{'name': 'column1'}, {'name': 'column2'}], 'table2': [{'name': 'column1'}, {'name': 'column2'}]}

@patch('snowflake.connector.connect')
def test_snowflake_connector_get_metadata(mock_connect):
    mock_connection = MagicMock()
    mock_connect.return_value = mock_connection
    mock_cursor = MagicMock()
    mock_connection.cursor.return_value.__enter__.return_value = mock_cursor
    mock_cursor.fetchall.side_effect = [
        [('table1',), ('table2',)],  # First call to SHOW TABLES
        [('column1', 'STRING'), ('column2', 'NUMBER')],  # First call to DESCRIBE TABLE table1
        [('column1', 'STRING'), ('column2', 'NUMBER')]   # Second call to DESCRIBE TABLE table2
    ]

    connector = SnowflakeConnector('user', 'password', 'account', 'warehouse', 'database', 'schema')
    metadata = connector.get_metadata()
    
    assert metadata == {
        'table1': [{'name': 'column1', 'type': 'STRING'}, {'name': 'column2', 'type': 'NUMBER'}],
        'table2': [{'name': 'column1', 'type': 'STRING'}, {'name': 'column2', 'type': 'NUMBER'}]
    }

@patch('boto3.client')
def test_s3_connector_get_metadata(mock_boto_client):
    mock_client = MagicMock()
    mock_boto_client.return_value = mock_client
    mock_client.list_objects_v2.return_value = {
        'Contents': [{'Key': 'object1'}, {'Key': 'object2'}]
    }

    connector = S3Connector('access_key', 'secret_key', 'bucket', 'region')
    metadata = connector.get_metadata()
    
    assert metadata == ['object1', 'object2']
