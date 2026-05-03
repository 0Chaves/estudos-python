from midia import Midia
from editora import Editora
from dataclasses import dataclass

@dataclass
class Livro(Midia):
    autor: str
    isbn: str
    editora: Editora = None

    def reproduzir(self):
        print(f"Lendo o livro '{self.titulo}' de {self.autor} ({self.ano}) - Editora: {self.editora.nome}")

    def definir_editora(self, editora: Editora):
        self.editora = editora