
from controllers.funcionario_controller import (
    cadastrar_funcionario,
)

from model.funcionario import Funcionario 

def menu_funcionarios():
    while True:
        print("\n=== Gerenciar Funcionários ===")
        print("1. Cadastrar Novo Funcionário")
        print("0. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_funcionario_view()
        elif opcao == "0":
            print("Voltando ao Menu Principal...")
            break
        else:
            print("Opção inválida! Tente novamente.")

def cadastrar_funcionario_view():
    print("\n--- Cadastrar Novo Funcionário ---")
    nome = input("Nome: ")
    endereco = input("Endereço: ")
    telefone = input("Telefone (ex: 11987654321): ")
    email = input("Email: ")
    login = input("Login: ")
    senha = input("Senha: ") 

    novo_funcionario = Funcionario(
        nome=nome,
        endereco=endereco,
        telefone=telefone,
        email=email,
        login=login,
        senha=senha
    )

    funcionario_id = cadastrar_funcionario(novo_funcionario)

    if funcionario_id:
        print(f"Funcionário '{nome}' cadastrado com sucesso! ID: {funcionario_id}")
    else:
        print("Falha ao cadastrar funcionário. Verifique os dados e tente novamente.")