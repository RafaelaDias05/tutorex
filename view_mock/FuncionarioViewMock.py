from controller.FuncionarioController import FuncionarioController

class FuncionarioViewMock:
    def __init__(self, io):
        self.controller = FuncionarioController()
        self.io = io

    def cadastrar_funcionario(self):
        self.io.print("Cadastro de funcionário")
        nome = self.io.input("Nome: ")
        matricula = self.io.input("Matrícula: ")
        cpf = self.io.input("CPF: ")
        id = self.controller.cadastrar_funcionario(nome, matricula, cpf)
        self.io.print("Funcionário cadastrado com ID:", id)
        return id
