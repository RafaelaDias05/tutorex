from controller.AlunoController import AlunoController
from controller.StrategiesAluno import BuscaPorVencimento, BuscaPorNome, BuscaPorCPF, BuscaPorSerie

class AlunoViewMock:
    def __init__(self, io):
        self.controller = AlunoController()
        self.io = io

    def cadastrar_aluno(self):
        self.io.print("Cadastro de Aluno")
        nome = self.io.input("Nome: ")
        cpf = self.io.input("CPF: ")
        colegio = self.io.input("Colégio: ")
        serie = self.io.input("Série: ")
        endereco = self.io.input("Endereço: ")
        email = self.io.input("Email: ")
        responsavel1 = self.io.input("Responsável 1: ")
        data_matricula = self.io.input("Data da matrícula (YYYY-MM-DD): ")
        vencimento = self.io.input("Dia de vencimento da mensalidade: ")
        
        
        dados_aluno = {
            "nome": nome,
            "cpf": cpf,
            "colegio": colegio,
            "serie": serie,
            "endereco": endereco,
            "email": email,
            "responsavel_aluno": responsavel1,
            "data_matricula": data_matricula,
            "vencimento_mensalidade": int(vencimento)
        }

        id = self.controller.cadastrar_aluno(dados_aluno)

        self.io.print("Aluno cadastrado com ID:", id)
        return id

    def buscar_aluno(self):
        self.io.print("Buscar aluno por:")
        self.io.print("1 - Nome")
        self.io.print("2 - CPF")
        self.io.print("3 - Série")
        self.io.print("4 - Vencimento")
        opcao = self.io.input("Escolha a opção de busca: ")

        estrategia = None
        termo = ""

        if opcao == "1":
            termo = self.io.input("Digite o nome: ")
            estrategia = "nome"
        elif opcao == "2":
            termo = self.io.input("Digite o CPF: ")
            estrategia = "cpf"
        elif opcao == "3":
            termo = self.io.input("Digite a série: ")
            estrategia = "serie"
        elif opcao == "4":
            termo = self.io.input("Digite o vencimento: ")
            estrategia = "vencimento"
        else:
            self.io.print("Opção inválida.")
            return

        resultados = self.controller.buscar_alunos(estrategia, termo)

        if resultados:
            self.io.print("Alunos encontrados:")
            for aluno in resultados:
                self.io.print(aluno)
        else:
            self.io.print("Nenhum aluno encontrado.")
