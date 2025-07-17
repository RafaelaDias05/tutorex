from controller.AlunoController import AlunoController

class AlunoView:
    def __init__(self):
        self.controller = AlunoController()

    def cadastrar_aluno(self):
        print("\n-- Cadastro de Aluno --")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        colegio = input("Colégio: ")
        serie = input("Série: ")
        endereco = input("Endereço: ")
        email = input("E-mail: ")
        responsavel_aluno = input("Nome do responsável: ")
        segundo_responsavel_aluno = input("Nome do segundo responsável (opcional): ")
        data_matricula = input("Data de matrícula (AAAA-MM-DD): ")
        vencimento_mensalidade = input("Dia de vencimento da mensalidade (1 a 31): ")
        telefone = input("Telefone para contato: ")

        dados_aluno = {
            "nome": nome,
            "cpf": cpf,
            "colegio": colegio,
            "serie": serie,
            "endereco": endereco,
            "email": email,
            "responsavel_aluno": responsavel_aluno,
            "segundo_responsavel_aluno": segundo_responsavel_aluno if segundo_responsavel_aluno else None,
            "data_matricula": data_matricula,
            "vencimento_mensalidade": int(vencimento_mensalidade)
        }

        resultado = self.controller.cadastrar_aluno(dados_aluno)
        print(resultado["mensagem"])

        if resultado["sucesso"]:
            telefone_res = self.controller.cadastrar_telefone(resultado["id"], telefone)
            print(telefone_res["mensagem"])
            
            from controller.AlunoController import AlunoController

    def buscar_alunos(self):
        print("\n-- Busca de Aluno --")
        print("Filtros disponíveis: nome, cpf, serie, vencimento")
        filtro = input("Escolha um filtro: ").strip().lower()
        valor = input("Digite o valor para busca: ").strip()
        resultados = self.controller.buscar_alunos(filtro, valor)
        if resultados:
            print("\nAlunos encontrados:")
            for r in resultados:
                print(r)
            return resultados
        else:
            print("Nenhum aluno encontrado com esse filtro e valor.")
            return []

    def escolher_aluno(self, alunos):
        if not alunos:
            print("Nenhum aluno para escolher.")
            return None
        print("\nDigite o ID do aluno que deseja selecionar:")
        ids = [str(aluno[0]) for aluno in alunos]  
        while True:
            aluno_id = input("ID: ").strip()
            if aluno_id in ids:
                return aluno_id
            print("ID inválido, tente novamente.")

    def editar_aluno(self):
        alunos = self.buscar_alunos()
        if not alunos:
            return
        aluno_id = self.escolher_aluno(alunos)
        if not aluno_id:
            return
        print("Informe os dados que deseja atualizar (deixe vazio para pular):")
        campos = [
            "nome", "cpf", "colegio", "serie", "endereco", "email",
            "responsavel_aluno", "segundo_responsavel_aluno", "data_matricula", "vencimento_mensalidade"
        ]
        dados_atualizados = {}
        for campo in campos:
            valor = input(f"{campo}: ").strip()
            if valor:
                if campo == "vencimento_mensalidade":
                    valor = int(valor)
                dados_atualizados[campo] = valor
        if dados_atualizados:
            resultado = self.controller.editar_aluno(aluno_id, dados_atualizados)
            print(resultado["mensagem"])
        else:
            print("Nenhum dado foi informado para atualização.")

    def deletar_aluno(self):
        alunos = self.buscar_alunos()
        if not alunos:
            return
        aluno_id = self.escolher_aluno(alunos)
        if not aluno_id:
            return
        confirm = input("Tem certeza que deseja deletar este aluno? (s/n): ").lower()
        if confirm == 's':
            resultado = self.controller.deletar_aluno(aluno_id)
            print(resultado["mensagem"])
        else:
            print("Operação cancelada.")

