from model.Modelo import Modelo

class Questao(Modelo):
    def __init__(self, assunto=None, palavras_chaves=None, materia=None, enunciado=None, alternativas=None, gabarito=None):
        super().__init__()
        self.assunto = assunto
        self.palavras_chaves = palavras_chaves  
        self.materia = materia
        self.enunciado = enunciado
        self.alternativas = alternativas  
        self.gabarito = gabarito
    
    def get_nome_tabela(self):
        return "questoes"
    
    def get_colunas_valores(self, _):
        colunas = ["assunto", "palavras_chaves", "materia", "enunciado", "alternativas", "gabarito"]
        valores = [self.assunto, self.palavras_chaves, self.materia, self.enunciado, self.alternativas, self.gabarito]
        return colunas, valores
