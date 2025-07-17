from model.Modelo import Modelo

class Funcionario(Modelo):
    def __init__(self, nome=None, endereco=None, email=None):
        super().__init__()
        self.nome = nome
        self.endereco = endereco
        self.email = email
    
    def get_nome_tabela(self):
        return "funcionarios"
    
    def get_colunas_valores(self, _):
        colunas = ["nome", "endereco", "email"]
        valores = [self.nome, self.endereco, self.email]
        return colunas, valores