from model.Questao import Questao

class BuscaPorAssunto:
    def buscar(self, assunto):
        questao = Questao()
        sql = "SELECT * FROM questoes WHERE assunto LIKE ?"
        questao.cursor.execute(sql, (f"%{assunto}%",))
        return questao.cursor.fetchall()

class BuscaPorMateria:
    def buscar(self, materia):
        questao = Questao()
        sql = "SELECT * FROM questoes WHERE materia LIKE ?"
        questao.cursor.execute(sql, (f"%{materia}%",))
        return questao.cursor.fetchall()

class BuscaPorPalavraChave:
    def buscar(self, palavra_chave):
        questao = Questao()
        sql = "SELECT * FROM questoes WHERE palavras_chaves LIKE ?"
        questao.cursor.execute(sql, (f"%{palavra_chave}%",))
        return questao.cursor.fetchall()
