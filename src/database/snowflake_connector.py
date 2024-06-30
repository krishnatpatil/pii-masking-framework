import snowflake.connector
from .connector import DatabaseConnector

class SnowflakeConnector(DatabaseConnector):
    def __init__(self, username, password, account, warehouse, database, schema):
        self.connection_params = {
            'user': username,
            'password': password,
            'account': account,
            'warehouse': warehouse,
            'database': database,
            'schema': schema
        }
        self.connection = None

    def get_engine(self):
        self.connection = snowflake.connector.connect(**self.connection_params)
        return self.connection

    def get_metadata(self):
        cursor = self.connection.cursor()
        cursor.execute("SHOW TABLES")
        tables = [row[1] for row in cursor.fetchall()]
        metadata = {}
        for table in tables:
            cursor.execute(f"DESCRIBE TABLE {table}")
            columns = cursor.fetchall()
            metadata[table] = [{'name': col[0], 'type': col[1]} for col in columns]
        return metadata