from database.conect_database import conectar
from model.usuario import Usuario

def cadastrar_usuario(usuario: Usuario):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO usuarios (login, senha) VALUES (?, ?)", (usuario.login, usuario.senha))
        usuario.id = cursor.lastrowid
        conn.commit()
        print(f"Usuário '{usuario.login}' cadastrado com sucesso!")
        return usuario
    except Exception as e:
        conn.rollback()
        print(f"Erro ao cadastrar usuário: {e}")
        if "UNIQUE constraint failed: usuarios.login" in str(e):
             print("Erro: O login informado já está em uso. Escolha outro.")
        return None
    finally:
        conn.close()

def autenticar_usuario(login, senha):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id, login, senha FROM usuarios WHERE login = ?", (login,))
        row = cursor.fetchone()
        if row:
            usuario = Usuario(*row)
            
            if senha == usuario.senha: 
                return usuario 
            else:
                print("Senha incorreta. Dados inválidos. Tente novamente!")
                return None
        else:
            print("Login não encontrado. Dados inválidos. Tente novamente!")
            return None
    except Exception as e:
        print(f"Erro durante a autenticação: {e}")
        return None
    finally:
        conn.close()

def buscar_usuario_por_login(login):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id, login, senha FROM usuarios WHERE login = ?", (login,))
        row = cursor.fetchone()
        if row:
            return Usuario(*row)
        return None
    except Exception as e:
        print(f"Erro ao buscar usuário por login: {e}")
        return None
    finally:
        conn.close()