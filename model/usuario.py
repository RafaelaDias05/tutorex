class Usuario:
    def __init__(self, id=None, login="", senha=""):
        self.id = id
        self.login = login
        self.senha = senha 
 
    def __repr__(self):
        return f"Usuario(id={self.id}, login='{self.login}')"

    def __str__(self):
        return f"ID: {self.id}\nLogin: {self.login}\nSenha: {self.senha}"
