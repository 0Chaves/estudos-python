from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pessoa_tripulacao import PessoaTripulacao
from missao_invalida_erro import MissaoInvalidaErro

@dataclass
class NaveBase(ABC):
    nome: str
    nivel_combustivel: int
    status: bool = True
    tripulacao: list[PessoaTripulacao] = field(default_factory=list)
    integridade_casco: int = 100

    def __post_init__(self):
        if(self.nivel_combustivel < 0 or self.nivel_combustivel > 100):
            raise ValueError("Nivel do combustivel deve estar entre 0 e 100")
        if(self.integridade_casco < 0 or self.integridade_casco > 100):
            raise ValueError("Integridade do casco deve estar entre 0 e 100")
        

    @abstractmethod
    def preparar_para_decolagem(self):
        pass

    def exibir_status(self):
        return f"{self.nome}: {self.status}"
    
    def adicionar_tripulante(self, tripulante: PessoaTripulacao):
        if(tripulante in self.tripulacao):
            raise ValueError(f"{tripulante.nome} já está na tripulação de {self.nome}")
        self.tripulacao.append(tripulante)

    def abastecer(self, combustivel: int):
        if((self.nivel_combustivel + combustivel) > 100):
            raise ValueError("Muito combustivel ! Vai transbordar !")
        self.nivel_combustivel += combustivel
    
    def decolar(self):
        if(not self.status):
            return "Nave indisponivel para decolagem"
        self.status = False
        return "Nave decolando"

    def pousar(self):
        if(self.status):
            return "Nave já está disponível"
        self.status = True
        return "Nave pousando"