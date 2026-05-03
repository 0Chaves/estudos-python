def verificar_saborExiste(sabor: str) -> bool:
    return nome in lista_sabores

def buscar_por_codigo (codigo: str):
    '''busca um sabor pelo código e retorna o dicionario  ou None'''
    for sabor in lista_sabores:
        if sabor ['codigo'].upper() == codigo.upper():
            return sabor
    return None 

def imprimir_sabores (lista_sabores: list[dict]):
    '''Imrpime sabores quando há uma lista de dicionarios'''
    for sabor in lista_sabores:
        codigo = sabor.get('codigo', '----')
        nome = sabor.get('nome', 'desconhecido')
        preço = sabor.get('preço', 0.0)
        print(f'{codigo}, {nome.capitalize()}, R$ {preço:.2f}')



#------------------------------------------------------------------------
lista_sabores: dict[str, str, float] = {}
lista_sabores = [
    {'código': 'M001', 'nome': 'morango', 'preço': 2.50},
    {'código': 'C002', 'nome': 'chocolate', 'preço': 3.00},
    {'código': 'C003', 'nome': 'coco', 'preço': 1.50},
    {'código': 'U004', 'nome': 'uva', 'preço': 1.00},
    {'código': 'A005', 'nome': 'abacaxi', 'preço': 1.00},
    {'código': 'P006', 'nome': 'pistache', 'preço': 4.00},
    {'código': 'M007', 'nome': 'maca', 'preço': 0.50},
    {'código': 'P008', 'nome': 'pessego', 'preço': 0.75} 
]
#------------------------------------------------------------------------
lista_saboresdisponiveis: dict[str, str, float] = {}
lista_saboresdisponiveis = [
    {'código': 'M001', 'nome': 'morango', 'preço': 2.50},
    {'código': 'C003', 'nome': 'coco', 'preço': 1.50},
    {'código': 'U004', 'nome': 'uva', 'preço': 1.00},
    {'código': 'A005', 'nome': 'abacaxi', 'preço': 1.00},
    {'código': 'M007', 'nome': 'maca', 'preço': 0.50},
]
#------------------------------------------------------------------------
lista_saboresindisponiveis: dict[str, str, float] = {}
lista_saboresindisponiveis = [
    {'código': 'C002', 'nome': 'chocolate', 'preço': 3.00},
    {'código': 'P006', 'nome': 'pistache', 'preço': 4.00},
    {'código': 'P008', 'nome': 'pessego', 'preço': 0.75} 
]
#------------------------------------------------------------------------
carrinho: list[dict] = []
#Para armazenar os códigos do item 4, tornando possivel a soma no item 5
#------------------------------------------------------------------------

print ('Olá, seja bem-vindo a sorveteria SaborRosa, em que podemos ajudar?')

opcao = 0
codigo = 1
quant = 0

while (opcao != 8):
    print ('\nPor favor, escolha uma das opções abaixo:')
    print ('''
    1- Cadastrar um novo sabor (nome, código, valor)
    2- Ver lista dos sabores disponiveis
    3- Ver lista dos sabores indisponiveis
    4- Selecionar sorvetes escolhidos (pelo código)
    5- Valor final da compra
    6- Adicionar sabor disponivel
    7- Adicionar sabor indisponivel
    8- Ver lista de todos os sabores
    9- Sair''')

    opcao = int(input("Digite a opção desejada:"))
    if opcao == 9:
        print("Encerrando o programa. Até mais!")
        exit()
    if opcao <1 or opcao > 9:
        print("Opção inválida. Digite um número entre 1 e 9.")
        continue
    else:
        match opcao:
            case 1:
                nome = input('digite o nome do sabor:')
                codigo = input('digite o codigo:')
                preço = float(input('digite o preço:'))
                lista_sabores[nome]=(codigo, preço)
                existe = verificar_saborExiste(nome)
                if not existe:
                    print('sabor cadastrado com sucesso')
                    break
                else:
                    print('sabor já existente no sistema')

            case 2:
                if lista_saboresdisponiveis:
                    imprimir_sabores(lista_saboresdisponiveis)
                else:
                    print('Nenhum sabor disponivel no momento')

            case 3:
                if lista_saboresindisponiveis:
                    imprimir_sabores(lista_saboresindisponiveis)
                else:
                    print('Nenhum sabor indisponivel no momento')
#--------------------------------------------------------------------------------------------------
            case 4:
                if lista_saboresdisponiveis:
                    imprimir_sabores(lista_saboresdisponiveis)
                else:
                    print('Nenhum sabor disponivel no momento')
                codigo = input('\ndigite o codigo do sabor escolhido:').strip()
                sabor_escolhido = buscar_por_codigo
                if sabor_escolhido:
                    carrinho.append(sabor_escolhido)
                    print(f'\n{sabor_escolhido} adicionado ao carrinho')
                else:
                    print(f'\nCódigo {codigo} não encontrado')

            case 5:
                if not carrinho:
                    print('\n carrinho vazio')
                else:
                  while True: #loop, permite retirar varios itens do carrinho
                      print('\nItens no carrinho:')
                      for i, item in enumerate(carrinho, 1):
                          print(f'{i}. {item['nome'].capitalize()} - R$ {item['preço']:.2f}')

                      total = sum(item['preço'] for item in carrinho)
                      print(f'\ntotal a pagar: R$ {total:.2f}')

                      print('\n O que deseja fazer?')
                      print('1- Voltar ao menu principal:')
                      print('2- Remover um item')

                      escolha = input('Digite 1 ou 2:').strip()
                      if escolha == '1':
                          break #volta ao primeiro menu
                      elif escolha == '2':
                          try:
                              num = int(input('digite o numero do item que deseja remover:'))
                              if 1 <= num <= len(carrinho):
                                  removido = carrinho.pop(num - 1)
                                  print(f'\n {removidp['nome'].capitalize()} removido com sucesso')
                              else:
                                  print('Numero inválido')
                          except ValueError:
                              print('\n por favor digite um numero valido')
                      else:
                          print('opção invalida')
                          break
                      
            case 6:
                nome = input('digite o nome do sabor:').strip().lower()
                if not nome:
                    print('nome inválido')
                    break
                if nome in lista_saboresindisponiveis:
                    preço = lista_saboresindisponiveis[nome]
                    del lista_saboresindisponiveis[nome]
                    lista_saboresdisponiveis[nome] = preço
                    print(f'sabor {nome.capitalize()} removido da lista de disponiveis')
                    print(f'codigo: {codigo} e preço: R$ {preço:.2f}')
                else:
                    print(f'Sabor {nome} não encontrado na lista de indisponiveis')

            case 7:
                nome = input('digite o nome do sabor:').strip().lower()
                if not nome:
                    print('nome inválido')
                    break
                if nome in lista_saboresdisponiveis:
                    preço = lista_saboresdisponiveis[nome]
                    del lista_saboresdisponiveis[nome]
                    lista_saboresindisponiveis[nome] = preço
                    print(f'sabor {nome.capitalize()} removido da lista de indisponiveis')
                    print(f'codigo: {codigo} e preço: R$ {preço:.2f}')
                else:
                    print(f'Sabor {nome} não encontrado na lista de disponiveis')
#----------------------------------------------------------------------------------------------
            case 8:
                if lista_sabores:
                    imprimir_sabores(lista_sabores)
                else:
                    print('Nenhum sabor cadastrado no momento')


            

                    

                    

                    

                