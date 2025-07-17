from controller.AtividadeController import AtividadeController

class AtividadeViewMock:
    def __init__(self, io):
        self.controller = AtividadeController()
        self.io = io
        
    def montar_atividade(self):
        self.io.print("\n-- Montagem de Atividade --")
        atividade_id = self.controller.criar_atividade()
        return atividade_id
    
    def selecionar_questoes(self, atividade_id):
        ids_str = self.io.input("Digite os IDs das questões que deseja adicionar à atividade, separados por vírgula: ")
        try:
            ids_selecionados = [int(id.strip()) for id in ids_str.split(",") if id.strip().isdigit()]
        except:
            self.io.print("Entrada inválida.")
            return ""
        self.controller.adicionar_questoes_na_atividade(atividade_id, ids_selecionados)
        self.io.print(f"Questões adicionadas à atividade {atividade_id}.")
        self.io.print("Montagem da atividade finalizada.")
        