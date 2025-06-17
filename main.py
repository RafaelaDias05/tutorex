from view.questao_view import menu_questoes
from view.atividade_view import montar_atividade
from view.aluno_view import menu_alunos
from view.funcionario_view import menu_funcionarios
from view.auth_view import menu_autenticacao

from database.conect_database import criar_tabelas
from database.insert_data import inserir_dados

def menu_principal():
    while True:
        print("\n📚 MENU PRINCIPAL - TUTOREX")
        print("1. Gerenciar Alunos")
        print("2. Gerenciar Questões")
        print("3. Gerenciar Atividades")
        print("4. Gerenciar Funcionários")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_alunos()
        elif opcao == "2":
            menu_questoes()
        elif opcao == "3":
            montar_atividade()
        elif opcao == "4":
            menu_funcionarios()
        elif opcao == "0":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida!")

def main():
    criar_tabelas()
    inserir_dados()

    print("🔐 Bem-vindo ao TUTOREX!")
    
    usuario_autenticado = None
    while usuario_autenticado is None: 
        usuario_autenticado = menu_autenticacao() 

        if usuario_autenticado:
            print(f"\nLogin realizado com sucesso. Bem-vindo, {usuario_autenticado.login}!")
            menu_principal() 
            break 
        elif usuario_autenticado is None: 
            print("Acesso finalizado.")
            break 

if __name__ == "__main__":
    main()
