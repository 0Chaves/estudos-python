def calcular_desconto(valor_total):
    return valor_total * 0.95

def catalogo():
    return "\nCódigo, Produto, Preço Unitário \n101, Shampoo, 10,00 \n102, Condicionador, 12,00 \n103, Sabonete, 3,00 \n104, Creme dental, 15,00 \n0 Sair"

def print_produtos(nota_fiscal):
    for item in nota_fiscal:
        print(f"{nota_fiscal.index(item) + 1}. {item.produto.nome} - qtd: {item.quantidade} - valor_uni: {item.produto.preco} - valor: {item.quantidade * item.produto.preco}\n")

class Produto:
    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco

class Item:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade
 
produtos = [Produto(104, "Creme dental", 15.0), Produto(103, "Sabonete", 3.0), Produto(102, "Condicionador", 12.0), Produto(101, "Shampoo", 10.0)]

# Produto
cod = -1
quantidade = 0

# Nota fiscal
nota_fiscal = []
valor_total = 0.0
tipo_pagamento = -1

while cod != 0:
    print(catalogo())
    cod = int(input("Digite o codigo do produto: "))
    if cod == 0:
        break
    if cod == 101 or cod == 102 or cod == 103 or cod == 104:
        while quantidade <= 0:
            quantidade = int(input("Digite a quantidade: "))
            for produto in produtos:
                if produto.codigo == cod:
                    item = Item(produto, quantidade)
                    nota_fiscal.append(item)
                    break
        quantidade = 0
    else:
        print("\nCodigo invalido\n")

for item in nota_fiscal:
    valor_total += item.produto.preco * item.quantidade

while tipo_pagamento != 1 and tipo_pagamento != 2:
    tipo_pagamento = int(input("Qual a forma de pagamento? \n1 - Débito \n2 - Crédito\n"))

if tipo_pagamento == 1:
    print_produtos(nota_fiscal)
    print(f"Valor total com desconto de 5%: R$ {calcular_desconto(valor_total)}")
else:
    print_produtos(nota_fiscal)
    print(f"Valor total: R$ {valor_total}")