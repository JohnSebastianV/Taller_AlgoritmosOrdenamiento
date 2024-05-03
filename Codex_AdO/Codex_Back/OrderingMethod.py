from abc import ABC, abstractmethod


class OrderingMethod(ABC):
    @staticmethod
    @abstractmethod
    def sort(arr: list) -> list:
        ...
