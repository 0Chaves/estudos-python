class Funcionario:
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

    def __init__(self, nome, email, valor_hora):
        self.__nome = nome
        self.email = email
        self.valor_hora = valor_hora
        self.horas_trabalhadas = {}
        for mes in self.meses:
            self.horas_trabalhadas[mes] = 0

    def mostrar_horas(self):
        print(f"{self.horas_trabalhadas}")

    def cadastrar_horas (self, mes, horas):
        self.horas_trabalhadas[mes] = horas
        print(f"Confirma: {self.horas_trabalhadas}")
        
    def salario_mensal (self):
        pass
    
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