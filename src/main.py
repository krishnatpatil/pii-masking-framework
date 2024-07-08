import yaml
import logging.config
from src.database.mysql_connector import MySQLConnector
from src.database.oracle_connector import OracleConnector
from src.database.snowflake_connector import SnowflakeConnector
from src.database.s3_connector import S3Connector
from src.detection.pii_detector import PIIDetector
from src.masking.masking_rule import MaskingRule
from src.framework.pii_masking_framework import PIIMaskingFramework

def load_config(config_path='config/config.yaml'):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def setup_logging(logging_config):
    logging.config.dictConfig(logging_config)

def get_db_connector(config):
    db_type = config['database']['type']
    if db_type == 'mysql':
        return MySQLConnector(
            config['database']['username'],
            config['database']['password'],
            config['database']['host'],
            config['database']['port'],
            config['database']['database_name']
        )
    elif db_type == 'oracle':
        return OracleConnector(
            config['database']['username'],
            config['database']['password'],
            config['database']['host'],
            config['database']['port'],
            config['database']['database_name']
        )
    elif db_type == 'snowflake':
        return SnowflakeConnector(
            config['database']['username'],
            config['database']['password'],
            config['database']['account'],
            config['database']['warehouse'],
            config['database']['database_name'],
            config['database']['schema']
        )
    elif db_type == 's3':
        return S3Connector(
            config['database']['access_key'],
            config['database']['secret_key'],
            config['database']['bucket'],
            config['database']['region']
        )
    else:
        raise ValueError(f"Unsupported database type: {db_type}")

if __name__ == "__main__":
    config = load_config()
    setup_logging(config['logging'])
    
    logger = logging.getLogger(__name__)
    logger.info("Starting PII Masking Framework")
    
    try:
        db_connector = get_db_connector(config)
        pii_detector = PIIDetector()
        masking_rule = MaskingRule()
        
        framework = PIIMaskingFramework(db_connector, pii_detector, masking_rule)
        framework.mask_pii_data()
    except Exception as e:
        logger.exception("An error occurred while running the PII Masking Framework")
