from sqlalchemy import create_engine

class DBConnector:
    def __init__(self, config):
        self.config = config

    def get_oracle_engine(self):
        oracle_url = f"oracle+cx_oracle://{self.config['oracle']['user']}:{self.config['oracle']['password']}@{self.config['oracle']['host']}:{self.config['oracle']['port']}/{self.config['oracle']['service_name']}"
        return create_engine(oracle_url)

    def get_snowflake_engine(self):
        snowflake_url = f"snowflake://{self.config['snowflake']['user']}:{self.config['snowflake']['password']}@{self.config['snowflake']['account']}/{self.config['snowflake']['database']}/{self.config['snowflake']['schema']}?warehouse={self.config['snowflake']['warehouse']}"
        return create_engine(snowflake_url)