from controller.QuestaoController import QuestaoController

class QuestaoView:
    def __init__(self):
        self.controller = QuestaoController()

    def cadastrar_questao(self):
        print("\n-- Cadastro de Questão --")
        assunto = input("Assunto: ")
        palavras_chaves = input("Palavras-chave (separadas por vírgula): ")
        materia = input("Matéria: ")
        enunciado = input("Enunciado: ")
        alternativas = input("Alternativas (deixe vazio se não houver): ")
        gabarito = input("Gabarito: ")

        resultado = self.controller.cadastrar_questao(assunto, palavras_chaves, materia, enunciado, alternativas, gabarito)
        print(resultado["mensagem"])

    def buscar_questao(self):
        print("\n-- Busca de Questões --")
        filtro = input("Filtro (assunto, materia, palavra-chave): ")
        valor = input("Valor para busca: ")

        resultado = self.controller.buscar_questoes(filtro, valor)
        if resultado["sucesso"]:
            print("Questões encontradas:")
            for q in resultado["resultados"]:
                print(f"ID: {q[0]}, Assunto: {q[1]}, Matéria: {q[3]}, Enunciado: {q[4][:30]}...")
        else:
            print("Erro na busca:", resultado["mensagem"])
