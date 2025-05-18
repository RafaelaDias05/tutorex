from controllers.questao_controller import cadastrar_questao, buscar_questoes
from controllers.atividade_controller import criar_atividade
from controllers.auth_controller import cadastrar_usuario
from controllers.aluno_controller import cadastrar_aluno
from controllers.funcionario_controller import cadastrar_funcionario
from model.questao import Questao
from model.aluno import Aluno
from model.funcionario import Funcionario
from model.usuario import Usuario

from datetime import datetime

def inserir_dados():
    print("\n🔧 Inserindo dados...")

    # --- USUÁRIOS ---
    usuarios = [
    Usuario(login="carlos", senha="senha123"),     
    Usuario(login="fernanda", senha="senha456"),   
    Usuario(login="joao", senha="senha789")        
    ]
    for user in usuarios:
        cadastrar_usuario(user)
        print(" 3 usuários criados (carlos, fernanda, joao).")


    # --- FUNCIONÁRIOS ---
    funcionarios = [
        Funcionario("Carlos Silva", "Rua A, 123", "11999999999", "carlos@escola.com", "carlos", "senha123"),
        Funcionario("Fernanda Lima", "Rua C, 789", "11888888888", "fernanda@escola.com", "fernanda", "senha456"),
        Funcionario("João Pedro", "Rua D, 101", "11777777777", "joao@escola.com", "joao", "senha789")
    ]
    for f in funcionarios:
        cadastrar_funcionario(f)
    print("3 funcionários criados.")

    # --- ALUNOS ---
    alunos = [
        {
            "dados": Aluno("Maria Souza", "12345678900", "Colégio Alpha", "8º Ano", "Rua B, 456", "maria@gmail.com", "João Souza", "Ana Souza", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "10"),
            "telefones": ["11988887777", "11977776666"]
        },
        {
            "dados": Aluno("Pedro Oliveira", "23456789011", "Colégio Beta", "7º Ano", "Rua E, 789", "pedro@gmail.com", "Carlos Oliveira", "Juliana Oliveira", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "15"),
            "telefones": ["11966665555"]
        },
        {
            "dados": Aluno("Ana Clara", "34567890122", "Colégio Gama", "9º Ano", "Rua F, 321", "ana@gmail.com", "Eduardo Silva", "Luciana Silva", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "5"),
            "telefones": ["11944443333", "11933332222"]
        },
        {
            "dados": Aluno("Lucas Martins", "45678901233", "Colégio Delta", "6º Ano", "Rua G, 654", "lucas@gmail.com", "Marcos Martins", "Paula Martins", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "20"),
            "telefones": ["11922221111"]
        },
        {
            "dados": Aluno("Beatriz Rocha", "56789012344", "Colégio Zeta", "5º Ano", "Rua H, 987", "beatriz@gmail.com", "Ricardo Rocha", "Sofia Rocha", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "25"),
            "telefones": ["11911110000", "11900009999"]
        }
    ]
    for a in alunos:
        cadastrar_aluno(a["dados"], a["telefones"])
    print("5 alunos cadastrados com telefones.")

    # --- QUESTÕES ---
    questoes_ = [
        Questao("Matemática", "fração,divisão", "Matemática", "Qual é o resultado de 1/2 + 1/4?", "A) 1/2 | B) 3/4 | C) 2/4", "B"),
        Questao("Português", "verbo,conjugação", "Português", "Qual é o verbo da frase: 'Ele corre todos os dias'?", "A) Ele | B) corre | C) dias", "B"),
        Questao("História", "brasil,colonial", "História", "Em que ano o Brasil foi descoberto?", "A) 1500 | B) 1600 | C) 1700", "A"),
    ]
    for questao in questoes_:
        cadastrar_questao(questao)
    print("3 questões cadastradas.")

    # --- ATIVIDADE ---
    todas_questoes = buscar_questoes()
    ids = [q.id for q in todas_questoes]
    if ids:
        criar_atividade("Atividade  - Revisão Geral", ids)
        print("1 atividade criada com todas as questões.")
    else:
        print("Nenhuma questão para criar atividade.")
