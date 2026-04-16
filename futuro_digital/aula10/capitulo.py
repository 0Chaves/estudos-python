from dataclasses import dataclass
from datetime import date
@dataclass(slots=True)
class Capitulo:
    titulo: str
    numero: int
    data: date = date.today()
    visto: bool = False

    def alternar_visto(self):
        self.visto = not self.visto
        return True
