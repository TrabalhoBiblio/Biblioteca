#importando a classe Banco do arquivo Banco
from Banco import Banco 

#criando a classe usuarios
class Usuarios(object):
#método inicial que contem os atributos das classe
    def __init__(self, id_usuario = 0, nome= "", cpf= "" , email= "" , telefone= "" , endereco= "" ):
        self.id_usuario = id_usuario
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.endereco = endereco
                
#método para salvar cadastrar o usuario no banco
    def SalvarUsuario(self):
        banco = Banco()

        cursor = banco.conexao.cursor()

        cursor.execute ("""insert into usuarios(nome, cpf, email, telefone, endereco) values (?,?,?,?,?)""",
                        (self.nome, self.cpf, self.email, self.telefone, self.endereco))

        banco.conexao.commit()

        resultado = banco.conexao.commit

        cursor.close()

        return "Usuario cadastrado com sucesso!"              

        
#método para alterar o usuário no banco
    def AtualizarUsuario(self):
        banco = Banco()

        cursor = banco.conexao.cursor()

        cursor.execute("""update usuarios set nome = ?, cpf = ?, email = ?, telefone = ?, endereco = ? where id_usuario = ?""",
                       (self.nome, self.cpf, self.email, self.telefone, self.endereco, self.id_usuario))

        banco.conexao.commit()

        cursor.close()

        return "Usuário alterado com sucesso!"
#método para alterar o usuário no banco
    def ApagarUsuario(self):
        banco = Banco()

        cursor = banco.conexao.cursor()

        cursor.execute(""" delete from usuarios where id_usuario =:id_usuario""", {"id_usuario":self.id_usuario})

        banco.conexao.commit()
        
        cursor.close()

        return "Usuario excluido com sucesso"
#método para alterar o usuário no banco
    def BuscarUsuario(self):
        banco = Banco()

        cursor = banco.conexao.cursor()

        cursor.execute(""" select * from usuarios where id_usuario =:id_usuario""", {"id_usuario":self.id_usuario})

        for linha in cursor:
                  self.idusuario = linha[0]
                  self.nome = linha[1]
                  self.cpf = linha[2]
                  self.telefone = linha[3]
                  self.email = linha[4]
                  self.endereco = linha[5]                 
   
          
        return "Busca feita com sucesso!"

    def PesquisarUsuario(self):
        banco = Banco()

        cursor = banco.conexao.cursor()

        cursor.execute(""" select * from usuarios """)

        linhas = cursor.fetchall()

        for linha in linhas:
            print(linha)
            self.tree_usuario.insert("", self.espaco7.END, values=linha)
        return linha
          
      
#criando a classe livros
class Livros(object):
#método inicial que contem os atributos das classe
    def __init__(self, id_livro = 0, titulo= "", autor= "" , ano= "" , genero= "" ):
        self.id_livro = id_livro
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.genero = genero
                        
#método para cadastrar o livro no banco
    def SalvarLivro(self):
        banco = Banco()

        cursor = banco.conexao.cursor()

        cursor.execute ("""insert into livros(titulo, autor, ano, genero) values (?,?,?,?)""", (self.titulo, self.autor, self.ano, self.genero))

        banco.conexao.commit()

        cursor.close()
        
        return "Livro cadastrado com sucesso!"
#método para atualizar o livro no banco
    def AtualizarLivro(self):
        banco = Banco()

        cursor = banco.conexao.cursor()

        cursor.execute("""update livros set titulo = ?, autor = ?, ano = ?, genero = ? where id_livro = ?""" ,
                       (self.titulo, self.autor, self.ano, self.genero, self.id_livro))

        banco.conexao.commit()

        cursor.close()

        return "Livro alterado com sucesso!"
#método para apagar o livro no banco
    def ApagarLivro(self):
        banco = Banco()

        cursor = banco.conexao.cursor()

        cursor.execute("""delete from livros where id_livro =:id_livro""", {"id_livro":self.id_livro})

        banco.conexao.commit()
        
        cursor.close()

        return "Livro excluido com sucesso"
#método para buscar o livro no banco
    def BuscarLivro(self):
        banco = Banco()

        cursor = banco.conexao.cursor()

        cursor.execute(""" select * from livros where id_livro =:id_livro""", {"id_livro":self.id_livro})

        for linha in cursor:
                  self.id_livro = linha[0]
                  self.titulo = linha[1]
                  self.autor = linha[2]
                  self.ano = linha[3]
                  self.genero = linha[4]                                   
   
          
        return "Busca feita com sucesso!"

#criando a classe emprestimos
class Emprestimos(object):
#método para alterar o usuário no banco   
    def __init__(self, id_emprestimo = 0, idusuario = "", idlivro = "", data_inicio = ""):
        self.id_emprestimo = id_emprestimo    
        self.idusuario = idusuario
        #self.nome_usuario = nome_usuario
        self.idlivro = idlivro
        #self.titulo_livro = titulo_livro
        self.data_inicio = data_inicio
        
#método para cadastrar o emprestimo no banco
    def SalvarEmprestimo(self):
        banco = Banco()

        cursor = banco.conexao.cursor()

        cursor.execute("""insert into emprestimos(idusuario, idlivro, data_inicio) values (?,?,?,?,?)""",
                       (self.idusuario, self.idlivro, self.data_inicio))

        banco.conexao.commit()

        cursor.close()

        return "Emprestimo cadastrado com sucesso!"

#método para alterar o emprestimo no banco
    def AtualizarEmprestimo(self):
        banco = Banco()

        cursor = banco.conexao.cursor()

        cursor.execute(""" update emprestimos set ( idusuario, idlivro, data_inicio) values (?,?,?,?,?,?)""",
                       (self.idusuario, self.idlivro, self.data_inicio))

        banco.conexao.commit()

        cursor.close()

        return "Empréstimo alterado com sucesso!"        

#método para aapagar o emprestimo no banco
    def ApagarEmprestimo(self):
        banco = Banco()

        cursor = banco.conexao.cursor()

        cursor.execute(""" delete from emprestimos where id_emprestimo = ? """, (self.id_emprestimo))

        banco.conexao.commit()

        cursor.close()

        return "Emprestimo deletado com sucesso!"

#método para buscar o emprestimo no banco
    def BuscarEmprestimo(self):
        banco = Banco()

        cursor = banco.conexao.cursor()

        cursor.execute("""  """)

        cursor.close()
        
        return "Busca realizada com sucesso!"
