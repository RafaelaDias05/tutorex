class Questao:
    def __init__(self, id=None, assunto="", palavras_chaves="", materia="", enunciado="", alternativas=None, gabarito=""):
        self.id = id
        self.assunto = assunto
        self.palavras_chaves = palavras_chaves  
        self.materia = materia
        self.enunciado = enunciado
        self.alternativas = alternativas  
        self.gabarito = gabarito
