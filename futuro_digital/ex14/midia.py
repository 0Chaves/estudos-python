from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass(slots=True)
class Midia(ABC):
    titulo: str
    ano: int

    @abstractmethod
    def reproduzir(self):
        pass

    def __post_init__(self):
        if self.ano <= 1900:
            raise ValueError("Ano precisa ser maior que 1900")