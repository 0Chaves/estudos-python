from dataclasses import dataclass
from posto_enum import PostoEnum

@dataclass
class PessoaTripulacao:
    nome: str
    posto: PostoEnum
    idade: int
    anos_experiencia: int

    def __post_init__(self):
        if(self.idade < 18):
            raise ValueError("Membros da tripulacao devem ter pelo menos 18 anos")
        if(self.anos_experiencia > self.idade):
            raise ValueError("O tempo de experiencia deve ser menor do que a idade")
        