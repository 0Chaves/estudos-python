class RelogioDigital:
    def __init__(self, marca, modelo, hora = 0, minuto = 0):
        self.marca = marca
        self.modelo = modelo
        self.hora = hora
        self.minuto = minuto
        self.ligado = False

    def exibir_horario(self):
        print(f"Agora sao {self.hora:02d}:{self.minuto:02d}")
    
    def ajustar_hora(self, hora, minuto):
        if 0 <= hora < 24 and 0 <= minuto < 60:
            self.hora = hora
            self.minuto = minuto
            print(f"Hora ajustada para {self.hora:02d}:{self.minuto:02d}.")
        else:
            print("Hora ou minuto inválidos. Por favor, insira valores válidos.")
    
    def ligar(self):
        self.ligado = True
        print(f"O relógio digital {self.marca} {self.modelo} está ligado.") 

    def desligar(self):
        self.ligado = False
        print(f"O relógio digital {self.marca} {self.modelo} está desligado.")  