from model.Questao import Questao
from controller.StrategiesQuestao import *

class QuestaoController:
    def cadastrar_questao(self, assunto, palavras_chaves, materia, enunciado, alternativas, gabarito):
        questao = Questao(assunto, palavras_chaves, materia, enunciado, alternativas, gabarito)
        try:
            id_gerado = questao.inserir(questao)
            return {"sucesso": True, "mensagem": f"Questão cadastrada com sucesso! ID: {id_gerado}"}
        except Exception as e:
            return {"sucesso": False, "mensagem": f"Erro ao cadastrar questão: {str(e)}"}

    def buscar_questoes(self, filtro, valor):
        strategy = {
            "assunto": BuscaPorAssunto(),
            "materia": BuscaPorMateria(),
            "palavra-chave": BuscaPorPalavraChave()
        }.get(filtro.lower())
        
        if not strategy:
            return {"sucesso": False, "mensagem": "Filtro de busca inválido."}
        
        resultados = strategy.buscar(valor)
        return {"sucesso": True, "resultados": resultados}
