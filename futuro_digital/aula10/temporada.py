from dataclasses import dataclass, field
from capitulo import Capitulo

@dataclass(slots=True)
class Temporada:
    ano: int
    capitulos: list[Capitulo] = field(default_factory=list)
    visto: bool = False


    def adicionar_capitulo(self, capitulo: Capitulo):
        if capitulo in self.capitulos:
            print("Capitulo já adicionado")
            return False
        self.capitulos.append(capitulo)
        return True
    
    def remover_capitulo(self, capitulo: Capitulo):
        if capitulo in self.capitulos:
            self.capitulos.remove(capitulo)
            return True
        return False
    
    def verificar_visto(self):
        for capitulo in self.capitulos:
            if capitulo.visto == False:
                self.visto = False
                return True
        self.visto = True
        return True
    
    def alternar_visto(self):
        if self.visto == False:
            for capitulo in self.capitulos:
                if capitulo.visto == False:
                    capitulo.alternar_visto()
        if self.visto == True:
            for capitulo in self.capitulos:
                if capitulo.visto == True:
                    capitulo.alternar_visto()
        self.visto = not self.visto
        return True