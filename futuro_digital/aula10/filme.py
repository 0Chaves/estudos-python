from dataclasses import dataclass, field
from futuro_digital.aula10.genero import Genero

@dataclass
class Filme:
    titulo: str
    diretor: str
    ano: int
    imdb_rating: float
    visto: bool = False
    generos: list[Genero] = field(default_factory=list)
    #genero: Genero #para caso fosse apenas um genero, a criação da variavel seria assim
    
    def __post_init__ (self):
        if self.ano < 1895:
            print("O ano de lançamento do filme deve ser maior ou igual que 1895")

    def adicionar_genero(self, genero: Genero):
        if genero not in self.generos:
            self.generos.append(genero)
    