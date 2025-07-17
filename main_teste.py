from MockIO import MockIO
import dados_teste
from view_mock.UsuarioViewMock import UsuarioViewMock
from view_mock.FuncionarioViewMock import FuncionarioViewMock
from view_mock.AlunoViewMock import AlunoViewMock
from view_mock.QuestaoViewMock import QuestaoViewMock
from view_mock.AtividadeViewMock import AtividadeViewMock

def menu_admin(io):
    funcionario_view = FuncionarioViewMock(io)
    usuario_view = UsuarioViewMock(io)

    while True:
        io.print("\n===== MENU ADMIN =====")
        io.print("1 - Gerenciar Alunos")
        io.print("2 - Cadastrar Questão")
        io.print("3 - Montar Atividade")
        io.print("4 - Cadastrar Funcionário e Usuário")
        io.print("5 - Sair")

        opcao = io.input("Escolha uma opção: ")
        if opcao == "4":
            funcionario_id = funcionario_view.cadastrar_funcionario()
            if funcionario_id:
                usuario_view.cadastrar_usuario(funcionario_id)
        elif opcao == "5":
            io.print("Saindo do menu admin...")
            break

def menu_alunos():
    view = AlunoViewMock(io)
    while True:
        io.print("\n===== Gerenciar Alunos =====")
        io.print("1 - Cadastrar Aluno")
        io.print("2 - Exibir Aluno")
        io.print("3 - Editar Aluno")
        io.print("4 - Excluir Aluno")
        io.print("5 - Sair")

        opcao = io.input("Escolha uma opção: ")

        if opcao == "1":
            view.cadastrar_aluno()
        elif opcao == "2":
            view.buscar_aluno()
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_professor(io):
    questao_view = QuestaoViewMock(io)
    atividade_view = AtividadeViewMock(io)
    while True:
        io.print("\n===== MENU PROFESSOR =====")
        io.print("1 - Gerenciar Alunos")
        io.print("2 - Cadastrar Questão")
        io.print("3 - Montar Atividade")
        io.print("4 - Sair")

        opcao = io.input("Escolha uma opção: ")
        if opcao == "4":
            io.print("Saindo do menu professor...")
            break
        elif opcao == "1":
            menu_alunos()
        elif opcao == "2":
            questao_view.cadastrar_questao()
        elif opcao == "3":
            atividade_id = atividade_view.montar_atividade()
            if atividade_id:
                questao_view.buscar_questao()
                atividade_view.selecionar_questoes(atividade_id)
            
if __name__ == "__main__":
    dados_teste.inserir_dados_iniciais()
    entradas = """admin_user
1234
4
Joana Silva
MAT789
99999999999
prof_joana
1234
professor
5
prof_user
1234
1
1
Maria Silva     
12345678901     
Colégio do Saber
9º ano      
Rua das Flores 
maria@email.com   
João Silva
2025-07-17
10        
2
1
Maria Silva
5
2
Revolucao Francesa
Revolucao Francesa
Historia
Explique os principais fatores que levaram à Revolução Francesa
nenhuma
Resposta discursiva sobre causas sociais, políticas e econômicas.
3
assunto
Padrões de Projeto
1, 2, 3
4
"""
    io = MockIO(entradas)

    usuario_view = UsuarioViewMock(io)

    io.print("Bem-vindo ao TUTOREX - Tutoria de Excelência!")

    resultado = usuario_view.autenticar_usuario()
    if resultado["sucesso"]:
        if resultado["acesso"] == "admin":
            menu_admin(io)
        else:
            menu_professor(io)
    else:
        io.print(resultado["mensagem"])

    resultado = usuario_view.autenticar_usuario()
    if resultado["sucesso"]:
        if resultado["acesso"] == "admin":
            menu_admin(io)
        else:
            menu_professor(io)
    else:
        io.print(resultado["mensagem"])

    print("\n===== SAÍDA FINAL =====")
    print(io.get_output())
