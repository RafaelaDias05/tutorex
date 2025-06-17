

from controllers.auth_controller import autenticar_usuario, cadastrar_usuario, buscar_usuario_por_login 
from model.usuario import Usuario 

def menu_autenticacao():
    while True:
        print("\n=== Menu de Autenticação ===")
        print("1. Fazer Login")
        print("2. Cadastrar Novo Usuário")
        print("3. Esqueci Minha Senha") 
        print("0. Sair do Sistema")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            usuario_autenticado = fazer_login_view()
            if usuario_autenticado:
                return usuario_autenticado 
        elif opcao == "2":
            cadastrar_usuario_view()
        elif opcao == "3":
            recuperar_senha_view() 
        elif opcao == "0":
            print("Saindo do sistema. Até logo!")
            return None 
        else:
            print("Opção inválida! Tente novamente.")

def fazer_login_view():
    print("\n--- Fazer Login ---")
    login = input("Login: ")
    senha = input("Senha: ")

    usuario = autenticar_usuario(login, senha) 

    if usuario:
        print("Login realizado com sucesso.")
    else:
        print("Dados inválidos. Tente novamente!")
    
    return usuario

def cadastrar_usuario_view():
    print("\n--- Cadastrar Novo Usuário ---")
    login = input("Login para o novo usuário: ")
    senha = input("Senha para o novo usuário: ")

    novo_usuario = Usuario(login=login, senha=senha)
    usuario_cadastrado = cadastrar_usuario(novo_usuario)

    if usuario_cadastrado:
        print(f"Usuário '{login}' cadastrado com sucesso!")
    else:
        print("Falha ao cadastrar usuário. Verifique os dados e tente novamente.")

def recuperar_senha_view():
    print("\n--- Recuperar Senha ---")
    login_para_recuperar = input("Digite seu login para recuperação de senha: ")

    usuario_existente = buscar_usuario_por_login(login_para_recuperar)

    if usuario_existente:
        print(f"Um link para redefinição foi enviado para o e-mail associado a '{login_para_recuperar}'.")
    else:
        print("Login não encontrado ou campo vazio. Verifique e tente novamente.")
    