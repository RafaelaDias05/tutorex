from controller.UsuarioController import UsuarioController

class UsuarioViewMock:
    def __init__(self, io):
        self.controller = UsuarioController()
        self.io = io

    def autenticar_usuario(self):
        self.io.print("Autenticação de usuário")
        login = self.io.input("Login: ")
        senha = self.io.input("Senha: ")
        usuario = self.controller.autenticar_usuario(login, senha)
        if usuario:
            return usuario
        return {"sucesso": False, "mensagem": "Usuário ou senha inválidos"}

    def cadastrar_usuario(self, funcionario_id):
        self.io.print("Cadastro de usuário para funcionário ID:", funcionario_id)
        login = self.io.input("Login do novo usuário: ")
        senha = self.io.input("Senha: ")
        tipo = self.io.input("Tipo (admin/professor): ")
        self.controller.cadastrar_usuario(login, senha, tipo, funcionario_id)
