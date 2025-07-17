from model.Usuario import Usuario

class UsuarioController:
    def cadastrar_usuario(self, login, senha, acesso, funcionario_id):
        if self.login_existe(login):
            return {
                "sucesso": False,
                "mensagem": "Login já cadastrado!"
            }
        usuario = Usuario(login, senha, acesso, funcionario_id)
        try:
            id_gerado = usuario.inserir(usuario)
            return {
                "sucesso": True,
                "mensagem": f"Usuário cadastrado com sucesso! ID: {id_gerado}"
            }
        except Exception as e:
            return {
                "sucesso": False,
                "mensagem": f"Erro ao cadastrar usuário: {str(e)}"
            }

    def autenticar_usuario(self, login, senha):
        usuario = Usuario()
        autenticado, acesso = usuario.autenticar(login, senha)
        if autenticado:
            return {
                "sucesso": True,
                "mensagem": f"Acesso autorizado: {acesso}",
                "acesso": acesso
            }
        else:
            return {
                "sucesso": False,
                "mensagem": "Login ou senha inválidos."
            }

    def login_existe(self, login):
        conexao = Usuario().conexao
        cursor = conexao.cursor()
        cursor.execute("SELECT 1 FROM usuarios WHERE login = ?", (login,))
        return cursor.fetchone() is not None
