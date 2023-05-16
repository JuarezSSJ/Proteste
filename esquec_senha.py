import tkinter as tk
from tkinter import Button, PhotoImage, ttk
from tkinter import messagebox

def esqueci_senha():
    janela_esqueci_senha = tk.Tk()
    janela_esqueci_senha.geometry("400x300")
    janela_esqueci_senha.title("Recuperar Senha")
    janela_esqueci_senha.configure(bg="#195473")

    #valor do x para Login, Usuario, Senha
    valorx = 0.1
    valory = 0.25
    largcampo = .6

    #label da marca
    labelmarca = tk.Label(janela_esqueci_senha, text="PROTESTE",foreground="#6BD4CD", width="30", height="5", font=("Tamoho", 20), bg="#195473")
    labelmarca.place(relx = valorx+.17, rely=valory-.23, relwidth=.50, relheight=.12)

    #label slogan
    labelslogan = tk.Label(janela_esqueci_senha, text="Recuperar Senha",foreground="#6BD4CD", width="30", height="5", font=("Tamoho", 10), bg="#195473")
    labelslogan.place(relx = valorx+.24, rely=valory-.11, relwidth=.35, relheight=.05)

    #e-mail

    labelemail = tk.Label(janela_esqueci_senha, text="E-mail:", fg="#6BD4CD", font=("Arial",12), bg="#195473")
    labelemail.place(relx = valorx, rely=valory+.10, relwidth=.15, relheight=.06)

    caixa_texto_email = tk.Text(janela_esqueci_senha, width=5, height=5, bg="#6BD4CD")
    caixa_texto_email.place(relx = valorx+0.15, rely=valory+.10, relwidth=largcampo, relheight=.06)

    #cpf

    labelcpf = tk.Label(janela_esqueci_senha, text="CPF:", fg="#6BD4CD", font=("Arial",12), bg="#195473")
    labelcpf.place(relx = valorx, rely=valory+.24, relwidth=.15, relheight=.06)

    caixa_texto_cpf = tk.Text(janela_esqueci_senha, width=5, height=5, bg="#6BD4CD")
    caixa_texto_cpf.place(relx = valorx+0.15, rely=valory+.24, relwidth=largcampo, relheight=.06)

    #botão de salvar
    #criar função insert no banco
    botao_acessar = Button(janela_esqueci_senha, text="Recuperar", command="", width=10, height=8, bg="#6BD4CD")
    botao_acessar.place(relx = valorx+.2, rely=valory+.4, relwidth=.20, relheight=.1)

    #botão de fechar

    botao_fechar = Button(janela_esqueci_senha, text="Fechar", command=janela_esqueci_senha.destroy, width=10, height=8, bg="#6BD4CD")
    botao_fechar.place(relx = valorx+.50, rely=valory+.4, relwidth=.20, relheight=.1)
