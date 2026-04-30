usuario_dict = dict[str, str, bool]

usuarios: usuario_dict = {} 

def inserir_usuario(nome, senha, ativo):
    if nome not in usuarios.keys():
        usuarios[nome] = (senha, ativo)
    else:
        raise ValueError(f"{nome} ja existe no dicionario")
    
def validar_usuario(nome, senha):
    if nome not in usuarios.keys():
        raise KeyError(f"{nome} não existe no dicionario")
    if usuarios[nome][0] != senha:
        raise PermissionError("Senha incorreta")

if __name__ == "__main__":

    try:
        inserir_usuario("admin", "admin", True)
        inserir_usuario("joao123", "123", False)
        inserir_usuario("maria_dev", "mariazinha", True)
        inserir_usuario("maria_dev", "mariazinha", True)
    except ValueError as e:
        print(e)

    nome = input("Digite o nome de usuario\n")
    senha = input("Digite a senha\n")

    try:
        validar_usuario(nome, senha)
    except Exception as e:
        print(e)