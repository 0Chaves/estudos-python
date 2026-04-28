from sms_mixin import Sms_mixin
from telefone_mixin import Telefone_mixin

class Celular(Sms_mixin, Telefone_mixin):
    def __init__(self, numero, marca, modelo):
        self.numero = numero
        self.marca = marca
        self.modelo = modelo
