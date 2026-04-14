from dataclasses import dataclass, field
from filme import Filme

@dataclass
class Playlist:
    nome: str
    descricao: str
    filmes: list [Filme] = field(default_factory=list)

    def adicionar(self, filme):
        if not isinstance (filme, Filme):
            return False
        if filme not in self.filmes:
            self.filmes.append(filme)
            return True

    def remover(self, filme):
        if not isinstance (filme, Filme):
            return False
        if filme in self.filmes:
            self.filmes.remove(filme)
            return True