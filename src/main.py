from .database.oracle_connector import OracleConnector
from .database.snowflake_connector import SnowflakeConnector
from .masking.masker import Masker
from .config import DB_CONFIG

def main():
    oracle_connector = OracleConnector(DB_CONFIG['oracle'])
    oracle_connector.connect()

    snowflake_connector = SnowflakeConnector(DB_CONFIG['snowflake'])
    snowflake_connector.connect()

    masker = Masker(oracle_connector)
    masker.mask_pii('customers', ['name', 'address', 'phone_number', 'email_address', 'ssn', 'financial_details', 'dob'], 'date_created')

    masker = Masker(snowflake_connector)
    masker.mask_pii('customers', ['name', 'address', 'phone_number', 'email_address', 'ssn', 'financial_details', 'dob'], 'date_created')

if __name__ == "__main__":
    main()

###################################################################################################################################

from config_loader import ConfigLoader
from db_connector import DBConnector
from query_generator import QueryGenerator
from query_executor import QueryExecutor
from logger import Logger

def main():
    logger = Logger.get_logger('PII_Masking')
    
    config = ConfigLoader.load_config('config/config.yaml')
    db_config = ConfigLoader.load_config('config/db_connections.yaml')
    
    db_connector = DBConnector(db_config)
    query_generator = QueryGenerator(config)
    query_executor = QueryExecutor(db_connector)
    
    for table in config['tables']:
        update_query = query_generator.generate_update_query(table, config['masking_rules'])
        logger.info(f"Generated query for table {table['name']}: {update_query}")
        query_executor.execute_query(update_query, 'oracle')
        query_executor.execute_query(update_query, 'snowflake')

if __name__ == "__main__":
    main()