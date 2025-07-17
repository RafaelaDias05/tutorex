from model.conect_database import ConexaoSQLite

def inserir_dados_iniciais():
    conexao = ConexaoSQLite().get_conexao()
    cursor = ConexaoSQLite().get_cursor()

    funcionarios = [
        ("Admin Exemplo", "Rua dos Administradores, 123", "admin@tutorex.com"),
        ("Professor Exemplo", "Rua dos Professores, 456", "prof@tutorex.com")
    ]

    usuarios = [
        ("admin_user", "1234", "admin"),      
        ("prof_user", "1234", "professor")
    ]

    questoes = [
        {
            "assunto": "Padrões de Projeto",
            "palavras_chaves": "padrões de projeto, design patterns, programação orientada a objetos",
            "materia": "Programação",
            "enunciado": "O que são padrões de projeto em desenvolvimento de software?",
            "alternativas": "A) Estratégias fixas de codificação; B) Técnicas de deploy; C) Soluções reutilizáveis para problemas recorrentes; D) Frameworks para UI",
            "gabarito": "C"
        },
        {
            "assunto": "Padrões de Projeto",
            "palavras_chaves": "padrões de projeto, design patterns, singleton",
            "materia": "Programação",
            "enunciado": "Qual padrão de projeto é responsável por garantir que uma classe tenha apenas uma instância?",
            "alternativas": "A) Observer; B) Factory; C) Singleton; D) Strategy",
            "gabarito": "C"
        },
        {
            "assunto": "Padrões de Projeto",
            "palavras_chaves": "padrões de projeto, strategy, algoritmos",
            "materia": "Programação",
            "enunciado": "O padrão Strategy é útil quando:",
            "alternativas": "A) Queremos observar mudanças de estado; B) Precisamos de uma interface única para criação de objetos; C) Desejamos encapsular algoritmos intercambiáveis; D) Precisamos de uma única instância global",
            "gabarito": "C"
        }
    ]

    try:
        for q in questoes:
            cursor.execute("""
                INSERT INTO questoes (assunto, palavras_chaves, materia, enunciado, alternativas, gabarito)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                q["assunto"],
                q["palavras_chaves"],
                q["materia"],
                q["enunciado"],
                q["alternativas"],
                q["gabarito"]
            ))
        conexao.commit()
        print("Questões inseridas com sucesso!")
    except Exception as e:
        print(f"Erro ao inserir questões: {e}")
        conexao.rollback()

    try:
        for func in funcionarios:
            cursor.execute("INSERT INTO funcionarios (nome, endereco, email) VALUES (?, ?, ?)", func)
        conexao.commit()

        cursor.execute("SELECT id FROM funcionarios WHERE email = ?", (funcionarios[0][2],))
        admin_id = cursor.fetchone()[0]
        cursor.execute("SELECT id FROM funcionarios WHERE email = ?", (funcionarios[1][2],))
        prof_id = cursor.fetchone()[0]

        cursor.execute("INSERT INTO usuarios (funcionario_id, login, senha, acesso) VALUES (?, ?, ?, ?)", (admin_id, *usuarios[0]))
        cursor.execute("INSERT INTO usuarios (funcionario_id, login, senha, acesso) VALUES (?, ?, ?, ?)", (prof_id, *usuarios[1]))
        conexao.commit()

        print("Usuários e questões inseridos com sucesso!")

    except Exception as e:
        print(f"Erro ao inserir dados: {e}")
        conexao.rollback()

if __name__ == "__main__":
    inserir_dados_iniciais()
