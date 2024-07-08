from .mask_rules import MaskRules

class Masker:

    def __init__(self, db_connector):
        self.db_connector = db_connector

    def generate_update_queries(self, table_name, columns, date_column):
        queries = []
        for column in columns:
            rule = MASKING_RULES.get(column, None)
            if rule:
                queries.append(f"UPDATE {table_name} SET {column} = '{rule(None)}' WHERE {date_column} < SYSDATE - INTERVAL '20' YEAR")
        return queries

    def mask_pii(self, table_name, columns, date_column):
        queries = self.generate_update_queries(table_name, columns, date_column)
        for query in queries:
            self.db_connector.execute_query(query)