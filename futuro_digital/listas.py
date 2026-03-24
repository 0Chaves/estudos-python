def imprime_lista (lista):
    for item in lista:
        print(item)

lista_frutas = ['pera', 'uva', 'maçã', 'kiwi', 'abacaxi']
print("Lista original")
imprime_lista(lista_frutas)

lista_frutas.sort()
print("Lista ordenada")
imprime_lista(lista_frutas)

print("\nTerceiro elemento da lista = " + lista_frutas[2])
lista_frutas[1] = "banana"
print("\nLista com substituição = ")
imprime_lista(lista_frutas)

lista_frutas.append("abacate")

lista_frutas.remove("maçã")

lista_frutas.pop(-1)

print('\n')
imprime_lista(lista_frutas)

print("\nTamanho da lista = " + str(len(lista_frutas)))

lista_frutas.sort(reverse=True)

print("\nLista ao contrario = ")
imprime_lista(lista_frutas)

print("Frutas menos banana")
for fruta in lista_frutas:
    if fruta != "banana":
        print(fruta)

