from abc import ABC, abstractmethod


class MainAdapter(ABC):

    @abstractmethod
    def create_client(self):
        pass
    