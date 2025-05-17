-- Tabela de alunos
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(255) NOT NULL,
    cpf VARCHAR(13) NOT NULL UNIQUE,
    colegio VARCHAR(255) NOT NULL,
    serie VARCHAR(255) NOT NULL,
    endereco TEXT NOT NULL,
    email VARCHAR(255) NOT NULL,
    responsavel_aluno VARCHAR(255) NOT NULL,
    segundo_responsavel_aluno VARCHAR(255) NULL,
    data_matricula DATETIME NOT NULL,
    vencimento_mensalidade DATETIME NOT NULL
);

--Tabela que cadastra telefones dos alunos
CREATE TABLE IF NOT EXISTS aluno_telefone (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    aluno_id INTEGER NOT NULL,
    telefone VARCHAR(14) NOT NULL,
    FOREIGN KEY (aluno_id) REFERENCES alunos(id)
);

-- Tabela de funcionários
CREATE TABLE IF NOT EXISTS funcionarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(255) NOT NULL,
    endereco TEXT NOT NULL,
    telefone VARCHAR(14) NOT NULL,
    email VARCHAR(255) NOT NULL,
    login VARCHAR(255) NOT NULL UNIQUE,
    senha TEXT NOT NULL
);

-- Tabela de usuários (para login/autenticação)
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    login TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL
);

-- Tabela de questões
CREATE TABLE IF NOT EXISTS questoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    assunto VARCHAR(255) NOT NULL,
    palavras_chaves TEXT NOT NULL,
    materia VARCHAR(255) NOT NULL,
    enunciado TEXT NOT NULL,
    alternativas TEXT,  
    gabarito TEXT NOT NULL
);

-- Tabela de atividades
CREATE TABLE IF NOT EXISTS atividades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo VARCHAR(255) NOT NULL,
    data_criacao DATETIME NOT NULL
);

-- Tabela de ligação atividade-questao (atividade pode ter várias questões)
CREATE TABLE IF NOT EXISTS atividade_questao (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    atividade_id INTEGER NOT NULL,
    questao_id INTEGER NOT NULL,
    FOREIGN KEY (atividade_id) REFERENCES atividades(id),
    FOREIGN KEY (questao_id) REFERENCES questoes(id)
);