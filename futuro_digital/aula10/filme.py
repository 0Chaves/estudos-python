from dataclasses import dataclass, field

class Filme:
    titulo: str
    diretor: str
    ano: int
    imdb_rating: float
    visto: bool = False
    
    def __post_init__ (self):
        if self.ano < 1895:
            print("O ano de lançamento do filme deve ser maior ou igual que 1895")
    