from livro import Livro
from narrador import Narrador

class Audio_Livro(Livro):
    def __init__(self, titulo: str, autor: str, ano: int, isbn: str, narrador: Narrador, tempoLeitura: int):
        super().__init__(titulo, ano, autor, isbn)
        self.tempoLeitura = tempoLeitura
        self.narrador = narrador

    def reproduzir(self, velocidade: int = 1):
        print(f"O livro está sendo lido na velocidade {velocidade}")