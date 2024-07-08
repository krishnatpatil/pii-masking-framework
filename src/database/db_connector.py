from abc import ABC, abstractmethod
from sqlalchemy import create_engine

class DBConnector(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute_query(self, query: str):
        pass