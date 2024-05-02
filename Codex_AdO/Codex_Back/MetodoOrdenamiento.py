from abc import ABC, abstractmethod


class MetodoOrdenamiento(ABC):
    @staticmethod
    @abstractmethod
    def sort(arr: list) -> list:
        ...
