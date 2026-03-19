print("--------------Match Case-------------")
n = int(input("Digite um numero: "))
match n:
    case 1: print("Digitou um")
    case 2: print("Digitou dois")
    case 3: print("Digitou tres")
    case 4: print("Digitou quatro")
    case 5: print("Digitou cinco")
    case _: print("Digitou numero que nao esta entre 1 e 5")


print("----------Definição de funções------------")
def verificar_dia_util(dia):
    match dia.lower().strip():
        case "sabado" | "domingo":
            return "Fim de semana"
        case "segunda" | "terca" | "quarta" | "quinta" | "sexta":
            return "Dia util"
        case _:
            return "Dia invalido"

dia = input("Digite o dia da semana: ")
print(verificar_dia_util(dia))

print("---------None para retorno não numérico---------")
def operacao(n1, n2, op):
    match op:
        case '+':
            return n1 + n2
        case '-':
            return n1 - n2
        case '*':
            return n1 * n2
        case '/':
            if(n2 != 0):
                return n1 / n2
            else:
                print("Divisão por 0")
                return None
        case _:
            return None

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
op = input("Digite a operacao (+, -, *, /)")
resultado = operacao(n1,n2,op)
print(f"Resultado: {resultado}")



print("---------Desafio - Imprimir os algarismos de um número----------")
def alg(numero):
    if(numero >= 0 and numero <= 1000):
        unidade = numero % 10
        dezena = int((numero % 100) / 10)
        if numero == 1000:
            centena = 10
        else:
            centena = int(numero / 100)
        return [unidade, dezena, centena]
    return None

n = -1
algarismos = []
while n < 0 or n > 1000:
    n = int(input("Digite um numero de 0 a 1000: "))
algarismos = alg(n)
print(f"Unidade: {algarismos[0]} \nDezena: {algarismos[1]} \nCentena: {algarismos[2]}")
