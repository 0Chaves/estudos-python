from dataclasses import dataclass

@dataclass(slots=True)
class Editora:
    nome: str
    cnpj: str