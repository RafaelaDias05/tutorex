import sqlite3

class ConexaoSQLite:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(ConexaoSQLite, cls).__new__(cls)
            cls._instancia._inicializar()
        return cls._instancia

    def _inicializar(self):
        self.conexao = sqlite3.connect("tutorex.db")
        self.cursor = self.conexao.cursor()
        self.criar_tabelas()

    def criar_tabelas(self):
        comandos_sql = [
            """
            CREATE TABLE IF NOT EXISTS alunos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(255) NOT NULL,
                cpf VARCHAR(13) NOT NULL UNIQUE,
                colegio VARCHAR(255) NOT NULL,
                serie VARCHAR(255) NOT NULL,
                endereco TEXT NOT NULL,
                email VARCHAR(255) NOT NULL UNIQUE,
                responsavel_aluno VARCHAR(255) NOT NULL,
                segundo_responsavel_aluno VARCHAR(255) NULL,
                data_matricula DATETIME NOT NULL,
                vencimento_mensalidade INTEGER NOT NULL
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS aluno_telefone (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                aluno_id INTEGER NOT NULL,
                telefone VARCHAR(14) NOT NULL UNIQUE,
                FOREIGN KEY (aluno_id) REFERENCES alunos(id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS funcionarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(255) NOT NULL,
                endereco TEXT NOT NULL,
                email VARCHAR(255) NOT NULL UNIQUE
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                funcionario_id INTEGER NOT NULL,
                login TEXT NOT NULL UNIQUE,
                senha TEXT NOT NULL,
                acesso VARCHAR(255),
                FOREIGN KEY (funcionario_id) REFERENCES funcionarios(id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS questoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                assunto VARCHAR(255) NOT NULL,
                palavras_chaves TEXT NOT NULL,
                materia VARCHAR(255) NOT NULL,
                enunciado TEXT NOT NULL,
                alternativas TEXT,
                gabarito TEXT NOT NULL
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS atividades (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data_criacao DATETIME NOT NULL
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS atividade_questao (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                atividade_id INTEGER NOT NULL,
                questao_id INTEGER NOT NULL,
                FOREIGN KEY (atividade_id) REFERENCES atividades(id),
                FOREIGN KEY (questao_id) REFERENCES questoes(id)
            )
            """
        ]

        for sql in comandos_sql:
            self.cursor.execute(sql)
        self.conexao.commit()
        
    def get_conexao(self):
        return self.conexao

    def get_cursor(self):
        return self.cursor
