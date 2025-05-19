from view.questao_view import menu_questoes
from view.atividade_view import montar_atividade
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
            #menu_alunos()
            print("Ops! Sem implementação ainda")
        elif opcao == "2":
            menu_questoes()
        elif opcao == "3":
            montar_atividade()
        elif opcao == "4":
            #menu_porfessor()
            print("Ops! Sem implementação ainda")
        elif opcao == "0":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida!")

def main():
    criar_tabelas()
    inserir_dados()

    print("🔐 Bem-vindo ao TUTOREX!")
    '''
    #usuario = login_usuario()

    if usuario:
        print(f"\n Login realizado com sucesso. Bem-vindo, {usuario.login}!")
        menu_principal()
    else:
        print("Acesso negado. Finalizando o programa.")
    '''

if __name__ == "__main__":
    main()
