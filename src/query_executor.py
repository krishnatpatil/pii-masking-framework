class QueryExecutor:
    def __init__(self, db_connector):
        self.db_connector = db_connector

    def execute_query(self, query, db_type='oracle'):
        if db_type == 'oracle':
            engine = self.db_connector.get_oracle_engine()
        elif db_type == 'snowflake':
            engine = self.db_connector.get_snowflake_engine()

        with engine.connect() as connection:
            connection.execute(query)