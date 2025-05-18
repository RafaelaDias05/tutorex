from datetime import datetime

class Atividade:
    def __init__(self, id=None, titulo="", data_criacao=None):
        self.id = id
        self.titulo = titulo
        self.data_criacao = data_criacao or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
