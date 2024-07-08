import pytest
from src.config_loader import ConfigLoader
from src.db_connector import DBConnector
from src.query_executor import QueryExecutor

def test_execute_query():
    config = ConfigLoader.load_config('config/db_connections.yaml')
    db_connector = DBConnector(config)
    query_executor = QueryExecutor(db_connector)
    test_query = "SELECT 1"
    query_executor.execute_query(test_query, 'oracle')
    query_executor.execute_query(test_query, 'snowflake')
    assert True