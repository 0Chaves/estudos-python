from radio import Radio
from relogio_digital import RelogioDigital
from estacao import Estacao
from despertador import Despertador

if __name__ == "__main__":
    print("-----Testando o rádio:-----")
    estacao1 = Estacao("Atlantida", 101.5)
    estacao2 = Estacao("JovemPam", 600)
    estacao3 = Estacao("Radio Osório", 99.9, fm=False)
    radio = Radio("Sony", "X123")
    radio.adicionar_estacao(estacao1)
    radio.adicionar_estacao(estacao2)
    radio.ligar()
    radio.aumentar_volume()
    radio.sintonizar_estacao(estacao3)
    radio.sintonizar_estacao(estacao2)
    radio.desligar()

    print("\n-----Testando o relógio digital:-----")
    relogio1 = RelogioDigital("Casio", "DigiTime")
    relogio1.ajustar_hora(14, 30)
    relogio1.ligar()
    relogio1.exibir_horario()
    relogio1.desligar()

    print("\n-----Testando o despertador:-----")
    despertador = Despertador("Sony", "X123", volume=7, hora=6, minuto=30)
    despertador.ligar()
    despertador.configurar_alarme(6, 30)
    despertador.ativar_alarme()
    despertador.aumentar_volume()
    despertador.sintonizar_estacao("Estação FM")
    despertador.desativar_alarme()
    despertador.desligar() 
