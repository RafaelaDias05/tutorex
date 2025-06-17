
from controllers.aluno_controller import (
    validar_e_formatar_dia_vencimento,
    cadastrar_aluno,
    buscar_alunos,
    atualizar_aluno,
    deletar_aluno,
    selecionar_aluno_por_criterios
)
from model.aluno import Aluno
from datetime import datetime

def menu_alunos():
    while True:
        print("\n=== Gerenciar Alunos ===")
        print("1. Cadastrar Novo Aluno")
        print("2. Buscar Alunos")
        print("3. Atualizar Dados de Aluno")
        print("4. Deletar Aluno")
        print("5. Ver Detalhes de Aluno")
        print("0. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno_view()
        elif opcao == "2":
            buscar_alunos_view()
        elif opcao == "3":
            atualizar_aluno_view()
        elif opcao == "4":
            deletar_aluno_view() 
        elif opcao == "5":
            ver_detalhes_aluno_view() 
        elif opcao == "0":
            print("Voltando ao Menu Principal...")
            break
        else:
            print("Opção inválida! Tente novamente.")
 

def cadastrar_aluno_view():
    print("\n--- Cadastrar Novo Aluno ---")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    colegio = input("Colégio: ")
    serie = input("Série: ")
    endereco = input("Endereço: ")
    email = input("Email: ")
    responsavel_aluno = input("Nome do Responsável Principal: ")
    segundo_responsavel_aluno = input("Nome do Segundo Responsável (opcional, deixe em branco): ") or None
    data_matricula = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    vencimento_mensalidade = None
    while vencimento_mensalidade is None: 
        vencimento_dia_input = input("Dia de Vencimento da Mensalidade (DD, ex: 05 ou 20): ")
        vencimento_mensalidade = validar_e_formatar_dia_vencimento(vencimento_dia_input)
        if vencimento_mensalidade is None:
            print("Entrada inválida para o dia de vencimento. Por favor, digite um número entre 1 e 31.")

    novo_aluno = Aluno(
        nome=nome,
        cpf=cpf,
        colegio=colegio,
        serie=serie,
        endereco=endereco,
        email=email,
        responsavel_aluno=responsavel_aluno,
        segundo_responsavel_aluno=segundo_responsavel_aluno,
        data_matricula=data_matricula,
        vencimento_mensalidade=vencimento_mensalidade
    )

    telefones_input = input("Telefones (separados por vírgula, ex: 11987654321,11912345678): ")
    telefones = [t.strip() for t in telefones_input.split(',') if t.strip()]

    aluno_id = cadastrar_aluno(novo_aluno, telefones)

    if aluno_id:
        print(f"Aluno '{nome}' cadastrado com sucesso! ID: {aluno_id}")
    else:
        print("Falha ao cadastrar aluno. Verifique os dados e tente novamente.")


def buscar_alunos_view():
    print("\n--- Buscar Alunos ---")
    nome = input("Filtrar por Nome (ou deixe em branco): ") or None
    serie = input("Filtrar por Série (ou deixe em branco): ") or None
    vencimento_dia = input("Filtrar por Dia de Vencimento da Mensalidade (DD, ou deixe em branco): ") or None
    cpf = input("Filtrar por CPF (ou deixe em branco): ") or None

    alunos_encontrados = buscar_alunos(nome=nome, serie=serie, vencimento_mensalidade_dia=vencimento_dia, cpf=cpf)

    if alunos_encontrados:
        print("\n=== Alunos Encontrados ===")
        for aluno in alunos_encontrados:
            telefones_str = ", ".join(aluno.telefones) if aluno.telefones else "Nenhum"
            vencimento_data_formatada = datetime.strptime(aluno.vencimento_mensalidade, "%Y-%m-%d %H:%M:%S").strftime("%d")
            print(f"ID: {aluno.id} | Nome: {aluno.nome} | CPF: {aluno.cpf} | Série: {aluno.serie} | Vencimento Dia: {vencimento_data_formatada} | Telefones: {telefones_str}")
    else:
        print("Nenhum aluno encontrado com os filtros fornecidos.")
        
        
def atualizar_aluno_view():
    print("\n--- Atualizar Dados de Aluno ---")
    print("Primeiro, encontre o aluno que deseja atualizar.")

    nome_busca = input("Nome do aluno (para busca, ou deixe em branco): ") or None
    cpf_busca = input("CPF do aluno (para busca, ou deixe em branco): ") or None
    serie_busca = input("Série do aluno (para busca, ou deixe em branco): ") or None
    vencimento_dia_busca = input("Dia de vencimento (DD, para busca, ou deixe em branco): ") or None

    aluno_atual = selecionar_aluno_por_criterios(nome=nome_busca, cpf=cpf_busca, serie=serie_busca, vencimento_dia=vencimento_dia_busca)

    if not aluno_atual:
        return

    print(f"\nDados atuais do aluno (ID: {aluno_atual.id}, Nome: {aluno_atual.nome}):")
    print(aluno_atual)

    print("\nDigite os novos dados (deixe em branco para não alterar).")
    print("Para telefones, digite a lista completa para substituir os existentes.")

    dados_atualizacao = {}
    campos_principais = [
        'nome', 'cpf', 'colegio', 'serie', 'endereco', 'email', 'responsavel_aluno', 'segundo_responsavel_aluno'
    ]

    for campo in campos_principais:
        novo_valor = input(f"{campo.replace('_', ' ').title()} (atual: {getattr(aluno_atual, campo) or 'N/A'}): ")
        if novo_valor:
            dados_atualizacao[campo] = novo_valor

    vencimento_mensalidade_atualizado = None
    while vencimento_mensalidade_atualizado is None and (vencimento_dia_input := input(f"Novo Dia de Vencimento da Mensalidade (DD, atual: {datetime.strptime(aluno_atual.vencimento_mensalidade, '%Y-%m-%d %H:%M:%S').strftime('%d')}, ou deixe em branco para manter): ")) != ""):
        vencimento_mensalidade_atualizado = validar_e_formatar_dia_vencimento(vencimento_dia_input)
        if vencimento_mensalidade_atualizado is None:
            print("Entrada inválida para o dia de vencimento. Por favor, digite um número entre 1 e 31.")

    if vencimento_mensalidade_atualizado: 
        dados_atualizacao['vencimento_mensalidade'] = vencimento_mensalidade_atualizado


    telefones_input = input(f"Novos Telefones (atual: {', '.join(aluno_atual.telefones) or 'Nenhum'}, separados por vírgula, ou deixe em branco para manter os atuais): ")
    novos_telefones = None
    if telefones_input:
        novos_telefones = [t.strip() for t in telefones_input.split(',') if t.strip()]

    if atualizar_aluno(aluno_atual.id, dados_atualizacao, novos_telefones):
        print(f"Dados do aluno ID {aluno_atual.id} atualizados com sucesso!")
    else:
        print(f"Falha ao atualizar dados do aluno ID {aluno_atual.id}.")


def deletar_aluno_view():
    print("\n--- Deletar Aluno ---")
    print("Primeiro, encontre o aluno que deseja deletar.")

    nome_busca = input("Nome do aluno (para busca, ou deixe em branco): ") or None
    cpf_busca = input("CPF do aluno (para busca, ou deixe em branco): ") or None
    serie_busca = input("Série do aluno (para busca, ou deixe em branco): ") or None
    vencimento_dia_busca = input("Dia de vencimento (DD, para busca, ou deixe em branco): ") or None

    aluno_para_deletar = selecionar_aluno_por_criterios(nome=nome_busca, cpf=cpf_busca, serie=serie_busca, vencimento_dia=vencimento_dia_busca)

    if not aluno_para_deletar:
        return 

    print(f"\nDetalhes do aluno selecionado para deleção (ID: {aluno_para_deletar.id}, Nome: {aluno_para_deletar.nome}):")
    print(aluno_para_deletar)

    confirmacao = input(f"Tem certeza que deseja DELETAR o aluno '{aluno_para_deletar.nome}' (ID: {aluno_para_deletar.id}) e todos os seus telefones? (s/n): ").lower()
    if confirmacao == 's':
        if deletar_aluno(aluno_para_deletar.id):
            print(f"Aluno '{aluno_para_deletar.nome}' (ID: {aluno_para_deletar.id}) deletado com sucesso!")
        else:
            print(f"Falha ao deletar aluno '{aluno_para_deletar.nome}' (ID: {aluno_para_deletar.id}). Ele pode não existir.")
    else:
        print("Operação de deleção cancelada.")


def ver_detalhes_aluno_view():
    print("\n--- Ver Detalhes de Aluno ---")
    print("Primeiro, encontre o aluno para ver os detalhes.")

    nome_busca = input("Nome do aluno (para busca, ou deixe em branco): ") or None
    cpf_busca = input("CPF do aluno (para busca, ou deixe em branco): ") or None
    serie_busca = input("Série do aluno (para busca, ou deixe em branco): ") or None
    vencimento_dia_busca = input("Dia de vencimento (DD, para busca, ou deixe em branco): ") or None

    aluno_para_detalhes = selecionar_aluno_por_criterios(nome=nome_busca, cpf=cpf_busca, serie=serie_busca, vencimento_dia=vencimento_dia_busca)

    if not aluno_para_detalhes:
        return 

    print("\n=== Detalhes do Aluno ===")
    print(aluno_para_detalhes)