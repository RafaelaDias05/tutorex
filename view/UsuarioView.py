from controller.UsuarioController import UsuarioController

class UsuarioView:
    def __init__(self):
        self.controller = UsuarioController()

    def cadastrar_usuario(self, funcionario_id):
        print("\n-- Cadastro de Usuário --")
        login = input("Login: ")
        senha = input("Senha: ")
        acesso = input("Nível de acesso (admin/professor): ")

        resultado = self.controller.cadastrar_usuario(login, senha, acesso, funcionario_id)
        print(resultado["mensagem"])

    def autenticar_usuario(self):
        login = input("Login: ")
        senha = input("Senha: ")
        resultado = self.controller.autenticar_usuario(login, senha)
        return resultado
            
