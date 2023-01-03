from tkinter import * 
from tkinter import messagebox
from tkinter import ttk
import DataBaser

janela = Tk()
janela.title("Painel de acesso")
janela.geometry("600x300")
janela.configure(background="#201b2c")
janela.resizable(width=False, height=False)
# janela.attributes("-alpha", 0.9)
janela.iconbitmap(default="C:/Users/Erick/Desktop/Meu Portifolio/assets/projetos/Login/img/favicon.ico")

#carregando imagens
logo = PhotoImage(file="C:/Users/Erick/Desktop/Meu Portifolio/assets/projetos/Login/img/logo.png")

#Widgets
FrameEsquerda = Frame(janela, width=200, height=300, bg="#201b2c", relief="raise")
FrameEsquerda.pack(side=LEFT)

FrameDireita = Frame(janela, width=395, height=300, bg="#201b2c", relief="raise")
FrameDireita.pack(side=RIGHT)
#Logo
LogoLabel = Label(FrameEsquerda, image=logo, bg="#201b2c")
LogoLabel.place(x=50, y=100)
#Logo
#Usuário
UserLabel = Label(FrameDireita, text = "Usuário:", font=("Century Gothic", 20), bg="#201b2c", fg="#00ff88")
UserLabel.place(x=5, y=100)

EntradaUser = ttk.Entry(FrameDireita, width=37)
EntradaUser.place(x=110, y=110)
#Usuário
#Senha
SenhaLabel = Label(FrameDireita, text="Senha:", font=("Century Gothic", 20), bg="#201b2c", fg="#00ff88")
SenhaLabel.place(x=5, y=150)

EntradaSenha = ttk.Entry(FrameDireita, width=38, show="•")
EntradaSenha.place(x=105, y=160)
#Senha
#Botoes
#Função Entrar atribuida no botão de Login
def Entrar():
    Usuario = EntradaUser.get()
    Senha = EntradaSenha.get()
    
    DataBaser.cursor.execute("""
        SELECT * FROM Usuarios
        WHERE (Usuario = ? and Senha = ?)
     """, (Usuario, Senha))
    print("Selecionou")
    VerificarLogin = DataBaser.cursor.fetchone()
    try:    
        if(Usuario in VerificarLogin and Senha in VerificarLogin):
            messagebox.showinfo(title="Informação de Entrada", message="Acesso Confirmado. Seja Bem Vindo!")
    except:
        messagebox.showinfo(title="Informação de Entrada", message="Acesso Negado. Verifique se está Cadastrado no Sistema.")

LoginBtn = ttk.Button(FrameDireita, text="Entrar",width=30, command=Entrar)
LoginBtn.place(x=100, y=225)
def Register():
    #A função Register retira os botões de Entrar e Cadastrar e cria Entradas para Nome e Email
    LoginBtn.place(x=1000)
    CadasBtn.place(x=1000)
    NomeLabel = Label(FrameDireita, text="Nome:", font=("Century Gothic", 20), bg="#201b2c", fg="#00ff88")
    NomeLabel.place(x=5, y=5)
    
    EntradaNome = ttk.Entry(FrameDireita, width=39)
    EntradaNome.place(x=100, y=20)
    
    EmailLabel = Label(FrameDireita, text="E-mail:", font=("Century Gothic", 20), bg="#201b2c", fg="#00ff88")
    EmailLabel.place(x=5 ,y=55)
    
    EntradaEmail = ttk.Entry(FrameDireita, width=39)
    EntradaEmail.place(x=100, y=66)
    #Cadastro no banco de dados
    def CadastroDataBaser():
        Nome = EntradaNome.get()
        Email = EntradaEmail.get()
        Usuario = EntradaUser.get()
        Senha = EntradaSenha.get()
        
        if(Nome == "" and Email == "" and Usuario =="" and Senha == ""):
            messagebox.showerror(title="Erro de cadastro", message="Preencha Todos os Campos.")
        else:
            DataBaser.cursor.execute("""
                INSERT INTO Usuarios(Nome, Email, Usuario, Senha) VALUES(?, ?, ?, ?)
            """, (Nome, Email, Usuario, Senha))
            DataBaser.conn.commit()
            messagebox.showinfo(title="Informação de Cadastro", message="Conta criada com sucesso!")
    
    Cadastro = ttk.Button(FrameDireita, text="Cadastrar", width=30, command=CadastroDataBaser)
    Cadastro.place(x=100, y=225)
    
    def VoltaLogin():
        NomeLabel.place(x=1000)
        EntradaNome.place(x=1000)
        EmailLabel.place(x=1000)
        EntradaEmail.place(x=1000)
        Cadastro.place(x=1000)
        Voltar.place(x=1000)
        #A função VoltaLogin retira toda a parte de cadastro e traz de volta os botões de Entrar e Cadastrar
        LoginBtn.place(x=100, y=225)
        CadasBtn.place(x=130, y=260)
    
    Voltar = ttk.Button(FrameDireita, text="Voltar", width=20, command=VoltaLogin)
    Voltar.place(x=125, y=260)

CadasBtn = ttk.Button(FrameDireita, text="Cadastrar", width=20, command=Register)
CadasBtn.place(x=130, y=260)
#Botoes

janela.mainloop()