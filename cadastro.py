import tkinter as tk
from tkinter import Button, PhotoImage, ttk
from tkinter import messagebox

def novo_cadastro():
    janela_cadastro = tk.Tk()
    janela_cadastro.geometry("400x400")
    janela_cadastro.title("Cadastro")
    janela_cadastro.configure(bg="#195473")

    #valor do x para Login, Usuario, Senha
    valorx = 0.1
    valory = 0.25
    largcampo = .6

    #label da marca
    labelmarca = tk.Label(janela_cadastro, text="PROTESTE",foreground="#6BD4CD", width="30", height="5", font=("Tamoho", 20), bg="#195473")
    labelmarca.place(relx = valorx+.17, rely=valory-.23, relwidth=.50, relheight=.12)

    #label slogan
    labelslogan = tk.Label(janela_cadastro, text="Cadastro de Usuario",foreground="#6BD4CD", width="30", height="5", font=("Tamoho", 10), bg="#195473")
    labelslogan.place(relx = valorx+.24, rely=valory-.11, relwidth=.35, relheight=.05)


    #usuario

    labelusuario = tk.Label(janela_cadastro, text="Usuário:", fg="#6BD4CD", font=("Arial",12), bg="#195473")
    labelusuario.place(relx = valorx, rely=valory, relwidth=.15, relheight=.06)

    caixa_texto_usuario = tk.Text(janela_cadastro, width=5, height=5, bg="#6BD4CD")
    caixa_texto_usuario.place(relx = valorx+0.15, rely=valory, relwidth=largcampo, relheight=.06)

    #nome

    labelnome = tk.Label(janela_cadastro, text="Nome:", fg="#6BD4CD", font=("Arial",12), bg="#195473")
    labelnome.place(relx = valorx, rely=valory+.08, relwidth=.15, relheight=.06)

    caixa_texto_nome = tk.Text(janela_cadastro, width=5, height=5, bg="#6BD4CD")
    caixa_texto_nome.place(relx = valorx+0.15, rely=valory+.08, relwidth=largcampo, relheight=.06)

    #senha

    labelsenha = tk.Label(janela_cadastro, text="Senha:", fg="#6BD4CD", font=("Arial",12), bg="#195473")
    labelsenha.place(relx = valorx, rely=valory+.16, relwidth=.15, relheight=.06)

    caixa_texto_senha = tk.Text(janela_cadastro, width=5, height=5, bg="#6BD4CD")
    caixa_texto_senha.place(relx = valorx+0.15, rely=valory+.16, relwidth=largcampo, relheight=.06)

    #e-mail

    labelemail = tk.Label(janela_cadastro, text="E-mail:", fg="#6BD4CD", font=("Arial",12), bg="#195473")
    labelemail.place(relx = valorx, rely=valory+.24, relwidth=.15, relheight=.06)

    caixa_texto_email = tk.Text(janela_cadastro, width=5, height=5, bg="#6BD4CD")
    caixa_texto_email.place(relx = valorx+0.15, rely=valory+.24, relwidth=largcampo, relheight=.06)

    #cpf

    labelcpf = tk.Label(janela_cadastro, text="CPF:", fg="#6BD4CD", font=("Arial",12), bg="#195473")
    labelcpf.place(relx = valorx, rely=valory+.32, relwidth=.15, relheight=.06)

    caixa_texto_cpf = tk.Text(janela_cadastro, width=5, height=5, bg="#6BD4CD")
    caixa_texto_cpf.place(relx = valorx+0.15, rely=valory+.32, relwidth=largcampo, relheight=.06)

    #botão de salvar
    #criar função insert no banco
    botao_cadastrar = Button(janela_cadastro, text="Cadastrar", command="", width=10, height=5, bg="#6BD4CD")
    botao_cadastrar.place(relx = valorx+.2, rely=valory+.5, relwidth=.20, relheight=.06)

    #botão de fechar

    botao_acessar = Button(janela_cadastro, text="Fechar", command=janela_cadastro.destroy, width=10, height=5, bg="#6BD4CD")
    botao_acessar.place(relx = valorx+.50, rely=valory+.5, relwidth=.20, relheight=.06)

