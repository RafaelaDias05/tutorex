
from database.conect_database import conectar
from model.funcionario import Funcionario 

def cadastrar_funcionario(funcionario: Funcionario):
    conn = conectar()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO funcionarios (nome, endereco, telefone, email, login, senha) VALUES (?, ?, ?, ?, ?, ?) """, (funcionario.nome, funcionario.endereco, funcionario.telefone, funcionario.email, funcionario.login, funcionario.senha))

        funcionario_id = cursor.lastrowid

        conn.commit()
        funcionario.id = funcionario_id 
        return funcionario_id

    except Exception as e:
        conn.rollback()
        print(f"Erro ao cadastrar funcionário: {e}")
        return None
    finally:
        conn.close()