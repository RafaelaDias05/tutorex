import dados_teste
from view.UsuarioView import UsuarioView
from view.FuncionarioView import FuncionarioView
from view.AlunoView import AlunoView
from view.QuestaoView import QuestaoView
from view.AtividadeView import AtividadeView

def menu_admin():
    funcionario_view = FuncionarioView()
    usuario_view = UsuarioView()
    questao_view = QuestaoView()
    atividade_view = AtividadeView()

    while True:
        print("\n===== MENU ADMIN =====")
        print("1 - Gerenciar Alunos")
        print("2 - Cadastrar Questão")
        print("3 - Montar Atividade")
        print("4 - Cadastrar Funcionário e Usuário")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_alunos()
        elif opcao == "2":
            questao_view.cadastrar_questao()
        elif opcao == "3":
            atividade_id = atividade_view.montar_atividade()
            if atividade_id:
                questao_view.buscar_questao()
                atividade_view.selecionar_questoes(atividade_id)
        elif opcao == "4":
            funcionario_id = funcionario_view.cadastrar_funcionario()
            if funcionario_id:
                usuario_view.cadastrar_usuario(funcionario_id)
        elif opcao == "5":
            print("Saindo do menu admin...")
            break
        else:
            print("Opção inválida!")

def menu_alunos():
    view = AlunoView()
    while True:
        print("\n===== Gerenciar Alunos =====")
        print("1 - Cadastrar Aluno")
        print("2 - Exibir Aluno")
        print("3 - Editar Aluno")
        print("4 - Excluir Aluno")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            view.cadastrar_aluno()
        elif opcao == "2":
            view.buscar_alunos()
        elif opcao == "3":
            view.editar_aluno()
        elif opcao == "4":
            view.deletar_aluno()
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_professor():
    questao_view = QuestaoView()
    atividade_view = AtividadeView()
    while True:
        print("\n===== MENU PROFESSOR =====")
        print("1 - Gerenciar Alunos")
        print("2 - Cadastrar Questão")
        print("3 - Montar Atividade")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_alunos()
        elif opcao == "2":
            questao_view.cadastrar_questao()
        elif opcao == "3":
            atividade_id = atividade_view.montar_atividade()
            if atividade_id:
                questao_view.buscar_questao()
                atividade_view.selecionar_questoes(atividade_id)
        elif opcao == "4":
            print("Saindo do menu professor...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    dados_teste.inserir_dados_iniciais()
    while True:
        usuario_view = UsuarioView()
        print("Bem-vindo ao TUTOREX - Tutoria de Excelência!")
        print("Aperte Ctrl + C para sair")
        resultado = usuario_view.autenticar_usuario()
        if resultado["sucesso"]:
            acesso = resultado["acesso"]
            if acesso == "admin":
                menu_admin()
            else:
                menu_professor()
        else:
            print(resultado["mensagem"])
        