#Definição da estrutura de dados para armazenar
produto = dict[str, float]
lista_produtos: produto = {}

#Preenchendo o dicionário com os produtos e seus valores
lista_produtos['leite'] = 4.00
lista_produtos['ovos'] = 12.50
lista_produtos['pao'] = 2.50

#Exibindo os produtos e seus valores
def imprimir_dicionario(dicionario: dict[str, float]):
    for key,value in lista_produtos.items():
        print(f"{key}: {value:.2f}")

print("----------Produtos:")
imprimir_dicionario(lista_produtos)

#Alterando valores
lista_produtos['leite'] = 3.00
lista_produtos['bolacha'] = 8.00

print("\n----------------Produtos atualizados: ")
imprimir_dicionario(lista_produtos)

#Buscar um item com get atraves da chave, retorna o valor OU o valor default caso nao seja encontrado nenhuma chave
item1 = lista_produtos.get('banana', 0)
item2 = lista_produtos.get('leite', 'Produto nao encontrado')
print(f"\n---------Busca por produtos:\nValor banana:{item1} \nValor leite:{item2}")

#Remover uma chave:valor tem duas formas
valor_removido = lista_produtos.pop('bolacha')
del lista_produtos["ovos"]

print(f"Valor removido (e chave também é removida): {valor_removido}\n {lista_produtos}")

