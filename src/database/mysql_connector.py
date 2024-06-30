from sqlalchemy import create_engine, inspect
from .connector import DatabaseConnector
import logging

logger = logging.getLogger(__name__)

class MySQLConnector(DatabaseConnector):
    def __init__(self, username, password, host, port, database):
        self.connection_string = f"mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}"
        self.engine = create_engine(self.connection_string)
        logger.info(f"Connected to MySQL database: {database} at {host}:{port}")

    def get_engine(self):
        return self.engine

    def get_metadata(self):
        inspector = inspect(self.engine)
        tables = inspector.get_table_names()
        metadata = {}
        for table in tables:
            columns = inspector.get_columns(table)
            metadata[table] = columns
        logger.info(f"Metadata retrieved for MySQL database: {metadata}")
        return metadata