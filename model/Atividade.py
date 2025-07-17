from model.Modelo import Modelo
from datetime import datetime

class Atividade(Modelo):
    def __init__(self, data_criacao=None):
        super().__init__()
        self.data_criacao = data_criacao or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def get_nome_tabela(self):
        return "atividades"
    
    def get_colunas_valores(self, _):
        return ["data_criacao"], [self.data_criacao]

    def inserir_atividade_questao(self, atividade_id, questao_id):
        sql = "INSERT INTO atividade_questao (atividade_id, questao_id) VALUES (?, ?)"
        self.cursor.execute(sql, (atividade_id, questao_id))
        self.conexao.commit()
