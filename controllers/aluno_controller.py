
from database.conect_database import conectar
from model.aluno import Aluno
from datetime import datetime 
import calendar

def cadastrar_aluno(aluno_obj: Aluno, telefones: list):
    conn = conectar()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO alunos (nome, cpf, colegio, serie, endereco, email, responsavel_aluno, segundo_responsavel_aluno, data_matricula, vencimento_mensalidade)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            aluno_obj.nome,
            aluno_obj.cpf,
            aluno_obj.colegio,
            aluno_obj.serie,
            aluno_obj.endereco,
            aluno_obj.email,
            aluno_obj.responsavel_aluno,
            aluno_obj.segundo_responsavel_aluno,
            aluno_obj.data_matricula,      
            aluno_obj.vencimento_mensalidade 
        ))

        aluno_id = cursor.lastrowid

        if telefones:
            for telefone in telefones:
                cursor.execute("""
                    INSERT INTO aluno_telefone (aluno_id, telefone)
                    VALUES (?, ?)
                """, (aluno_id, telefone))

        conn.commit()
        aluno_obj.id = aluno_id 
        return aluno_id

    except Exception as e:
        conn.rollback()
        print(f"Erro ao cadastrar aluno: {e}")
        return None
    finally:
        conn.close()

def _carregar_telefones_aluno(aluno_id):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT telefone FROM aluno_telefone WHERE aluno_id = ?", (aluno_id,))
        telefones = [row[0] for row in cursor.fetchall()]
        return telefones
    except Exception as e:
        print(f"Erro ao carregar telefones para o aluno {aluno_id}: {e}")
        return []
    finally:
        conn.close()
        

def buscar_alunos(nome=None, serie=None, vencimento_mensalidade_dia=None, cpf=None):
    conn = conectar()
    cursor = conn.cursor()

    query = "SELECT id, nome, cpf, colegio, serie, endereco, email, responsavel_aluno, segundo_responsavel_aluno, data_matricula, vencimento_mensalidade FROM alunos WHERE 1=1"
    params = []

    if nome:
        query += " AND nome LIKE ?"
        params.append(f"%{nome}%")
    if serie:
        query += " AND serie = ?"
        params.append(serie)
    if vencimento_mensalidade_dia:
        query += " AND STRFTIME('%d', vencimento_mensalidade) = ?"
        params.append(str(vencimento_mensalidade_dia).zfill(2))
    if cpf:
        query += " AND cpf = ?"
        params.append(cpf)

    try:
        cursor.execute(query, params)
        resultados = cursor.fetchall()

        alunos = []
        for row in resultados:
            aluno = Aluno(*row)
            aluno.telefones = _carregar_telefones_aluno(aluno.id)
            alunos.append(aluno)
        return alunos
    except Exception as e:
        print(f"Erro ao buscar alunos: {e}")
        return []
    finally:
        conn.close()
        
def validar_e_formatar_dia_vencimento(dia_input):
    try:
        dia = int(dia_input)
        if 1 <= dia <= 31:
            hoje = datetime.now()
            try:
                data_vencimento_completa = hoje.replace(day=dia, hour=23, minute=59, second=59)
            except ValueError:
                ultimo_dia_mes = calendar.monthrange(hoje.year, hoje.month)[1]
                data_vencimento_completa = hoje.replace(day=ultimo_dia_mes, hour=23, minute=59, second=59)
            return data_vencimento_completa.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return None 
    except ValueError:
        return None 

def selecionar_aluno_por_criterios(nome=None, cpf=None, serie=None, vencimento_dia=None):
    alunos_encontrados = buscar_alunos(nome=nome, cpf=cpf, serie=serie, vencimento_mensalidade_dia=vencimento_dia)

    if not alunos_encontrados:
        print("Nenhum aluno encontrado com os critérios fornecidos.")
        return None
    elif len(alunos_encontrados) > 1:
        print("\n--- Múltiplos Alunos Encontrados ---")
        for aluno in alunos_encontrados:
            vencimento_data_formatada = datetime.strptime(aluno.vencimento_mensalidade, "%Y-%m-%d %H:%M:%S").strftime("%d")
            print(f"ID: {aluno.id} | Nome: {aluno.nome} | CPF: {aluno.cpf} | Série: {aluno.serie} | Vencimento Dia: {vencimento_data_formatada}")

        while True:
            try:
                id_aluno_selecionado = int(input("Digite o ID do aluno que deseja selecionar: "))
                aluno_selecionado = next((a for a in alunos_encontrados if a.id == id_aluno_selecionado), None)
                if aluno_selecionado:
                    return aluno_selecionado
                else:
                    print("ID inválido ou não corresponde a nenhum aluno na lista. Tente novamente.")
            except ValueError:
                print("ID inválido. Digite um número.")
    else:
        return alunos_encontrados[0]

def atualizar_aluno(id_aluno, dados_atualizacao: dict, novos_telefones: list = None):
    conn = conectar()
    cursor = conn.cursor()
    try:
        set_clauses = []
        params_alunos = []

        for key, value in dados_atualizacao.items():
            if value is not None:
                set_clauses.append(f"{key} = ?")
                params_alunos.append(value)

        if set_clauses:
            query_alunos = "UPDATE alunos SET " + ", ".join(set_clauses) + " WHERE id = ?"
            params_alunos.append(id_aluno)
            cursor.execute(query_alunos, params_alunos)

        if novos_telefones is not None:
            cursor.execute("DELETE FROM aluno_telefone WHERE aluno_id = ?", (id_aluno,))
            for telefone in novos_telefones:
                cursor.execute("""
                    INSERT INTO aluno_telefone (aluno_id, telefone)
                    VALUES (?, ?)
                """, (id_aluno, telefone))

        conn.commit()
        return True
    except Exception as e:
        conn.rollback()
        print(f"Erro ao atualizar aluno ID {id_aluno}: {e}")
        return False
    finally:
        conn.close()

def deletar_aluno(id_aluno):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM aluno_telefone WHERE aluno_id = ?", (id_aluno,))

        cursor.execute("DELETE FROM alunos WHERE id = ?", (id_aluno,))
        conn.commit()
        return cursor.rowcount > 0 
    except Exception as e:
        conn.rollback()
        print(f"Erro ao deletar aluno ID {id_aluno}: {e}")
        return False
    finally:
        conn.close()

def ver_detalhes_aluno(id_aluno):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id, nome, cpf, colegio, serie, endereco, email, responsavel_aluno, segundo_responsavel_aluno, data_matricula, vencimento_mensalidade FROM alunos WHERE id = ?", (id_aluno,))
        row = cursor.fetchone()
        if row:
            aluno = Aluno(*row)
            aluno.telefones = _carregar_telefones_aluno(aluno.id)
            return aluno
        return None
    except Exception as e:
        print(f"Erro ao obter detalhes do aluno ID {id_aluno}: {e}")
        return None
    finally:
        conn.close()