from src.main import load_config
from src.database.connector import DatabaseConnector
from src.detection.pii_detector import PIIDetector
from src.masking.masking_rule import MaskingRule
from src.framework.pii_masking_framework import PIIMaskingFramework

def run():
    config = load_config()
    db_config = config['database']

    db_connector = DatabaseConnector(
        db_type=db_config['type'],
        username=db_config['username'],
        password=db_config['password'],
        host=db_config['host'],
        port=db_config['port'],
        database=db_config['database_name']
    )
    pii_detector = PIIDetector()
    masking_rule = MaskingRule()
    
    framework = PIIMaskingFramework(db_connector, pii_detector, masking_rule)
    framework.mask_pii_data()

if __name__ == "__main__":
    run()
