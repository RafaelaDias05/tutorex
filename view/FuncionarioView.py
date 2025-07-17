from controller.FuncionarioController import FuncionarioController

class FuncionarioView:
    def __init__(self):
        self.controller = FuncionarioController()

    def cadastrar_funcionario(self):
        print("\n-- Cadastro de Funcionário --")
        nome = input("Nome: ")
        endereco = input("Endereço: ")
        email = input("E-mail: ")

        resultado = self.controller.cadastrar_funcionario(nome, endereco, email)
        if resultado["sucesso"]:
            return resultado["id"]
        else:
            return False

