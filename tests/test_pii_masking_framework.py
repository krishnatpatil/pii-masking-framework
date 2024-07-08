import pytest
from unittest.mock import MagicMock, patch
from src.framework.pii_masking_framework import PIIMaskingFramework

@patch('src.framework.pii_masking_framework.snowflake.connector.SnowflakeConnection')
@patch('src.framework.pii_masking_framework.boto3.client')
def test_mask_pii_data_sql(mock_snowflake, mock_boto_client, mock_mysql_connector, mock_pii_detector, mock_masking_rule):
    framework = PIIMaskingFramework(mock_mysql_connector, mock_pii_detector, mock_masking_rule)
    framework.mask_pii_data()
    
    mock_mysql_connector.get_engine.assert_called_once()
    mock_mysql_connector.get_metadata.assert_called_once()
    mock_pii_detector.detect_pii_columns.assert_called_once()
    assert mock_masking_rule.mask_value.call_count == 2

@patch('src.framework.pii_masking_framework.snowflake.connector.SnowflakeConnection')
def test_mask_pii_data_snowflake(mock_snowflake, mock_snowflake_connector, mock_pii_detector, mock_masking_rule):
    framework = PIIMaskingFramework(mock_snowflake_connector, mock_pii_detector, mock_masking_rule)
    framework.mask_pii_data()
    
    mock_snowflake_connector.get_engine.assert
