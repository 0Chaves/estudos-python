from dataclasses import dataclass
import datetime

@dataclass(slots=True)
class Capitulo:
    titulo: str
    numero: int
    data: datetime.date = datetime.date.today()
    visto: bool = False

    def alternar_visto(self):
        self.visto = not self.visto
        return True
