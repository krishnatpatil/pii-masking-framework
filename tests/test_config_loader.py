import pytest
from src.config_loader import ConfigLoader

def test_load_config():
    config = ConfigLoader.load_config('config/config.yaml')
    assert 'masking_rules' in config
    assert 'tables' in config