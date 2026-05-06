from radio import Radio
from relogio_digital import RelogioDigital
from interruptor_mixin import Interruptor_MixIn

class Despertador(Interruptor_MixIn, Radio, RelogioDigital):
    def __init__(self, marca, modelo, volume, hora, minuto):
        Radio.__init__(self, marca, modelo, volume)
        RelogioDigital.__init__(self, marca, modelo, hora, minuto)
        

    def configurar_alarme(self, hora, minuto):
        self.hora = hora
        self.minuto = minuto
        print(f"Alarme configurado para {self.hora:02d}:{self.minuto:02d}.")

    def ativar_alarme(self):
        self.ativado = True
        print("Alarme ativado.")

    def desativar_alarme(self):
        self.ativado = False
        print("Alarme desativado.")