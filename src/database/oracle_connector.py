from .db_connector import DBConnector
import cx_Oracle

class OracleConnector(DBConnector):

    def __init__(self, config):
        self.config = config
        self.connection = None

    def connect(self):
        self.connection = cx_Oracle.connect(
            self.config['username'],
            self.config['password'],
            self.config['host'],
            self.config['port'],
            self.config['service_name']
        )

    def execute_query(self, query: str):
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        cursor.close()