import pytest
from src.config_loader import ConfigLoader
from src.query_generator import QueryGenerator

def test_generate_update_query():
    config = ConfigLoader.load_config('config/config.yaml')
    query_generator = QueryGenerator(config)
    table_config = config['tables'][0]
    query = query_generator.generate_update_query(table_config, config['masking_rules'])
    assert "UPDATE" in query
    assert table_config['name'] in query