from validate_docbr import CPF
validador_cpf = CPF()

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
    
    @property
    def nome(self):
        return self._nome
    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def cpf(self, novo_cpf):
        if validador_cpf.validate(novo_cpf):
            self._cpf = novo_cpf
        print("Cpf invalido")