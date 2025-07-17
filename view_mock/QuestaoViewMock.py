from controller.QuestaoController import QuestaoController

class QuestaoViewMock:
    def __init__(self, io):
        self.controller = QuestaoController()
        self.io = io

    def cadastrar_questao(self):
        self.io.print("\n-- Cadastro de Questão --")
        assunto = self.io.input("Assunto: ")
        palavras_chaves = self.io.input("Palavras-chave (separadas por vírgula): ")
        materia = self.io.input("Matéria: ")
        enunciado = self.io.input("Enunciado: ")
        alternativas = self.io.input("Alternativas (deixe vazio se não houver): ")
        gabarito = self.io.input("Gabarito: ")

        resultado = self.controller.cadastrar_questao(assunto, palavras_chaves, materia, enunciado, alternativas, gabarito)
        self.io.print(resultado["mensagem"])

    def buscar_questao(self):
        self.io.print("\n-- Busca de Questões --")
        filtro = self.io.input("Filtro (assunto, materia, palavra-chave): ")
        valor = self.io.input("Valor para busca: ")

        resultado = self.controller.buscar_questoes(filtro, valor)
        if resultado["sucesso"]:
            self.io.print("Questões encontradas:")
            for q in resultado["resultados"]:
               self.io.print(f"ID: {q[0]}, Assunto: {q[1]}, Matéria: {q[3]}, Enunciado: {q[4][:30]}...")
        else:
           self.io.print("Erro na busca:", resultado["mensagem"])
