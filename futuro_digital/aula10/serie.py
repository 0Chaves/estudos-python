from dataclasses import dataclass, field
from temporada import Temporada
from genero import Genero

@dataclass(slots=True)
class Serie:
    titulo: str
    genero: Genero
    imdb: float
    temporadas: list[Temporada] = field(default_factory=list)
    visto: bool = False

    def adicionar_temporada(self, temporada):
        if not isinstance (temporada, Temporada):
            return False
        if temporada in self.temporadas:
            print("Temporada já existente")
            return False
        self.temporadas.append(temporada)
        return True
    
    def remover_temporada(self, temporada):
        if not isinstance (temporada, Temporada):
            return False
        if temporada in self.temporadas:
            self.temporadas.remove(temporada)
            return True
        return False
    
    def verificar_visto(self):
        for temporada in self.temporadas:
            if temporada.visto == False:
                self.visto = False
                return True
        self.visto = True
        return True
    
    def alternar_visto(self):
        if self.visto == False:
            for temporada in self.temporadas:
                if temporada.visto == False:
                    temporada.alternar_visto()
        if self.visto == True:
             for temporada in self.temporadas:
                if temporada.visto == True:
                    temporada.alternar_visto()
        self.visto = not self.visto
        return True
