from nave_base import NaveBase
from sistema_defesa_mixin import SistemaDefesaMixin
from pessoa_tripulacao import PessoaTripulacao
from missao_invalida_erro import MissaoInvalidaErro

class NaveGuerra(NaveBase, SistemaDefesaMixin):
    def __init__(self, nome: str, nivel_combustivel: int = 0, capitao: PessoaTripulacao = None):
        super().__init__(nome, nivel_combustivel)
        self.capitao = capitao
    
    @property
    def capitao(self):
        return self._capitao.nome
    
    @capitao.setter
    def capitao(self, capitao: PessoaTripulacao):
        if(capitao.posto.value < 3):
            raise MissaoInvalidaErro(f"A pessoa designada como capitao na verdade é um {capitao.posto.name}")
        self.tripulacao.append(capitao)
        self._capitao = capitao

    def preparar_para_decolagem(self):
        if(self.nivel_combustivel > 80 and self.tripulacao):
            return f"{self.nome} pronta para decolagem com comandante {self._capitao.nome}"
        raise MissaoInvalidaErro("A nave ainda não está pronta para decolagem")