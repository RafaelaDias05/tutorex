from model.questao import Questao
from controllers.questao_controller import cadastrar_questao, buscar_questoes

def menu_cadastro_questao():
    print("\n=== Cadastro de Questão ===")
    assunto = input("Assunto: ")
    palavras_chaves = input("Palavras-chave (separadas por vírgula): ")
    materia = input("Matéria: ")
    enunciado = input("Enunciado: ")
    alternativas = input("Alternativas (separadas por |, deixe vazio se não houver): ") or None
    gabarito = input("Gabarito: ")

    questao = Questao(
        assunto=assunto,
        palavras_chaves=palavras_chaves,
        materia=materia,
        enunciado=enunciado,
        alternativas=alternativas,
        gabarito=gabarito
    )

    cadastrar_questao(questao)
    print("Questão cadastrada com sucesso!")


def menu_busca_questoes():
    print("\n=== Buscar Questões ===")
    assunto = input("Filtrar por assunto (ou deixe em branco): ") or None
    materia = input("Filtrar por matéria (ou deixe em branco): ") or None
    palavra = input("Filtrar por palavra-chave (ou deixe em branco): ") or None

    questoes = buscar_questoes(assunto, materia, palavra)

    if not questoes:
        print("Nenhuma questão encontrada.")
    else:
        for q in questoes:
            print(f"\nID: {q.id}")
            print(f"Assunto: {q.assunto}")
            print(f"Matéria: {q.materia}")
            print(f"Palavras-chave: {q.palavras_chaves}")
            print(f"Enunciado: {q.enunciado}")
            print(f"Alternativas: {q.alternativas}")
            print(f"Gabarito: {q.gabarito}")

def menu_questoes():
    while True:
        print("\n Menu de Questões")
        print("1. Cadastrar Questão")
        print("2. Buscar Questões")
        print("0. Voltar ao menu principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_cadastro_questao()
        elif opcao == "2":
            menu_busca_questoes()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")
