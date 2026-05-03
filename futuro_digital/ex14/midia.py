from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass(slots=True)
class Midia(ABC):
    titulo: str
    ano: int

    @abstractmethod
    def reproduzir(self):
        pass