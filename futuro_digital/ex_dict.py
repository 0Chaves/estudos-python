def verificar_cpfExiste(cpf: str) -> bool:
 return cpf in pessoas

dados_pessoa = dict[str, str, int] #cpf da pessoa, nome e idade
pessoas: dados_pessoa = {} #dicionário vazio para armazenar as pessoas e seus dados
opcao = 0 #guarda a opção escolhida pelo usuário

while (opcao != 7):
    print("\nEscolha uma das opções abaixo:")
    print("""
    1 - Cadastrar nova pessoa (nome, idade e cpf) 
    2 - Pesquisar se uma pessoa já está cadastrada (pelo cpf)
    3 - Listar os dados de uma pessoa (pelo cpf)
    4 - Remover uma pessoa do cadastro (pelo cpf)
    5 - Listar todo o cadastro de pessoas
    6 - Verificar quantidade de registros
    7 - Sair """)
    opcao = int(input("Digite a opção desejada:"))
    if opcao == 7:
        print("Encerrando o programa. Até mais!")
        exit()
    if opcao <1 or opcao > 7:
        print("Opção inválida. Digite um número entre 1 e 7.")
        continue
    else:
        match opcao:
            case 1:
                cpf = input("Digite o cpf da pessoa:")
                nome = input("Digite o nome da pessoa:")
                idade = int(input("Digite a idade da pessoa:"))
                pessoas[cpf] = (nome, idade)
            case 2:
                cpf = input("Digite o cpf da pessoa:")
                existe = verificar_cpfExiste(cpf)
                if existe:
                    print(f"Pessoa encontrada")
                else:
                    print("Pessoa não encontrada.")
            case 3:
                cpf = input("Digite o cpf da pessoa:")
                existe = verificar_cpfExiste(cpf)
                if existe:
                    print(f"Dados da pessoa: {pessoas[cpf]}")
                else:
                    print("Pessoa não encontrada.")
            case 4:
                cpf = input("Digite o cpf da pessoa:")
                existe = verificar_cpfExiste(cpf)
                if existe:
                    del pessoas[cpf]
                    print("Pessoa removida do cadastro.")
                else:
                    print("Pessoa não encontrada.")
            case 5:
                print("Cadastro de pessoas:")
                for key, value in pessoas.items():
                    nome = value[0]
                    idade = value[1]
                    print(f"\nCpf: {key} Nome: {nome} Idade:{idade}")
            case 6:
                print(f"Quantidade de registros: {len(pessoas)}")