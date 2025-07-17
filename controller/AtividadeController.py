from model.Atividade import Atividade
from controller.QuestaoController import QuestaoController

class AtividadeController:
    def __init__(self):
        self.questao_controller = QuestaoController()
    
    def criar_atividade(self):
        atividade = Atividade()
        atividade_id = atividade.inserir(atividade)
        return atividade_id
    
    def adicionar_questoes_na_atividade(self, atividade_id, questoes_ids):
        atividade = Atividade()
        for q_id in questoes_ids:
            atividade.inserir_atividade_questao(atividade_id, q_id)