from filme import Filme
from generoFilme import GeneroFilme
from playlist import Playlist

if __name__ == "__main__":
    filme1 = Filme("O Poderoso Chefão", "Francis Ford Coppola", 1972, 9.2)
    filme1.adicionar_genero(GeneroFilme.DRAMA)
    filme1.adicionar_genero(GeneroFilme.POLICIAL)
    filme2 = Filme("A Origem", "Christopher Nolan", 2010, 8.8)
    filme2.adicionar_genero(GeneroFilme.ACAO)
    filme3 = Filme("O Grande Hotel Budapeste", "Wes Anderson", 2014, 8.1)
    filme3.adicionar_genero(GeneroFilme.COMEDIA)
    filme4 = Filme("Parasita", "Bong Joon-ho", 2019, 8.6)
    filme4.adicionar_genero(GeneroFilme.DRAMA)
    filme4.adicionar_genero(GeneroFilme.SUSPENSE)
    filme5 = Filme("A Viagem de Chihiro", "Hayao Miyazaki", 2001, 8.6, generos=[GeneroFilme.AVENTURA])
    print(filme5)
    filme5.adicionar_genero(GeneroFilme.FICCAO_CIENTIFICA)
    print(filme5)