from model.Aluno import Aluno
from controller.StrategiesAluno import *

class AlunoController:
    def cadastrar_aluno(self, dados_aluno):
        if self.cpf_existe(dados_aluno["cpf"]):
            return {"sucesso": False, "mensagem": "CPF já cadastrado!", "id": None}
        if self.email_existe(dados_aluno["email"]):
            return {"sucesso": False, "mensagem": "Email já cadastrado!", "id": None}
        aluno = Aluno(**dados_aluno)
        try:
            id_gerado = aluno.inserir(aluno)
            return {"sucesso": True, "mensagem": "Aluno cadastrado com sucesso!", "id": id_gerado}
        except Exception as e:
            return {"sucesso": False, "mensagem": f"Erro ao cadastrar aluno: {str(e)}", "id": None}

    def cadastrar_telefone(self, aluno_id, telefone):
        aluno = Aluno()
        try:
            aluno.cursor.execute("SELECT 1 FROM aluno_telefone WHERE telefone = ?", (telefone,))
            if aluno.cursor.fetchone():
                return {"sucesso": False, "mensagem": "Telefone já cadastrado para outro aluno."}
            aluno.cursor.execute(
                "INSERT INTO aluno_telefone (aluno_id, telefone) VALUES (?, ?)",
                (aluno_id, telefone)
            )
            aluno.conexao.commit()
            return {"sucesso": True, "mensagem": "Telefone cadastrado com sucesso."}
        except Exception as e:
            return {"sucesso": False, "mensagem": f"Erro ao cadastrar telefone: {str(e)}"}

    def cpf_existe(self, cpf):
        conexao = Aluno().conexao
        cursor = conexao.cursor()
        cursor.execute("SELECT 1 FROM alunos WHERE cpf = ?", (cpf,))
        return cursor.fetchone() is not None

    def email_existe(self, email):
        conexao = Aluno().conexao
        cursor = conexao.cursor()
        cursor.execute("SELECT 1 FROM alunos WHERE email = ?", (email,))
        return cursor.fetchone() is not None
    
    def buscar_alunos(self, filtro, valor):
        strategies = {
            "nome": BuscaPorNome(),
            "cpf": BuscaPorCPF(),
            "serie": BuscaPorSerie(),
            "vencimento": BuscaPorVencimento()
        }
        strategy = strategies.get(filtro)
        if not strategy:
            return []
        return strategy.buscar(valor)
    
    def editar_aluno(self, aluno_id, dados_atualizados):
        aluno = Aluno()
        try:
            colunas = []
            valores = []
            for chave, valor in dados_atualizados.items():
                colunas.append(f"{chave} = ?")
                valores.append(valor)
            valores.append(aluno_id)
            sql = f"UPDATE alunos SET {', '.join(colunas)} WHERE id = ?"
            aluno.cursor.execute(sql, valores)
            aluno.conexao.commit()
            return {"sucesso": True, "mensagem": "Aluno atualizado com sucesso."}
        except Exception as e:
            return {"sucesso": False, "mensagem": f"Erro ao atualizar aluno: {str(e)}"}
    
    def deletar_aluno(self, aluno_id):
        aluno = Aluno()
        try:
            aluno.cursor.execute("DELETE FROM aluno_telefone WHERE aluno_id = ?", (aluno_id,))
            aluno.cursor.execute("DELETE FROM alunos WHERE id = ?", (aluno_id,))
            aluno.conexao.commit()
            return {"sucesso": True, "mensagem": "Aluno deletado com sucesso."}
        except Exception as e:
            return {"sucesso": False, "mensagem": f"Erro ao deletar aluno: {str(e)}"}
