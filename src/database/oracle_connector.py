from sqlalchemy import create_engine, inspect
from .connector import DatabaseConnector

class OracleConnector(DatabaseConnector):
    def __init__(self, username, password, host, port, database):
        self.connection_string = f"oracle+cx_oracle://{username}:{password}@{host}:{port}/?service_name={database}"
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