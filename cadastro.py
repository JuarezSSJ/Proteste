import tkinter as tk
from tkinter import Button, PhotoImage, ttk
from tkinter import messagebox
from view import *



def cadastro(caixa_texto_usuario, caixa_texto_nome, caixa_texto_senha, caixa_texto_email, caixa_texto_cpf):
    tabela = "tb_login"
    usuario = caixa_texto_usuario.get("1.0", "end-1c")
    nome = caixa_texto_nome.get("1.0", "end-1c")
    senha = caixa_texto_senha.get("1.0", "end-1c")
    email = caixa_texto_email.get("1.0", "end-1c")
    cpf = caixa_texto_cpf.get("1.0", "end-1c")

    lista_campos = tb_login_vars
    #['nome', 'cpf', 'email', 'login', 'senha']
    lista_campos_preenchidos = [nome, cpf, email, usuario, senha]

    if cpf == " " and usuario == " ":
        messagebox.showerror('Erro', 'Possui campo obrigatorio vazio')
    else:
        cadastrar_info(tabela, lista_campos, lista_campos_preenchidos)
        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')
        caixa_texto_usuario.delete('1.0', 'end')
        caixa_texto_nome.delete('1.0', 'end')
        caixa_texto_senha.delete('1.0', 'end')
        caixa_texto_email.delete('1.0', 'end')
        caixa_texto_cpf.delete('1.0', 'end')
    novo_cadastro.destroy()


def novo_cadastro():
    janela_cadastro = tk.Tk()
    janela_cadastro.geometry("400x400")
    janela_cadastro.title("Cadastro")
    janela_cadastro.configure(bg="#195473")

    # valor do x para Login, Usuario, Senha
    valorx = 0.1
    valory = 0.25
    largcampo = .6

    # label da marca
    labelmarca = tk.Label(janela_cadastro, text="PROTESTE", foreground="#6BD4CD",
                          width="30", height="5", font=("Tamoho", 20), bg="#195473")
    labelmarca.place(relx=valorx+.17, rely=valory-.23,
                     relwidth=.50, relheight=.12)

    # label slogan
    labelslogan = tk.Label(janela_cadastro, text="Cadastro de Usuario",
                           foreground="#6BD4CD", width="30", height="5", font=("Tamoho", 10), bg="#195473")
    labelslogan.place(relx=valorx+.24, rely=valory-.11,
                      relwidth=.35, relheight=.05)

    # usuario

    labelusuario = tk.Label(janela_cadastro, text="Usuário:",
                            fg="#6BD4CD", font=("Arial", 12), bg="#195473")
    labelusuario.place(relx=valorx, rely=valory, relwidth=.15, relheight=.06)

    caixa_texto_usuario = tk.Text(
        janela_cadastro, width=5, height=5, bg="#6BD4CD",wrap="none",font=("Arial", 12))
    caixa_texto_usuario.place(
        relx=valorx+0.15, rely=valory, relwidth=largcampo, relheight=.06)

    # nome

    labelnome = tk.Label(janela_cadastro, text="Nome:",
                         fg="#6BD4CD", font=("Arial", 12), bg="#195473")
    labelnome.place(relx=valorx, rely=valory+.08, relwidth=.15, relheight=.06)

    caixa_texto_nome = tk.Text(
        janela_cadastro, width=5, height=5, bg="#6BD4CD")
    caixa_texto_nome.place(relx=valorx+0.15, rely=valory+.08,
                           relwidth=largcampo, relheight=.06)

    # senha

    labelsenha = tk.Label(janela_cadastro, text="Senha:",
                          fg="#6BD4CD", font=("Arial", 12), bg="#195473")
    labelsenha.place(relx=valorx, rely=valory+.16, relwidth=.15, relheight=.06)

    caixa_texto_senha = tk.Text(
        janela_cadastro, width=5, height=5, bg="#6BD4CD")
    caixa_texto_senha.place(relx=valorx+0.15, rely=valory+.16,
                            relwidth=largcampo, relheight=.06)

    # e-mail

    labelemail = tk.Label(janela_cadastro, text="E-mail:",
                          fg="#6BD4CD", font=("Arial", 12), bg="#195473")
    labelemail.place(relx=valorx, rely=valory+.24, relwidth=.15, relheight=.06)

    caixa_texto_email = tk.Text(
        janela_cadastro, width=5, height=5, bg="#6BD4CD")
    caixa_texto_email.place(relx=valorx+0.15, rely=valory+.24,
                            relwidth=largcampo, relheight=.06)

    # cpf

    labelcpf = tk.Label(janela_cadastro, text="CPF:",
                        fg="#6BD4CD", font=("Arial", 12), bg="#195473")
    labelcpf.place(relx=valorx, rely=valory+.32, relwidth=.15, relheight=.06)

    caixa_texto_cpf = tk.Text(janela_cadastro, width=5, height=5, bg="#6BD4CD")
    caixa_texto_cpf.place(relx=valorx+0.15, rely=valory+.32,
                          relwidth=largcampo, relheight=.06)

    # botão de salvar
    # criar função insert no banco
    botao_cadastrar = Button(janela_cadastro, text="Cadastrar",
                             command=lambda: cadastro(caixa_texto_usuario, caixa_texto_nome, caixa_texto_senha, caixa_texto_email, caixa_texto_cpf), 
                             width=10, height=5, bg="#6BD4CD")
    botao_cadastrar.place(relx=valorx+.2, rely=valory+.5,
                          relwidth=.20, relheight=.06)

    # botão de fechar

    botao_acessar = Button(janela_cadastro, text="Fechar",
                           command=janela_cadastro.destroy, width=10, height=5, bg="#6BD4CD")
    botao_acessar.place(relx=valorx+.50, rely=valory+.5,
                        relwidth=.20, relheight=.06)
