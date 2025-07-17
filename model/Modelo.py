from abc import ABC, abstractmethod
from model.conect_database import ConexaoSQLite

class Modelo(ABC):
    def __init__(self):
        self.conexao = ConexaoSQLite().get_conexao()
        self.cursor = self.conexao.cursor()
    
    @abstractmethod
    def get_nome_tabela(self):
        pass
    
    @abstractmethod
    def get_colunas_valores(self, objeto):
        pass
    
    def inserir(self, objeto):
        tabela = self.get_nome_tabela()
        colunas, valores = self.get_colunas_valores(objeto)
        placeholders = ', '.join(['?'] * len(valores))
        sql = f"INSERT INTO {tabela} ({', '.join(colunas)}) VALUES ({placeholders})"
        self.cursor.execute(sql, valores)
        self.conexao.commit()
        return self.cursor.lastrowid