from model.Modelo import Modelo

class Usuario(Modelo):
    def __init__(self, login=None, senha=None, acesso=None, funcionario_id=None):
        super().__init__()
        self.login = login
        self.senha = senha
        self.acesso = acesso
        self.funcionario_id = funcionario_id
    
    def get_nome_tabela(self):
        return "usuarios"
    
    def get_colunas_valores(self, _):
        colunas = ["login", "senha", "acesso", "funcionario_id"]
        valores = [self.login, self.senha, self.acesso, self.funcionario_id]
        return colunas, valores
    
    def autenticar(self, login, senha):
        query = "SELECT acesso FROM usuarios WHERE login = ? AND senha = ?"
        self.cursor.execute(query, (login, senha))
        resultado = self.cursor.fetchone()
        if resultado:
            acesso = resultado[0]  
            return True, acesso
        return False, None
