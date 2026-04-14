from enum import Enum, unique

@unique #não permite que haja valores repetidos no enum
class Meses(Enum):
    JANEIRO = 1
    FEVEREIRO = 2
    MARÇO = 3
    ABRIL = 4
    MAIO = 5
    JUNHO = 6
    JULHO = 7
    AGOSTO = 8
    SETEMBRO = 9
    OUTUBRO = 10
    NOVEMBRO = 11
    DEZEMBRO = 12

class Funcionario:
    meses = [mes.name for mes in Meses]

    __slots__ = ["nome", "email", "valor_hora"] #proibe o objeto criado de criar novos atributos em tempo de execução, e evita criação de dicionario para os atributos
    def __init__(self, nome, email, valor_hora):
        self.nome = nome
        self.email = email
        self.valor_hora = valor_hora
        self.horas_trabalhadas: dict [str, int] = {}
        for mes in self.meses:
            self.horas_trabalhadas[mes] = 0

    def mostrar_horas(self):
        print(f"{self.horas_trabalhadas}")

    def cadastrar_horas (self, mes, horas):
        if mes in self.meses:
            self.horas_trabalhadas[mes] = horas
            print(f"Confirma: {self.horas_trabalhadas}")
        
    def salario_mensal (self, mes):
        if mes in self.meses:
            salario = self.horas_trabalhadas[mes] * self.valor_hora
            return salario
    
    def relatorio (self):
        pass
    
    def media_salarial (self):
        pass

    def getNome(self):
        return self.__nome
    
    def setNome(self, nome):
        self.__nome = nome

    def getEmail(self):
        return self.email
    
    def __str__(self):
        return f"Funcionario: {self.__nome}, email: {self.email}"

    def __eq__(self, value):
        if not isinstance (value, Funcionario):
            return False
        return self.__nome == value.__nome