from model.Aluno import Aluno

class BuscaStrategy:
    def buscar(self, termo):
        raise NotImplementedError()

class BuscaPorNome(BuscaStrategy):
    def buscar(self, nome):
        conexao = Aluno().conexao
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM alunos WHERE nome LIKE ?", (f"%{nome}%",))
        return cursor.fetchall()

class BuscaPorCPF(BuscaStrategy):
    def buscar(self, cpf):
        conexao = Aluno().conexao
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM alunos WHERE cpf = ?", (cpf,))
        return cursor.fetchall()

class BuscaPorSerie(BuscaStrategy):
    def buscar(self, serie):
        conexao = Aluno().conexao
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM alunos WHERE serie = ?", (serie,))
        return cursor.fetchall()

class BuscaPorVencimento(BuscaStrategy):
    def buscar(self, dia_vencimento):
        conexao = Aluno().conexao
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM alunos WHERE vencimento_mensalidade = ?", (dia_vencimento,))
        return cursor.fetchall()
