
print("--------------LISTAS-------------------")
cidades = ["São Paulo", 0, "Osório", "Porto Alegre"]
print(id(cidades))
print(type(cidades))
print()
print(cidades[0])
print(cidades[1])
print(cidades[2])
print(cidades[-3])

cidades.insert(1, 'Nova Bassano')
print(cidades)
cidades.remove(0)
print(cidades)
cidades.append("Rio de Janeiro")
print(cidades)
cidades[1] = "Tramandai"
print(cidades)
print(id(cidades))
for cidade in cidades:
    print(cidade)

print("----------------DICIONARIOS------------------")
cidades = {
    'Veranopolis': 100,
    'Nova Bassano': 80,
    'Nova Prata': 90
}

print(type(cidades))

print(cidades.keys())
print(cidades.values())
print(cidades.items())
print(cidades['Veranopolis'])
cidades['nova prata'] = 95
cidades['Nova Prata'] = 495
print(cidades.items())

print("-----------------Conjuntos------------------")

numerosInteiros = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
numerosImpares = [1,3,5,7,9,11,13,15,17,19]
numerosPrimos = {2,3,5,7,11,13,17,19}
cidadesDict = {'Veranopolis': 100, 'Camboriu': 123}
cidadesSet = {'Veranopolis', 'Camboriu'}

inteiros = set(numerosInteiros)
impares = set(numerosImpares)
primos = set(numerosPrimos)

print('Inteiros:', inteiros)
print('Impares:', impares)
print('Primos:', primos)

print("Classe das cidadesDict: ", type(cidadesDict))
print("Classe das cidadesSet: ", type(cidadesSet))
print(type(numerosInteiros), type(numerosImpares), type(numerosPrimos))
print(type(inteiros), type(impares), type(primos))

interseccao = impares.intersection(primos)
print("Int: ", interseccao)
diferenca = impares.difference(primos)
print("Dif:", diferenca)
uniao = impares.union(primos)
print("Uni:", uniao)

print("----------Laços de Repeticao-----------")

frutas = ['Morango', 'Limão', 'Uva', 'Abacaxi']

for f in frutas:
    print(f)

for _ in frutas:
    print("Frutas caindo...")

# De 0 a <= valor
for i in range(10):
    print(i)

# Valor inicial a <= valor final
for i in range(1,10):
    print(i)

# Incrementos de 2 em 2
for i in range(0,10,2):
    print(i)

# Decrementos de 2 em 2
for i in range(10,0,-2):
    print(i)

print("--------------Definicao de Funcoes------------")

def hello():
    print("Hello World!")

def saudacao(nome):
    print("Olá, ", nome)

def soma(num1, num2):
    s = num1 + num2
    return s

hello()
saudacao('Daniel')
print(soma(4, 7))

print("---------------Exercicios-------------")

dado = input("Insira uma nota de 0 a 10 \n")
nota = 0
try:
    nota = int(dado)
    while nota < 0 or nota > 10:
        nota = int(input("Valor inválido. Insira uma nota entre 0 e 10 \n"))
    print("Nota: ", nota)
except:
    print("Valor fornecido não é um número")


lista = []
for i in range(0,5):
    print("Digite o numero", i+1, "de 5")
    num = int(input())
    lista.append(num)
print("O maior numero foi:", max(lista))
print("O menor numero foi: ", min(lista))
print("A media dos numeros e: ", sum(lista)/5)

def tabuada(numero):
    print("Tabuada do", numero)
    for i in range(1,11):
        print(numero, "x", i, "=", numero*i)
tabuada(7)