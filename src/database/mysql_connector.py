from sqlalchemy import create_engine, inspect
from .connector import DatabaseConnector

class MySQLConnector(DatabaseConnector):
    def __init__(self, username, password, host, port, database):
        self.connection_string = f"mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}"
        self.engine = create_engine(self.connection_string)

    def get_engine(self):
        return self.engine

    def get_metadata(self):
        inspector = inspect(self.engine)
        tables = inspector.get_table_names()
        metadata = {}
        for table in tables:
            columns = inspector.get_columns(table)
            metadata[table] = columns
        return metadata
