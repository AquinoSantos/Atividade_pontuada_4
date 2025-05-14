import os

os.system("cls || clear")  

class Funcionario:  # Classe funcionário
    def exibir_dados(self):  # Exibir dados do funcionário
        print("\n--- Dados do Funcionário ---")
        print(f"CPF: {self.cpf}")
        print(f"Nome: {self.nome}")
        print(f"Cargo: {self.cargo}")
        print(f"Salário: R$ {self.salario}")


def cadastrar_funcionario(funcionarios):  # Cadastrar funcionário
    cpf = input("Digite o CPF do funcionário: ")
    for funcionario in funcionarios:
        if funcionario.cpf == cpf:
            print("Funcionário com esse CPF já existe.")
            return funcionarios

    nome = input("Nome: ")
    cargo = input("Cargo: ")
    salario = input("Salário: ")

    funcionario = Funcionario()
    funcionario.cpf = cpf
    funcionario.nome = nome
    funcionario.cargo = cargo
    funcionario.salario = salario

    funcionarios.append(funcionario)
    print("Funcionário cadastrado com sucesso!")
    return funcionarios


def listar_funcionarios(funcionarios):  # Listar funcionários
    if funcionarios:
        for funcionario in funcionarios:
            funcionario.exibir_dados()
    else:
        print("Nenhum funcionário cadastrado.")


def atualizar_funcionario(funcionarios):  # Atualizar funcionário
    cpf = input("Digite o CPF do funcionário que deseja atualizar: ")
    for funcionario in funcionarios:
        if funcionario.cpf == cpf:
            funcionario.nome = input(f"Novo nome ({funcionario.nome}): ") or funcionario.nome
            funcionario.cargo = input(f"Novo cargo ({funcionario.cargo}): ") or funcionario.cargo
            funcionario.salario = input(f"Novo salário ({funcionario.salario}): ") or funcionario.salario
            print("Dados do funcionário atualizados com sucesso!")
            return funcionarios
    print("Funcionário não encontrado.")
    return funcionarios


def excluir_funcionario(funcionarios):  # Excluir funcionário
    cpf = input("Digite o CPF do funcionário que deseja excluir: ")
    for funcionario in funcionarios:
        if funcionario.cpf == cpf:
            funcionarios.remove(funcionario)
            print("Funcionário excluído.")
            return funcionarios
    print("Funcionário não encontrado.")
    return funcionarios


def carregar_dados():  # Carregar dados do arquivo
    nome_arquivo = "funcionarios.csv"
    funcionarios = []
    try:
        with open(nome_arquivo, "r") as arquivo:
            linhas = arquivo.readlines()
            for i in range(0, len(linhas), 4):  # Lê 4 linhas por funcionário
                cpf = linhas[i].strip().replace("Cpf:", "")
                nome = linhas[i + 1].strip().replace("Nome:", "")
                cargo = linhas[i + 2].strip().replace("Cargo:", "")
                salario = linhas[i + 3].strip().replace("Salário:", "")

                funcionario = Funcionario()
                funcionario.cpf = cpf
                funcionario.nome = nome
                funcionario.cargo = cargo
                funcionario.salario = salario

                funcionarios.append(funcionario)

        print("Dados carregados com sucesso.")
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    return funcionarios


def salvar_dados(funcionarios):  # Salvar dados no arquivo
    nome_arquivo = "funcionarios.csv"
    with open(nome_arquivo, "w") as arquivo:
        for func in funcionarios:
            arquivo.write(f"Cpf:{func.cpf}\nNome:{func.nome}\nCargo:{func.cargo}\nSalário:{func.salario}\n")
    print("Dados salvos com sucesso.")


def menu():  # Menu principal
    funcionarios = []
    while True:
        print("\nDENDÊ TECH:")
        print("1 - Cadastrar Funcionário")
        print("2 - Listar Funcionários")
        print("3 - Atualizar Funcionário")
        print("4 - Excluir Funcionário")
        print("5 - Carregar Dados do Arquivo")
        print("6 - Salvar Dados no Arquivo")
        print("7 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            funcionarios = cadastrar_funcionario(funcionarios)
        elif opcao == "2":
            listar_funcionarios(funcionarios)
        elif opcao == "3":
            funcionarios = atualizar_funcionario(funcionarios)
        elif opcao == "4":
            funcionarios = excluir_funcionario(funcionarios)
        elif opcao == "5":
            funcionarios = carregar_dados()
        elif opcao == "6":
            salvar_dados(funcionarios)
        elif opcao == "7":
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Inicia o programa
menu()
