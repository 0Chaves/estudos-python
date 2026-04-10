from funcionario import Funcionario

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]


if __name__ == "__main__":
    func = Funcionario("Eu", "email", 5.5)
    func2 = Funcionario("Eu", "email", 4.4)

    # mes=int(input(f"""Escolha o mês trabalhado:
    # 1. {meses[0]}
    # 2. {meses[1]}
    # 3. {meses[2]}
    # 4. {meses[3]}
    # 5. {meses[4]}
    # 6. {meses[5]}
    # 7. {meses[6]}
    # 8. {meses[7]}
    # 9. {meses[8]}
    # 10. {meses[9]}
    # 11. {meses[10]}
    # 12. {meses[11]}\n
    # """))
    # horas = int(input("Horas trabalhadas: "))
    # func.cadastrar_horas()




    func.email = "outro email novo"
    print(func.getEmail())
    print(func.getNome())
    # func.setNome("Novo nome")
    print(func.getNome())
    print(func.__eq__(func2))
