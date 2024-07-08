import pytest
from src.masking.masking_rule import MaskingRule

@pytest.fixture
def masking_rule():
    return MaskingRule()

def test_mask_value_string(masking_rule):
    original_value = 'John Doe'
    masked_value = masking_rule.mask_value(original_value, 'STRING')
    assert masked_value == 'masked_string'

def test_mask_value_number(masking_rule):
    original_value = 123456789
    masked_value = masking_rule.mask_value(original_value, 'NUMBER')
    assert masked_value == 999999999

def test_mask_value_date(masking_rule):
    original_value = '1990-01-01'
    masked_value = masking_rule.mask_value(original_value, 'DATE')
    assert masked_value == '1900-01-01'
