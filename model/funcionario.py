
class Funcionario:
    def __init__(self, id=None, nome="", endereco="", telefone="", email="", login="", senha=""):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.login = login
        self.senha = senha

    def __repr__(self):
        return f"Funcionario(id={self.id}, nome='{self.nome}', login='{self.login}')"

    def __str__(self):
        return (f"ID: {self.id}\n"
                f"Nome: {self.nome}\n"
                f"Endereço: {self.endereco}\n"
                f"Telefone: {self.telefone}\n"
                f"Email: {self.email}\n"
                f"Login: {self.login}\n"
                f"Senha: {self.senha}")