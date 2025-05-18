from controllers.questao_controller import buscar_questoes
from controllers.atividade_controller import criar_atividade

def montar_atividade():
    print("\n=== Montar Atividade ===")
    assunto = input("Filtrar por assunto (ou deixe em branco): ") or None
    materia = input("Filtrar por matéria (ou deixe em branco): ") or None
    palavra = input("Filtrar por palavra-chave (ou deixe em branco): ") or None

    questoes = buscar_questoes(assunto, materia, palavra)

    if not questoes:
        print("Nenhuma questão encontrada.")
        return

    print("\n=== Questões Encontradas ===")
    for q in questoes:
        print(f"\nID: {q.id}")
        print(f"Assunto: {q.assunto}")
        print(f"Matéria: {q.materia}")
        print(f"Enunciado: {q.enunciado}")
        print(f"Gabarito: {q.gabarito}")

    ids_input = input("\nDigite os IDs das questões que deseja incluir (separados por vírgula): ")
    try:
        questoes_ids = [int(i.strip()) for i in ids_input.split(",") if i.strip().isdigit()]
    except ValueError:
        print("Entrada inválida.")
        return

    if not questoes_ids:
        print("Nenhuma questão selecionada.")
        return

    titulo = input("Título da atividade: ")
    atividade_id = criar_atividade(titulo, questoes_ids)
    print(f"Atividade criada com sucesso! ID: {atividade_id}")
