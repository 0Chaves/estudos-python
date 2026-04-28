from estacao import Estacao

class Radio:
    def __init__(self, marca, modelo, volume = 1):
        self.marca = marca
        self.modelo = modelo
        self.estacoes = [Estacao]
        self.ligado = False
        self.volume = volume
    
    def adicionar_estacao(self, estacao):
        self.estacoes.append(estacao)
        print(f"Estação {estacao} adicionada ao rádio {self.marca} {self.modelo}.")

    def ligar(self):
        self.ligado = True
        print(f"O rádio {self.marca} {self.modelo} está ligado.")

    def desligar(self):
        self.ligado = False
        print(f"O rádio {self.marca} {self.modelo} está desligado.")

    def aumentar_volume(self):
        if self.volume < 10:
            self.volume += 1
            print(f"Volume aumentado para {self.volume}.")
        else:
            print("Volume já está no máximo.")

    def diminuir_volume(self):
        if self.volume > 0:
            self.volume -= 1
            print(f"Volume diminuído para {self.volume}.")
        else:
            print("Volume já está no mínimo.")

    def sintonizar_estacao(self, estacao):
        if estacao in self.estacoes:
            print(f"Sintonizando na estação {estacao}...")
        else:
            print(f"A estação {estacao} não está disponível no rádio {self.marca} {self.modelo}.")  