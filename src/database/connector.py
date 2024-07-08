from abc import ABC, abstractmethod

class DatabaseConnector(ABC):
    @abstractmethod
    def get_engine(self):
        pass

    @abstractmethod
    def get_metadata(self):
        pass
