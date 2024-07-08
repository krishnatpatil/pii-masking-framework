import pytest
from src.config_loader import ConfigLoader
from src.db_connector import DBConnector

def test_connect_oracle():
    config = ConfigLoader.load_config('config/db_connections.yaml')
    db_connector = DBConnector(config)
    engine = db_connector.get_oracle_engine()
    assert engine is not None

def test_connect_snowflake():
    config = ConfigLoader.load_config('config/db_connections.yaml')
    db_connector = DBConnector(config)
    engine = db_connector.get_snowflake_engine()
    assert engine is not None