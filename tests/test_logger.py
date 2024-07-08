import pytest
from src.logger import Logger

def test_get_logger():
    logger = Logger.get_logger('test_logger')
    assert logger is not None