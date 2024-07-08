import pytest
from src.masking.masker import Masker
from src.database.db_connector import DBConnector

class MockDBConnector(DBConnector):

    def connect(self):
        pass

    def execute_query(self, query: str):
        pass

def test_generate_update_queries():
    db_connector = MockDBConnector()
    masker = Masker(db_connector)
    queries = masker.generate_update_queries('customers', ['name', 'city', 'phone_number', 'ssn', 'financial_details', 'dob'], 'date_created')
    assert len(queries) == 6