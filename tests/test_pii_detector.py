import pytest
from src.detection.pii_detector import PIIDetector

def test_detect_pii_columns():
    metadata = {
        'table1': [{'name': 'name', 'type': 'STRING'}, {'name': 'age', 'type': 'NUMBER'}, {'name': 'email', 'type': 'STRING'}],
        'table2': [{'name': 'phone', 'type': 'STRING'}, {'name': 'address', 'type': 'STRING'}, {'name': 'dob', 'type': 'DATE'}]
    }
    
    pii_detector = PIIDetector()
    pii_columns = pii_detector.detect_pii_columns(metadata)
    
    expected_pii_columns = {
        'table1': ['name', 'email'],
        'table2': ['phone', 'address']
    }
    
    assert pii_columns == expected_pii_columns
