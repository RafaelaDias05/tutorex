from database.conect_database import conectar
from model.questao import Questao

def cadastrar_questao(questao: Questao):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO questoes (assunto, palavras_chaves, materia, enunciado, alternativas, gabarito)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        questao.assunto, questao.palavras_chaves, questao.materia,
        questao.enunciado, questao.alternativas, questao.gabarito
    ))

    conn.commit()
    conn.close()


def buscar_questoes(assunto=None, materia=None, palavra_chave=None):
    conn = conectar()
    cursor = conn.cursor()

    query = "SELECT * FROM questoes WHERE 1=1"
    params = []

    if assunto:
        query += " AND assunto LIKE ?"
        params.append(f"%{assunto}%")
    if materia:
        query += " AND materia LIKE ?"
        params.append(f"%{materia}%")
    if palavra_chave:
        query += " AND palavras_chaves LIKE ?"
        params.append(f"%{palavra_chave}%")

    cursor.execute(query, params)
    resultados = cursor.fetchall()
    conn.close()

    questoes = []
    for q in resultados:
        questoes.append(Questao(*q))
    return questoes
