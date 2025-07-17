from model.Modelo import Modelo

class Aluno(Modelo):
    def __init__(self, nome=None, cpf=None, colegio=None, serie=None, endereco=None,
                 email=None, responsavel_aluno=None, segundo_responsavel_aluno=None,
                 data_matricula=None, vencimento_mensalidade=None):
        super().__init__()
        self.nome = nome
        self.cpf = cpf
        self.colegio = colegio
        self.serie = serie
        self.endereco = endereco
        self.email = email
        self.responsavel_aluno = responsavel_aluno
        self.segundo_responsavel_aluno = segundo_responsavel_aluno
        self.data_matricula = data_matricula
        self.vencimento_mensalidade = vencimento_mensalidade
    
    def get_nome_tabela(self):
        return "alunos"
    
    def get_colunas_valores(self, _):
        colunas = [
            "nome", "cpf", "colegio", "serie", "endereco", "email",
            "responsavel_aluno", "segundo_responsavel_aluno", "data_matricula", "vencimento_mensalidade"
        ]
        valores = [
            self.nome, self.cpf, self.colegio, self.serie, self.endereco, self.email,
            self.responsavel_aluno, self.segundo_responsavel_aluno, self.data_matricula, self.vencimento_mensalidade
        ]
        return colunas, valores
