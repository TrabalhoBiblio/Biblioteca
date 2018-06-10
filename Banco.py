# importando o módulo SQLLite3
import sqlite3
#
class Banco(object):
#cria e faz a conexão com o banco de dados
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTableUsuario()
        self.createTableLivro()
        self.createTableEmprestimo
        self.encerrar()
        
#encera o banco
    def encerrar(self):
        cursor = self.conexao.cursor()
        cursor.close()
#cria a tabela usuarios
    def createTableUsuario(self):
        cursor = self.conexao.cursor()

        cursor.execute("""create table if not exists usuarios(
                             id_usuario integer not null primary key autoincrement,
                             nome text not null,
                             cpf text not null,
                             telefone text,
                             email text,
                             endereco text not null);""")
        self.conexao.commit()
     
#cria a tabela livros
    def createTableLivro(self):
        cursor = self.conexao.cursor()

        cursor.execute(""" create table if not exists livros(
                          id_livro integer not null primary key autoincrement,
                          titulo text not null,
                          autor text not null,
                          ano text not null,
                          genero text);""")

        self.conexao.commit()

#cria a tabela emprestimos
    def createTableEmprestimo(self):
        cursor = self.conexao.cursor()

        cursor.execute("""create table if not exists emprestimos(
                        id_emprestimo integer not null primary key autoincrement,
                        idusuario text not null,
                        idlivro text not null,
                        data_inicio text not null);""")

        self.conexao.commit()
        


    
    
                          
