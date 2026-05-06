import random

numero_aleatorio = random.randint(1,100)
numero_tentativa = -1
numeros_tentados = []
count = 0

print(numero_aleatorio)

while numero_tentativa != numero_aleatorio:
    numero_tentativa = int(input("Adivinhe o numero de 1 a 100: "))
    numeros_tentados.append(numero_tentativa)
    count+=1
    if numero_tentativa != numero_aleatorio:
        print("Numero errado, tente novamente\n")
    
print(f"Você acertou!\nTentativas: {count}\nNumero correto: {numero_aleatorio}\nNumeros tentados: {numeros_tentados}")
