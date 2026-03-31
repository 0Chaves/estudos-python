def valida_categoria(categoria):
    if(categoria == "ALIMENTO" or categoria == "HIGIENE" or categoria == "LIMPEZA"):
        return True
    return False


def agrupar_por_categoria(lista_compras: dict[str, str, float]):
    lista_agrupada = {
        "ALIMENTO": 0.0,
        "LIMPEZA": 0.0,
        "HIGIENE": 0.0
    }
    for value in lista_compras.values():
        lista_agrupada[value[0]] += value[1]
    
    return lista_agrupada

def verificar_produto_mais_caro_por_categoria(lista_compras: dict[str, str, float]):
    lista_mais_caro = {
        "ALIMENTO": ("Nada inserido", 0.0),
        "LIMPEZA": ("Nada inserido", 0.0),
        "HIGIENE": ("Nada inserido", 0.0)
    }
    for key,value in lista_compras.items():
        if(value[1] > lista_mais_caro[value[0]][1]):
            lista_mais_caro[value[0]] = (key, value[1])
    
    return lista_mais_caro
    

def calcular_gasto_total(lista_compras: dict[str, str, float]):
    soma = 0.0
    for valores in lista_compras.values():
        soma += valores[1]
    return soma


opcao = -1
produto_dict = dict[str, str, float]
lista_compras: produto_dict = {}

# lista_compras["Maçã"] = ("Alimento".upper(), 5.5)
# lista_compras["Detergente"] = ("Limpeza".upper(), 12.0)
# lista_compras["Banana"] = ("Alimento".upper(), 3.0)
# lista_compras["Sabonete"] = ("Higiene".upper(), 4.5)
# lista_compras["Arroz"] = ("Alimento".upper(), 25.0)
# lista_compras["Esponja"] = ("Limpeza".upper(), 2.0)

while(opcao != 0):
    print("""
    0 - Sair
    1 - Cadastrar nova produto (nome do produto, categoria e preço) 
    2 - Exibir relatório total de gastos por categoria (Alimento, Limpeza, Higiene)
    3 - Exibir o produto mais caro de cada categoria
    4 - Exibir gasto total
     """)
    opcao = int(input("\n"))
    match opcao:
        case 0:
            break
        case 1:
            nome_produto = input("Digite o nome do produto: ").capitalize()
            categoria = input("Digite a categoria (Alimento, Higiene, Limpeza): ")
            categoria_formatada = categoria.upper()
            while (valida_categoria(categoria_formatada) != True):
                print("Categoria incorreta. Categorias permitidas são ALIMENTO, HIGIENE, LIMPEZA: ")
                categoria = input("Digite novamente: ")
                categoria_formatada = categoria.upper()
            valor = float(input("Digite o valor: "))
            lista_compras[nome_produto] = (categoria_formatada, valor)
            print(f"\nInserido: {nome_produto} {lista_compras[nome_produto]}")
        case 2:
            lista_agrupada = agrupar_por_categoria(lista_compras)
            for key,value in lista_agrupada.items():
                print(f"\n{key}: {value:.2f}")
        case 3:
            lista_mais_caro = verificar_produto_mais_caro_por_categoria(lista_compras)
            for key,value in lista_mais_caro.items():
                print(f"\n{key}: {value}")
        case 4:
            gasto_total = calcular_gasto_total(lista_compras)
            print(f"\nGasto total: {gasto_total:.2f}")
        case _:
            print("Opção inválida")
