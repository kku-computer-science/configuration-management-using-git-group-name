from abc import ABC, abstractmethod

class SortFact(ABC):
    @abstractmethod
    def sort(self, data):
        pass
