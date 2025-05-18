from database.conect_database import conectar
from model.atividade import Atividade

def criar_atividade(titulo, questoes_ids):
    conn = conectar()
    cursor = conn.cursor()

    #insere uma nova atividade
    cursor.execute("""
        INSERT INTO atividades (titulo, data_criacao)
        VALUES (?, datetime('now'))
    """, (titulo,))
    atividade_id = cursor.lastrowid

    #insere as questões da atividade na tabela atividade_questao
    for qid in questoes_ids:
        cursor.execute("""
            INSERT INTO atividade_questao (atividade_id, questao_id)
            VALUES (?, ?)
        """, (atividade_id, qid))

    conn.commit()
    conn.close()
    return atividade_id
