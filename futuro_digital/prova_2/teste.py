from nave_guerra import NaveGuerra
from sistema_defesa_mixin import SistemaDefesaMixin
from missao_invalida_erro import MissaoInvalidaErro
from pessoa_tripulacao import PessoaTripulacao     
from posto_enum import PostoEnum

def teste1():
    print("----------- TESTE 1 -----------------")
    try:
        pessoa4 = PessoaTripulacao("Luiz", idade=50, anos_experiencia=30, posto=PostoEnum.CAPITAO)
        nave = NaveGuerra(nome = "Enterprise", capitao=pessoa4)
        pessoa1 = PessoaTripulacao("Pedro", idade=25, anos_experiencia=3, posto=PostoEnum.CABO)
        nave.adicionar_tripulante(pessoa1)
        pessoa2 = PessoaTripulacao("Maria", idade=30, anos_experiencia=5, posto=PostoEnum.SARGENTO)
        nave.adicionar_tripulante(pessoa2)
        pessoa3 = PessoaTripulacao("Joao", idade=40, anos_experiencia=10, posto=PostoEnum.TENENTE)
        nave.adicionar_tripulante(pessoa3)
        pessoa5 = PessoaTripulacao("Bruna", idade=60, anos_experiencia=40, posto=PostoEnum.ALMIRANTE)
        nave.adicionar_tripulante(pessoa5)
        pessoa6 = PessoaTripulacao("Bruna", idade=60, anos_experiencia=40, posto=PostoEnum.ALMIRANTE)
        nave.adicionar_tripulante(pessoa6)
        
        nave.abastecer(100)
        texto = nave.preparar_para_decolagem()
        print(texto)
        texto = nave.decolar()
        print(texto)
        if not nave.status:
            print("nave indisponíel para outras missões")
        texto = nave.pousar()
        print(texto)  
        if nave.status:
            print("nave pronta apara outras outras missões")  
    except Exception as mie:
        print(mie)

def teste2():
    print("----------- TESTE 2 -----------------")
    #tratamento de erros na criacao de pessoa_tripulante com menos de 18 anos
    try:
        pessoa1 = PessoaTripulacao("Pedro", idade=16, anos_experiencia=3, posto=PostoEnum.CABO)
    except ValueError as ve:
        print(ve)

    #tratamento de erros na criacao de pessoa_tripulante com anos_experiencia >  idade
    try:
        pessoa1 = PessoaTripulacao("Pedro", idade=20, anos_experiencia=23, posto=PostoEnum.CABO)
    except ValueError as ve:
        print(ve)

def teste3():
    print("----------- TESTE 3 -----------------")
    pessoa4 = PessoaTripulacao("Luiz", idade=50, anos_experiencia=30, posto=PostoEnum.CAPITAO)
    nave = NaveGuerra(nome = "Enterprise", capitao=pessoa4)
    #tratamento de erros na adição de tripulantes duplicados
    try:
        pessoa1 = PessoaTripulacao("Pedro", idade=25, anos_experiencia=3, posto=PostoEnum.CABO)
        nave.adicionar_tripulante(pessoa1)
        nave.adicionar_tripulante(pessoa1)
    except ValueError as ve:
        print(ve)

    #tratamento de erros na adição de combustível
    try:
        nave.abastecer(100)
        print(f"Quantidade de combustivel = {nave.nivel_combustivel}")
        nave.abastecer(10)
    except ValueError as ve:
        print(ve)

def teste4():
    print("----------- TESTE 4 -----------------")
    pessoa4 = PessoaTripulacao("Luiz", idade=50, anos_experiencia=30, posto=PostoEnum.CAPITAO)
    nave = NaveGuerra(nome = "Enterprise", capitao=pessoa4)
    pessoa1 = PessoaTripulacao("Pedro", idade=25, anos_experiencia=3, posto=PostoEnum.CABO)
    nave.adicionar_tripulante(pessoa1)
    pessoa2 = PessoaTripulacao("Maria", idade=30, anos_experiencia=5, posto=PostoEnum.SARGENTO)
    nave.adicionar_tripulante(pessoa2)
    pessoa3 = PessoaTripulacao("Joao", idade=40, anos_experiencia=10, posto=PostoEnum.TENENTE)
    nave.adicionar_tripulante(pessoa3)
    pessoa5 = PessoaTripulacao("Bruna", idade=60, anos_experiencia=40, posto=PostoEnum.ALMIRANTE)
    
    #tratamento de erro por atribuir alguém ao posto de capitão com patente inferior a TENENTE
    try:
        nave.capitao = pessoa3
    except MissaoInvalidaErro as mie:
        print(mie)   

    #tratamento de erro por falta de combustível 
    try:
        nave.preparar_para_decolagem()
    except MissaoInvalidaErro as mie:
        print(mie)   

    #tratamento de erro por falta de almirante na tripulação
    # try:
    #     nave.abastecer(90)
    #     nave.preparar_para_decolagem()
    # except MissaoInvalidaErro as mie:
    #     print(mie)  


if __name__ == "__main__":
    teste1()
    # teste2()
    # teste3()
    # teste4()