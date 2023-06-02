import tkinter as tk
from tkinter import Button, PhotoImage, ttk
from tkinter import messagebox
import cadastro
import esquec_senha
from view import *


janela = tk.Tk()

janela.title("Proteste")  # editar titulo
janela.geometry("1200x700")
janela.resizable(False, False)
janela.configure(bg="#04345C")


def verificar_login():
    usuario = caixa_texto_usuario.get()
    senha = caixa_texto_senha.get()

    verificar = verificar_cadastro(usuario, senha)
    if verificar == True:
        messagebox.showinfo("Sucesso!", "Login realizado com sucesso")
        import tela01
        janela.destroy()
        tela01.tela_01()

    else:
        messagebox.showerror("Erro", "Usuario ou Senha incorreto!")


# backgraud
imagem = PhotoImage(file="img//3.png")
imagem = imagem.subsample(1, 1)
labelimagem = tk.Label(image=imagem)
labelimagem.place(x=0, y=0, relwidth=1.0, relheight=1.0)


# valor do x para Login, Usuario, Senha
valorx = 0.02
valory = 0.3

# label da marca
labelmarca = tk.Label(text="PROTESTE", foreground="#6BD4CD",
                      width="30", height="5", font=("Tamoho", 80), bg="#195473")
labelmarca.place(relx=valorx+0.35, rely=valory +
                 0.10, relwidth=.50, relheight=.13)

# label slogan
labelslogan = tk.Label(text="SOFTWARE DE TESTE", foreground="#6BD4CD",
                       width="30", height="5", font=("Tamoho", 25), bg="#195473")
labelslogan.place(relx=valorx+0.42, rely=valory +
                  0.22, relwidth=.35, relheight=.05)

# label de login
labelLogin = tk.Label(text="LOGIN", foreground="#6BD4CD",
                      width="30", height="5", font=("Tamoho", 60), bg="#195473")
labelLogin.place(relx=valorx, rely=valory, relwidth=.23, relheight=.12)

# label de usuario
labelusuario = tk.Label(text="Usuário:", fg="#6BD4CD",
                        font=("Arial", 20), bg="#195473")
labelusuario.place(relx=valorx, rely=valory+0.12, relwidth=.08, relheight=.06)

caixa_texto_usuario = tk.Entry(janela, width=10, bg="#6BD4CD")
caixa_texto_usuario.place(relx=valorx, rely=valory +
                          0.2, relwidth=.25, relheight=.06)

# label de senha
labelsenha = tk.Label(text="Senha:", fg="#6BD4CD",
                      font=("Arial", 20), bg="#195473")
labelsenha.place(relx=valorx, rely=valory+0.27, relwidth=.08, relheight=.06)

caixa_texto_senha = tk.Entry(width=10, bg="#6BD4CD")
caixa_texto_senha.place(relx=valorx, rely=valory+0.35,
                        relwidth=.25, relheight=.06)

# botão de acesso

botao_acessar = Button(
    text="Acessar", command=verificar_login, width=10, height=5, bg="#6BD4CD")
botao_acessar.place(relx=valorx, rely=0.74, relwidth=.10, relheight=.06)

# botão de esqueci a senha

botao_esqueci_senha = Button(
    text="Esqueci a senha", command=esquec_senha.esqueci_a_senha, width=10, height=5, bg="#6BD4CD")
botao_esqueci_senha.place(relx=valorx, rely=0.81, relwidth=.25, relheight=.03)

# botão cadastro

botao_cadastrar = Button(
    text="Novo Cadastro", command=cadastro.novo_cadastro, width=10, height=5, bg="#6BD4CD")
botao_cadastrar.place(relx=valorx+0.15, rely=0.74, relwidth=.10, relheight=.06)


janela.mainloop()  # mainloop = loop infinito para deixar a tela visivel
