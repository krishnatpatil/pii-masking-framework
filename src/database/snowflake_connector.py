from .db_connector import DBConnector
from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine

class SnowflakeConnector(DBConnector):

    def __init__(self, config):
        self.config = config
        self.engine = None

    def connect(self):
        url = URL(
            account=self.config['account'],
            user=self.config['user'],
            password=self.config['password'],
            database=self.config['database'],
            schema=self.config['schema'],
            warehouse=self.config['warehouse'],
            role=self.config['role']
        )
        self.engine = create_engine(url)

    def execute_query(self, query: str):
        with self.engine.connect() as conn:
            conn.execute(query)