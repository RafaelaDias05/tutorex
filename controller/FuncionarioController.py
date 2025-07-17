from model.Funcionario import Funcionario

class FuncionarioController:
    def cadastrar_funcionario(self, nome, endereco, email):
        if self.email_existe(email):
            return {
                "sucesso": False,
                "mensagem": "Email já cadastrado!",
                "id": None
            }
        
        funcionario = Funcionario(nome, endereco, email)
        try:
            id_gerado = funcionario.inserir(funcionario)
            return {
                "sucesso": True,
                "mensagem": "Funcionário cadastrado com sucesso.",
                "id": id_gerado
            }
        except Exception as e:
            return {
                "sucesso": False,
                "mensagem": f"Erro ao cadastrar funcionário: {str(e)}",
                "id": None
            }
    
    def email_existe(self, email):
        conexao = Funcionario().conexao
        cursor = conexao.cursor()
        cursor.execute("SELECT 1 FROM funcionarios WHERE email = ?", (email,))
        return cursor.fetchone() is not None
