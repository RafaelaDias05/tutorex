
from datetime import datetime

class Aluno:
    def __init__(self, id=None, nome="", cpf="", colegio="", serie="",
                 endereco="", email="", responsavel_aluno="",
                 segundo_responsavel_aluno=None, data_matricula=None,
                 vencimento_mensalidade=None, telefones=None):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.colegio = colegio
        self.serie = serie
        self.endereco = endereco
        self.email = email
        self.responsavel_aluno = responsavel_aluno
        self.segundo_responsavel_aluno = segundo_responsavel_aluno 
        self.data_matricula = data_matricula or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.vencimento_mensalidade = vencimento_mensalidade or datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
        self.telefones = telefones if telefones is not None else [] 

    def __repr__(self):
        return f"Aluno(id={self.id}, nome='{self.nome}', cpf='{self.cpf}')"

    def __str__(self):
        telefones_str = ", ".join(self.telefones) if self.telefones else "Nenhum"
        
        vencimento_formatado = "N/A"
        try:
            if self.vencimento_mensalidade:
                # Converte para datetime para extrair o dia, caso não seja já um objeto datetime
                dt_obj = datetime.strptime(str(self.vencimento_mensalidade), "%Y-%m-%d %H:%M:%S")
                vencimento_formatado = dt_obj.strftime("%d") 
        except (ValueError, TypeError):
            pass 

        return f"ID: {self.id}\nNome: {self.nome}\nCPF: {self.cpf}\nColégio: {self.colegio}\nSérie: {self.serie}\n" \
               f"Endereço: {self.endereco}\nEmail: {self.email}\n" \
               f"Responsável 1: {self.responsavel_aluno}\nResponsável 2: {self.segundo_responsavel_aluno or 'N/A'}\n" \
               f"Data de Matrícula: {self.data_matricula}\n" \
                f"Vencimento Mensalidade (Dia): {vencimento_formatado}\n" \
               f"Telefones: {telefones_str}"
