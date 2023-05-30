from tkinter import 
from tkinter import messagebox
from tkinter import ttk
import sqlite3 as lite

'''
# criando a conexão
con = lite.connect('dados.db')

# criando a tabela
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE formulario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT, telefone TEXT, cpf TEXT)")
'''

#CRUD

#Create = Adicionar/criar
#Ready = Acessar/mostrar
#Update = Atualizar/alterar
#Delete = Deletar/excluir


#criando a conexão
con = lite.connect('dados.db')


#Adicionar informações
def adicionar_info(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO formulario (nome, email, telefone, cpf) VALUES (?, ?, ?, ?)"
        cur.execute(query, i)


#Acessar informações
def mostrar_info():
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM formulario"
        cur.execute(query)
        info = cur.fetchall()
        
        for i in info:
            lista.append(i)
    return lista


lista = ['lucas', 1]
#Atualizar as informações
def atualizar_info(i):
    with con:
        cur = con.cursor()
        query = "UPDATE formulario SET nome=?, email=?, telefone=?, cpf=?, WHERE id=?"
        cur.execute(query, i)


lista = [1]
#Excluir as informações
def deletar_info(id):
    with con:
        cur = con.cursor()
        query = "DELETE FROM formulario WHERE id=?"
        cur.execute(query, id)



def cadastrar_usuario():
    nome = entry_nome.get()
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    # Verificar se os campos estão preenchidos
    if nome == "" or usuario == "" or senha == "":
        messagebox.showerror("Erro", "Preencha todos os campos.")
    else:
        messagebox.showinfo("Cadastro", "Cadastro realizado com sucesso!")

def fazer_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    # Verificar se as credenciais são válidas
    if usuario == usuario and senha == senha:
        messagebox.showinfo("Login", "Login bem-sucedido!")
        janela_tabela()
    else:
        messagebox.showerror("Login", "Credenciais inválidas. Tente novamente.")

def janela_tabela():
    janela_login.destroy()

    janela_tabela = Tk()
    janela_tabela.title('Tabela de Usuários')
    janela_tabela.geometry('860x460')
    janela_tabela.configure(background='gray84')
    janela_tabela.resizable(width=FALSE, height=FALSE)

    # Resto do código para a janela da tabela

# Criar janela de login
janela_login = Tk()
janela_login.title("Cadastro e Login")
janela_login.geometry("300x200")
janela_login.configure(background='gray84')
janela_login.resizable(width=FALSE, height=FALSE)


# Criar rótulo de nome
label_nome = Label(janela_login, text="Nome:")
label_nome.pack()

# Criar campo de entrada de nome
entry_nome = Entry(janela_login)
entry_nome.pack()

# Criar rótulo de usuário
label_usuario = Label(janela_login, text="Usuário:")
label_usuario.pack()

# Criar campo de entrada de usuário
entry_usuario = Entry(janela_login)
entry_usuario.pack()

# Criar rótulo de senha
label_senha = Label(janela_login, text="Senha:")
label_senha.pack()

# Criar campo de entrada de senha
entry_senha = Entry(janela_login, show="*")
entry_senha.pack()

# Criar botão de cadastro
botao_cadastrar = Button(janela_login, text="Cadastrar", command=cadastrar_usuario)
botao_cadastrar.pack()

# Criar botão de login
botao_login = Button(janela_login, text="Login", command=fazer_login)
botao_login.pack()

# Iniciar loop da janela de login
janela_login.mainloop()

#criando a janela
janela_tabela = Tk()
janela_tabela.title('Tabela de Usuários')
janela_tabela.geometry('860x460')
janela_tabela.configure(background='gray84')
janela_tabela.resizable(width=FALSE, height=FALSE)

#dividindo a janela
frame_cima = Frame(janela_tabela, width=310, height=50, bg='gray7', relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela_tabela, width=310, height=400, bg='gray67', relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_dir = Frame(janela_tabela, width=588, height=400, bg='gray92', relief='flat')
frame_dir.grid(row=0, column=1, rowspan=2, padx=1, sticky=NSEW)

#Label de cima
app_nome = Label(frame_cima, text='Ficha de Cadastro', anchor=NW, font=('Ivy 13 bold'), bg='gray7', fg='white', relief='flat')
app_nome.place(x=10, y=20)

#Variavel tree global
global tree

#Função adicionar
def adicionar():
    nome = ent_nome.get()
    email = ent_email.get()
    telefone = ent_telefone.get()
    cpf = ent_cpf.get()

    lista = [nome, email, telefone, cpf]

    if nome == '':
        messagebox.showerror('Erro', 'O campo nome pode estar vazio.')
    else:
        adicionar_info(lista)
        messagebox.showinfo('Sucesso', 'Dados inseridos com sucesso!')

        ent_nome.delete(0, 'end')
        ent_email.delete(0, 'end')
        ent_telefone.delete(0, 'end')
        ent_cpf.delete(0, 'end')

    for widget in frame_dir.winfo_children():
        widget.destroy()

    mostrar()


#Função atualizar
def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor_id = tree_lista[0]

        ent_nome.delete(0, 'end')
        ent_email.delete(0, 'end')
        ent_telefone.delete(0, 'end')
        ent_cpf.delete(0, 'end')

        ent_nome.insert(0, tree_lista[1])
        ent_email.insert(0, tree_lista[2])
        ent_telefone.insert(0, tree_lista[3])
        ent_cpf.insert(0, tree_lista[4])

        def alterar():
            nome = ent_nome.get()
            email = ent_email.get()
            telefone = ent_telefone.get()
            cpf = ent_cpf.get()

            lista = [nome, email, telefone, cpf, valor_id]

            if nome == '':
                messagebox.showerror('Erro', 'O campo nome pode estar vazio.')
            else:
                messagebox.showinfo('Sucesso', 'Dados atualizados com sucesso!')

                ent_nome.delete(0, 'end')
                ent_email.delete(0, 'end')
                ent_telefone.delete(0, 'end')
                ent_cpf.delete(0, 'end')

            for widget in frame_dir.winfo_children():
                widget.destroy()

            mostrar()
        #Botão atualizar
        b_confirmar = Button(frame_baixo, command=alterar, text='Confirmar', width=10, font=('Ivy 7 bold'), bg='green', fg='white', relief='raised', overrelief='ridge')
        b_confirmar.place(x=112, y=370)

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados na tabela')

#Função deletar
def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor_id = [tree_lista[0]]

        deletar_info(valor_id)
        messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso!')

        for widget in frame_dir.winfo_children():
            widget.destroy()

        mostrar()

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados na tabela')


#Configurando o frame baixo

#Nome
label_nome = Label(frame_baixo, text='Nome *', anchor=NW, font=('Ivy 10 bold'), bg='gray67', fg='black', relief='flat')
label_nome.place(x=10, y=10)
ent_nome = Entry(frame_baixo, width=45, justify='left', relief='solid')
ent_nome.place(x=15, y=30)

#Email
label_email = Label(frame_baixo, text='Email *', anchor=NW, font=('Ivy 10 bold'), bg='gray67', fg='black', relief='flat')
label_email.place(x=10, y=70)
ent_email = Entry(frame_baixo, width=45, justify='left', relief='solid')
ent_email.place(x=15, y=90)

#Telefone
label_telefone = Label(frame_baixo, text='Telefone *', anchor=NW, font=('Ivy 10 bold'), bg='gray67', fg='black', relief='flat')
label_telefone.place(x=10, y=130)
ent_telefone = Entry(frame_baixo, width=45, justify='left', relief='solid')
ent_telefone.place(x=15, y=150)

#Cpf
label_cpf = Label(frame_baixo, text='CPF *', anchor=NW, font=('Ivy 10 bold'), bg='gray67', fg='black', relief='flat')
label_cpf.place(x=10, y=200)
ent_cpf = Entry(frame_baixo, width=45, justify='left', relief='solid')
ent_cpf.place(x=15, y=220)

#Botão adicionar
b_adicionar = Button(frame_baixo, command=adicionar, text='Adicionar', width=10, font=('Ivy 9 bold'), bg='blue', fg='white', relief='raised', overrelief='ridge')
b_adicionar.place(x=15, y=340)

#Botão alterar
b_alterar = Button(frame_baixo, command=atualizar, text='Alterar', width=10, font=('Ivy 9 bold'), bg='green', fg='white', relief='raised', overrelief='ridge')
b_alterar.place(x=112, y=340)

#Botão excluir
b_excluir = Button(frame_baixo, command=deletar, text='Excluir', width=10, font=('Ivy 9 bold'), bg='red', fg='white', relief='raised', overrelief='ridge')
b_excluir.place(x=210, y=340)


#Frame direita
def mostrar():
    global tree
    lista = mostrar_info()
    
    #Cabeçalho
    tabela_cabeca = ['ID', 'Nome', 'Email', 'Telefone', 'CPF']
    
    #Criando tabela
    tree = ttk.Treeview(frame_dir, selectmode='extended', columns=tabela_cabeca, show='headings')
    
    #Scrollbar vertical
    sbv = ttk.Scrollbar(frame_dir, orient='vertical', command=tree.yview)
    
    #Scrollbar horizontal
    sbh = ttk.Scrollbar(frame_dir, orient='horizontal', command=tree.xview)
    tree.configure(yscrollcommand=sbv.set, xscrollcommand=sbh.set)
    tree.grid(column=0, row=0, sticky='nsew')
    sbv.grid(column=1, row=0, sticky='ns')
    sbh.grid(column=0, row=1, sticky='ew')
    frame_dir.grid_rowconfigure(0, weight=12)

    hd=['nw', 'nw', 'nw', 'center', 'center']
    h=[60, 160, 130, 100, 80]
    n=0

    for col in tabela_cabeca:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=h[n], anchor=hd[0])
        n+=1

    for item in lista:
        tree.insert('', 'end', values=item)

mostrar()

janela_tabela.mainloop()
