#importando o arquivo com as Classes
from Classes import *
#importando o módulo Tkinter
from tkinter import *
from tkinter import ttk
#criando uma classe que conterá toda a interface
class Interface(object):
    #método que contém a tela inicial
    def __init__(self, tela):
        #criando e empacotando as frames
        self.espaco = Frame(tela)
        self.espaco.pack()
        self.espaco0 = Frame(tela)
        self.espaco0.pack()
        self.espaco1 = Frame(tela)
        self.espaco1.pack()
        self.espaco2 = Frame(tela)
        self.espaco2.pack()
        self.espaco3 = Frame(tela)
        self.espaco3.pack()
        self.espaco4 = Frame(tela)
        self.espaco4.pack()
        self.espaco5 = Frame(tela)
        self.espaco5.pack()
        self.espaco6 = Frame(tela)
        self.espaco6.pack()
        self.espaco7 = Frame(tela)
        self.espaco7.pack()
        self.espaco8 = Frame(tela)
        self.espaco8.pack()
        self.espaco9 = Frame(tela)
        self.espaco9.pack()
        self.espaco10 = Frame(tela)
        self.espaco10.pack()
        self.espaco11 = Frame(tela)
        self.espaco11.pack()

#criando e empacotando os elementos da tela
        self.msg = Label(self.espaco, text = "Escolha sua ação:")
        self.usuario = Button(self.espaco0, text="Usuário", width = 30, command = self.Interface_Usuario)
        self.livro = Button(self.espaco1, text="Livro", width = 30, command = self.Interface_Livro)
        self.emprestimo = Button(self.espaco2, text="Empréstimo", width = 30, command=self.Interface_Emprestimo)
        self.prazo = Button(self.espaco3, text="Prazo", width = 30)
        self.multa = Button(self.espaco4, text="Multa", width = 30, command=self.Interface_Multa)
        self.msg.pack()
        self.usuario.pack()
        self.livro.pack()
        self.emprestimo.pack()
        self.prazo.pack()
        self.multa.pack()

#criando a tela de usuário
    def Interface_Usuario(self):
        self.inf = Label(self.espaco, text="Informe os dados do usuário:")
        self.inf.pack()
        self.msg_id = Label(self.espaco0, text="Id:")
        self.msg_id.pack(side="left")
        self.id_usuario = Entry(self.espaco0)
        self.id_usuario.pack(side="left")
        self.buscar_usuario = Button(self.espaco0, text="Buscar", command=self.Buscar_Usuario)
        self.buscar_usuario.pack(side="left")
        self.msg_nome = Label(self.espaco1, text="Nome:")
        self.msg_nome.pack(side = "left")
        self.nome = Entry(self.espaco1)
        self.nome.pack(side="left")
        self.msg_cpf = Label(self.espaco2, text="CPF:")
        self.msg_cpf.pack(side = "left")
        self.cpf = Entry(self.espaco2)
        self.cpf.pack()
        self.msg_email = Label(self.espaco3, text="Email:")
        self.msg_email.pack(side ="left")
        self.email = Entry(self.espaco3)
        self.email.pack()
        self.msg_telefone = Label(self.espaco4, text="Telefone:")
        self.msg_telefone.pack(side ="left")
        self.telefone = Entry(self.espaco4)
        self.telefone.pack()
        self.msg_endereco = Label(self.espaco5, text="Endereço:")
        self.msg_endereco.pack(side="left")
        self.endereco = Entry(self.espaco5)
        self.endereco.pack()
        self.salvar = Button(self.espaco6, text="Salvar", command = self.Salvar_Usuario)
        self.salvar.pack(side="left")
        self.alterar = Button(self.espaco6, text="Alterar", command=self.Atualizar_Usuario)
        self.alterar.pack(side="left")
        self.deletar = Button(self.espaco6, text="Deletar", command=self.Apagar_Usuario)
        self.deletar.pack(side="left")
        self.pesquisar = Button(self.espaco6, text="Pesquisar", command=self.Pesquisar_Usuario)
        self.pesquisar.pack(side="left")
        self.voltar = Button(self.espaco6, text="Voltar", command=self.Voltar_Usuario)
        self.voltar.pack()
        self.mensagem = Label(self.espaco7)
        self.mensagem.pack()
        self.tree_usuario = ttk.Treeview(self.espaco7)
        self.tree_usuario.pack()
        self.tree_usuario.config(columns=('nome', 'cpf', 'email', 'telefone', 'endereco'))
        self.tree_usuario.config(height = 200)
        self.tree_usuario.column('#0',width=25)
        self.tree_usuario.heading('nome', text="Nome")
        self.tree_usuario.column('nome', width=100)
        self.tree_usuario.heading('cpf', text="CPF")
        self.tree_usuario.column('cpf', width=100)
        self.tree_usuario.heading('email', text="Email")
        self.tree_usuario.column('email', width = 100)
        self.tree_usuario.heading('telefone', text="Telefone")
        self.tree_usuario.column('telefone', width=100)
        self.tree_usuario.heading('endereco', text="Endereço")
        self.tree_usuario.column('endereco', width=100)
        self.EscondeElementos_Interface()       

#criando a tela de livro
    def Interface_Livro(self):
        self.inf = Label(self.espaco, text="Informe os dados do livro:")
        self.inf.pack()
        self.msg_id = Label(self.espaco0, text="ID:")
        self.msg_id.pack(side="left")
        self.id_livro = Entry(self.espaco0)
        self.id_livro.pack(side="left")
        self.buscar_livro = Button(self.espaco0, text="Buscar", command=self.Buscar_Livro)
        self.buscar_livro.pack(side="left")
        self.msg_titulo = Label(self.espaco1, text="Título:")
        self.msg_titulo.pack(side="left")
        self.titulo = Entry(self.espaco1)
        self.titulo.pack(side="left")
        self.msg_autor = Label(self.espaco2, text="Autor:")
        self.msg_autor.pack(side="left")
        self.autor = Entry(self.espaco2)
        self.autor.pack()
        self.msg_ano = Label(self.espaco3, text="Ano:")
        self.msg_ano.pack(side="left")
        self.ano = Entry(self.espaco3)
        self.ano.pack()
        self.msg_genero = Label(self.espaco4, text="Gênero:")
        self.msg_genero.pack(side="left")
        self.genero = Entry(self.espaco4)
        self.genero.pack(side="left")
        self.salvar = Button(self.espaco5, text="Salvar", command=self.Salvar_Livro)
        self.salvar.pack(side="left")
        self.alterar = Button(self.espaco5, text="Alterar", command=self.Atualizar_Livro)
        self.alterar.pack(side="left")
        self.pesquisar = Button(self.espaco5, text = "Pesquisar")
        self.pesquisar.pack(side='left')
        self.deletar = Button(self.espaco5, text="Deletar", command=self.Apagar_Livro)
        self.deletar.pack(side="left")
        self.voltar = Button(self.espaco5, text="Voltar", command=self.Voltar_Livro)
        self.voltar.pack(side="left")
        self.mensagem = Label(self.espaco6)
        self.mensagem.pack()
        self.tree_livro = ttk.Treeview(self.espaco7)
        self.tree_livro.pack()
        self.tree_livro.config(columns=('titulo', 'autor', 'ano', 'genero'))
        self.tree_livro.config(height = 200)
        self.tree_livro.column('#0',width=25)
        self.tree_livro.heading('titulo', text="Titulo")
        self.tree_livro.column('titulo', width=100)
        self.tree_livro.heading('autor', text="Autor")
        self.tree_livro.column('autor', width=100)
        self.tree_livro.heading('ano', text="Ano")
        self.tree_livro.column('ano', width = 100)
        self.tree_livro.heading('genero', text="Gênero")
        self.tree_livro.column('genero', width=100)              
        self.EscondeElementos_Interface()

#criando a tela de emprestimo
    def Interface_Emprestimo(self):
        self.inf = Label(self.espaco, text="Informe os dados abaixo:")
        self.inf.pack()
        self.msg_id_emprestimo = Label(self.espaco0, text="ID:")
        self.msg_id_emprestimo.pack(side = "left")
        self.id_emprestimo = Entry(self.espaco0)
        self.id_emprestimo.pack()
        self.msg_idusuario = Label(self.espaco1, text="ID_Usuário:")
        self.msg_idusuario.pack(side = "left")
        self.idusuario = Entry(self.espaco1)
        self.idusuario.pack()             
        self.msg_idlivro = Label(self.espaco2, text="ID_Livro:")
        self.msg_idlivro.pack(side = "left")
        self.idlivro = Entry(self.espaco2)
        self.idlivro.pack()
        self.msg_data = Label(self.espaco3, text="Data:")
        self.msg_data.pack(side="left")
        self.data_inicio = Entry(self.espaco3)
        self.data_inicio.pack()
        self.salvar = Button(self.espaco4, text="Salvar", command=self.Salvar_Emprestimo)
        self.salvar.pack(side='left')
        self.alterar = Button(self.espaco4, text="Alterar", command=self.Atualizar_Emprestimo)
        self.alterar.pack(side='left')
        self.pesquisar = Button(self.espaco4, text="Pesquisar")
        self.pesquisar.pack(side='left')
        self.deletar = Button(self.espaco4, text="Deletar", command=self.Apagar_Emprestimo)
        self.deletar.pack(side='left')
        self.voltar = Button(self.espaco4, text="Voltar", command=self.Voltar_Emprestimo)
        self.voltar.pack(side='left')
        self.mensagem = Label(self.espaco5)
        self.mensagem.pack()
        self.tree_emprestimo = ttk.Treeview(self.espaco6)
        self.tree_emprestimo.pack()
        self.tree_emprestimo.config(columns=('id_usuario', 'usuario', 'id_livro', 'livro', 'data_inicio'))
        self.tree_emprestimo.config(height = 200)
        self.tree_emprestimo.column('#0',width=25)
        self.tree_emprestimo.heading('id_usuario', text="Id_Usuario")
        self.tree_emprestimo.column('id_usuario', width=100)
        self.tree_emprestimo.heading('usuario', text="Usuário")
        self.tree_emprestimo.column('usuario', width=100)
        self.tree_emprestimo.heading('id_livro', text="Id_Livro")
        self.tree_emprestimo.column('id_livro', width = 100)
        self.tree_emprestimo.heading('livro', text="Livro")
        self.tree_emprestimo.column('livro', width=100)
        self.tree_emprestimo.heading('data_inicio', text="Data")
        self.tree_emprestimo.column('data_inicio', width=100) 
        self.EscondeElementos_Interface()

    def Interface_Multa(self):
        self.dinheiro = Button(self.espaco0, text="Pagar em dinheiro", command=self.Interface_Dinheiro)
        self.dinheiro.pack()
        self.cartao = Button(self.espaco1, text="Pagar no cartao", command = self.Interface_Cartao)
        self.cartao.pack()
        self.EscondeElementos_Interface()

    def EscondeElementos_Multa(self):
        self.dinheiro.pack_forget()
        self.cartao.pack_forget()

    def Interface_Dinheiro(self):

        self.msg1 = Label(self.espaco, text = "Digite as informações abaixo:")
        self.msg1.pack()
        self.msg2 = Label(self.espaco0, text = " Números de dias atrasados:")
        self.msg2.pack(side="left")
        self.dias = Entry(self.espaco0)
        self.dias.pack()
        self.gerar = Button(self.espaco1, text = "Gerar multa")
        self.gerar.pack()
        self.resultado = Label(self.espaco2)
        self.resultado.pack()
        self.EscondeElementos_Interface()
        self.EscondeElementos_Multa()

    def Interface_Cartao(self):
        self.msg1 = Label(self.espaco)
        
    #def Gerar_Multa(self, 
      


        
#esconde os elementos da tela inicial com o método pack_forget
    def EscondeElementos_Interface(self):
        self.msg.pack_forget()
        self.usuario.pack_forget()
        self.livro.pack_forget()
        self.emprestimo.pack_forget()
        self.prazo.pack_forget()
        self.multa.pack_forget()

#mostra/empacota os elementos novamente
    def MostraElementos(self):
        self.msg.pack()
        self.usuario.pack()
        self.livro.pack()
        self.emprestimo.pack()
        self.prazo.pack()
        self.multa.pack()
          
#esconde os elementos da tela de usuario e volta pra tela inicial
    def Voltar_Usuario(self):
        self.buscar_usuario.pack_forget()
        self.inf.pack_forget()
        self.msg_id.pack_forget()
        self.id_usuario.pack_forget()
        self.msg_nome.pack_forget()
        self.nome.pack_forget()
        self.msg_cpf.pack_forget()
        self.cpf.pack_forget()
        self.msg_email.pack_forget()
        self.email.pack_forget()
        self.msg_telefone.pack_forget()
        self.telefone.pack_forget()
        self.msg_endereco.pack_forget()
        self.endereco.pack_forget()
        self.salvar.pack_forget()
        self.alterar.pack_forget()
        self.pesquisar.pack_forget()
        self.deletar.pack_forget()
        self.voltar.pack_forget()
        self.mensagem.pack_forget()
        self.tree_usuario.pack_forget()
        self.MostraElementos()

#esconde os elementos da tela de livro e volta para a tela inicial
    def Voltar_Livro(self):
        self.buscar_livro.pack_forget()
        self.inf.pack_forget()
        self.msg_id.pack_forget()
        self.id_livro.pack_forget()
        self.msg_titulo.pack_forget()
        self.titulo.pack_forget()
        self.msg_autor.pack_forget()
        self.autor.pack_forget()
        self.msg_ano.pack_forget()
        self.ano.pack_forget()
        self.msg_genero.pack_forget()
        self.genero.pack_forget()
        self.salvar.pack_forget()
        self.alterar.pack_forget()
        self.pesquisar.pack_forget()
        self.deletar.pack_forget()
        self.voltar.pack_forget()
        self.mensagem.pack_forget()
        self.tree_livro.pack_forget()
        self.MostraElementos()

#esconde os elementos da tela de emprestimo e volta para a tela inicial
    def Voltar_Emprestimo(self):
        self.inf.pack_forget()
        self.msg_id_emprestimo.pack_forget()
        self.id_emprestimo.pack_forget()
        self.msg_idusuario.pack_forget()
        self.idusuario.pack_forget()
        self.msg_idlivro.pack_forget()
        self.idlivro.pack_forget()
        #self.msg_livro.pack_forget()
        #self.titulo_livro.pack_forget()
        #self.msg_nome.pack_forget()
        #self.nome_usuario.pack_forget()
        self.msg_data.pack_forget()
        self.data_inicio.pack_forget()
        self.salvar.pack_forget()
        self.alterar.pack_forget()
        self.pesquisar.pack_forget()
        self.deletar.pack_forget()
        self.voltar.pack_forget()
        self.mensagem.pack_forget()
        self.tree_emprestimo.pack_forget()
        self.MostraElementos()

    def Voltar_Multa(self):
        self.dinheiro.pack_forget()
        self.cartao.pack_forget()
        self.MostraElementos()
        
#salva os dados digitados do usuario
    def Salvar_Usuario(self):
        #instanciando a classe usuarios
        usuario = Usuarios()

        usuario.nome = self.nome.get()
        usuario.cpf = self.cpf.get()
        usuario.telefone = self.telefone.get()
        usuario.email = self.email.get()
        usuario.endereco = self.endereco.get()

        self.mensagem['text'] = usuario.SalvarUsuario()

        self.id_usuario.delete(0, END)
        self.nome.delete(0, END)
        self.cpf.delete(0, END)
        self.telefone.delete(0, END)
        self.email.delete(0, END)
        self.endereco.delete(0, END)

#metodo para buscar o usuario atraves da captura do id
    def Buscar_Usuario(self):
        usuario = Usuarios()
   
        usuario.id_usuario = self.id_usuario.get()
   
        self.mensagem['text'] = usuario.BuscarUsuario()

        self.nome.delete(0, END)
        self.nome.insert(INSERT, usuario.nome)
        
        self.cpf.delete(0, END)
        self.cpf.insert(INSERT, usuario.cpf)
   
        self.telefone.delete(0, END)
        self.telefone.insert(INSERT,usuario.telefone)
   
        self.email.delete(0, END)
        self.email.insert(INSERT, usuario.email)
   
        self.endereco.delete(0, END)
        self.endereco.insert(INSERT, usuario.endereco)

    def Pesquisar_Usuario(self):
        usuario = Usuarios()

        if self.id_usuario==None:
            for linha in linhas:
                print(linha)
                self.tree_usuario.insert("", self.espaco7.END, values=linha) 
            
                
            

   
# método para alterar o usuario               
    def Atualizar_Usuario(self):
        usuario = Usuarios()
        
        usuario.id_usuario = self.id_usuario.get()
        usuario.nome = self.nome.get()
        usuario.cpf = self.cpf.get()
        usuario.telefone = self.telefone.get()
        usuario.email = self.email.get()
        usuario.endereco = self.endereco.get()

        self.mensagem['text'] = usuario.AtualizarUsuario()

        self.id_usuario.delete(0, END)
        self.nome.delete(0, END)
        self.cpf.delete(0, END)
        self.telefone.delete(0, END)
        self.email.delete(0, END)
        self.endereco.delete(0, END)

#metodo para apagar o usuario
    def Apagar_Usuario(self):
        usuario = Usuarios()
   
        usuario.id_usuario = self.id_usuario.get()
        
        self.mensagem['text'] = usuario.ApagarUsuario()

        self.id_usuario.delete(0, END)
        self.nome.delete(0, END)
        self.cpf.delete(0, END)
        self.telefone.delete(0, END)
        self.email.delete(0, END)
        self.endereco.delete(0, END)

#metodo para salvar livro
    def Salvar_Livro(self):
        #instanciando a classe livros
        livro = Livros()
        
        livro.id_livro = self.id_livro.get()
        livro.titulo = self.titulo.get()
        livro.autor = self.autor.get()
        livro.ano = self.ano.get()
        livro.genero = self.genero.get()

        self.mensagem['text'] = livro.SalvarLivro()

        self.id_livro.delete(0, END)
        self.titulo.delete(0, END)
        self.autor.delete(0, END)
        self.ano.delete(0, END)
        self.genero.delete(0, END)
        
# metodo para buscar livro       
    def Buscar_Livro(self):
        livro = Livros()

        livro.id_livro = self.id_livro.get()

        self.mensagem['text'] = livro.BuscarLivro()

        self.titulo.delete(0, END)  
        self.titulo.insert(INSERT, livro.titulo)
        self.autor.delete(0, END)        
        self.autor.insert(INSERT, livro.autor)
        self.ano.delete(0, END)
        self.ano.insert(INSERT, livro.ano)
        self.genero.delete(0, END)
        self.genero.insert(INSERT, livro.genero)

#              
    def Atualizar_Livro(self):
        livro = Livros()

        livro.id_livro = self.id_livro.get()
        livro.titulo = self.titulo.get()
        livro.autor = self.autor.get()
        livro.ano = self.ano.get()
        livro.genero = self.genero.get()

        self.mensagem['text'] = livro.AtualizarLivro()

        self.id_livro.delete(0, END)
        self.titulo.delete(0, END)
        self.autor.delete(0, END)
        self.ano.delete(0, END)
        self.genero.delete(0, END)

#
    def Apagar_Livro(self):
        livro = Livros()
   
        livro.id_livro= self.id_livro.get()
        
        self.mensagem['text'] = livro.ApagarLivro()

        self.id_livro.delete(0, END)
        self.titulo.delete(0, END)
        self.autor.delete(0, END)
        self.ano.delete(0, END)
        self.genero.delete(0, END)

#metodo para salvar emprestimo
    def Salvar_Emprestimo(self):
        #instanciando a classe emprestimos
        emprestimo = Emprestimos()
        
        emprestimo.id_emprestimo = self.id_emprestimo.get()
        emprestimo.idusuario = self.idusuario.get()
       #emprestimo.nome_usuario = self.nome_usuario.get()
        emprestimo.idlivro = self.idlivro.get()
       #emprestimo.titulo_livro = self.titulo_livro.get()
        emprestimo.data_inicio = self.data_inicio.get()
        

        self.mensagem['text'] = emprestimo.SalvarEmprestimo()

        self.id_emprestimo.delete(0, END)
        self.idusuario.delete(0, END)
        self.nome_usuario.delete(0, END)
        self.idlivro.delete(0, END)
        self.titulo_livro.delete(0, END)
        self.data_inicio.delete(0, END)
        
# metodo para buscar emprestimo      
    def Buscar_Emprestimo(self):
        emprestimo = Emprestimos()

        emprestimo.id_emprestimo = self.id_emprestimo.get()

        self.mensagem['text'] = emprestimo.BuscarEmprestimo()

        
        self.idusuario.delete(0, END)
        self.idusuario.insert(INSERT, emprestimo.idusuario)
        self.nome_usuario.delete(0, END)
        self.nome_usuario.insert(INSERT, emprestimo.nome_usuario)
        self.idlivro.delete(0, END)
        self.idlivro.insert(INSERT, emprestimo.idlivro)
        self.titulo_livro.delete(0, END)
        self.titulo_livro.insert(INSERT, emprestimo.titulo_livro)
        self.data_inicio.delete(0, END)
        self.data_inicio.insert(INSERT, emprestimo.data_inicio)
        

#              
    def Atualizar_Emprestimo(self):
        emprestimo = Emprestimos()

        emprestimo.id_emprestimo = self.id_emprestimo.get()
        emprestimo.idusuario = self.id_usuario.get()
       # emprestimo.nome_usuario = self.nome_usuario.get()
        emprestimo.idlivro = self.id_livro.get()
        #emprestimo.titulo_livro = self.titulo_livro.get()
        emprestimo.data_inicio = self.data_inicio.get()

        self.mensagem['text'] = emprestimo.AtualizarEmprestimo()

        self.id_emprestimo.delete(0, END)
        self.idusuario.delete(0, END)
        self.nome_usuario.delete(0, END)
        self.idlivro.delete(0, END)
        self.titulo_livro.delete(0, END)
        self.data_inicio.delete(0, END)

#
    def Apagar_Emprestimo(self):
        emprestimo = Emprestimos()

        emprestimo.id_emprestimo = self.id_emprestimo.get()
        
        self.mensagem['text'] = emprestimo.ApagarEmprestimo()

        self.id_emprestimo.delete(0, END)
        self.idusuario.delete(0, END)
        self.nome_usuario.delete(0, END)
        self.idlivro.delete(0, END)
        self.titulo_livro.delete(0, END)
        self.data_inicio.delete(0, END)
       
   
tela = Tk()
Interface(tela)
tela.title("Sistema Bibliotecário")
tela.geometry("650x400")
tela.mainloop
