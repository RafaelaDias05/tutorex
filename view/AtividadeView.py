from controller.AtividadeController import AtividadeController

class AtividadeView:
    def __init__(self):
        self.controller = AtividadeController()
        
    def montar_atividade(self):
        print("\n-- Montagem de Atividade --")
        atividade_id = self.controller.criar_atividade()
        return atividade_id
    
    def selecionar_questoes(self, atividade_id):
        ids_str = input("Digite os IDs das questões que deseja adicionar à atividade, separados por vírgula: ")
        try:
            ids_selecionados = [int(id.strip()) for id in ids_str.split(",") if id.strip().isdigit()]
        except:
            print("Entrada inválida.")
            return ""
        self.controller.adicionar_questoes_na_atividade(atividade_id, ids_selecionados)
        print(f"Questões adicionadas à atividade {atividade_id}.")
        print("Montagem da atividade finalizada.")
        