import tkinter as tk
from tkinter import Button, PhotoImage, ttk
from tkinter import messagebox
from view import *

"""
def esqueci_usuario_senha(caixa_texto_email, caixa_texto_cpf):
    email = caixa_texto_email.get("1.0", "end-1c")
    cpf = caixa_texto_cpf.get("1.0", "end-1c")
    print(email, cpf)
    print(esqueci_senha(email, cpf))
    verificar = esqueci_senha(email, cpf)
    if verificar == True:
        messagebox.showinfo("Sucesso!", "Verificar caixa de e-mail")
        
    else:
        messagebox.showerror("Erro", "E-mail ou CPF incorreto!")
"""

class JanelaEsqueciSenha(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")
        self.title("Recuperar Senha")
        self.configure(bg="#195473")
        #valor do x para Login, Usuario, Senha
        valorx = 0.1
        valory = 0.25
        largcampo = .6

        #label da marca
        labelmarca = tk.Label(self, text="PROTESTE",foreground="#6BD4CD", width="30", height="5", font=("Tamoho", 20), bg="#195473")
        labelmarca.place(relx = valorx+.17, rely=valory-.23, relwidth=.50, relheight=.12)

        #label slogan
        labelslogan = tk.Label(self, text="Recuperar Senha",foreground="#6BD4CD", width="30", height="5", font=("Tamoho", 10), bg="#195473")
        labelslogan.place(relx = valorx+.24, rely=valory-.11, relwidth=.35, relheight=.05)

        #e-mail

        labelemail = tk.Label(self, text="E-mail:", fg="#6BD4CD", font=("Arial",12), bg="#195473")
        labelemail.place(relx = valorx, rely=valory+.10, relwidth=.15, relheight=.06)

        self.caixa_texto_email = tk.Text(self, width=5, height=5, bg="#6BD4CD")
        self.caixa_texto_email.place(relx = valorx+0.15, rely=valory+.10, relwidth=largcampo, relheight=.06)

        #cpf

        labelcpf = tk.Label(self, text="CPF:", fg="#6BD4CD", font=("Arial",12), bg="#195473")
        labelcpf.place(relx = valorx, rely=valory+.24, relwidth=.15, relheight=.06)

        self.caixa_texto_cpf = tk.Text(self, width=5, height=5, bg="#6BD4CD")
        self.caixa_texto_cpf.place(relx = valorx+0.15, rely=valory+.24, relwidth=largcampo, relheight=.06)


        # botão de salvar
        botao_acessar = Button(self, text="Recuperar", command=self.esqueci_usuario_senha, width=10, height=8, bg="#6BD4CD")
        botao_acessar.place(relx=valorx + .2, rely=valory + .4, relwidth=.20, relheight=.1)

        # botão de fechar
        botao_fechar = Button(self, text="Fechar", command=self.destroy, width=10, height=8, bg="#6BD4CD")
        botao_fechar.place(relx=valorx + .50, rely=valory + .4, relwidth=.20, relheight=.1)

    def esqueci_usuario_senha(self):
        email = self.caixa_texto_email.get("1.0", "end-1c")
        cpf = self.caixa_texto_cpf.get("1.0", "end-1c")
        verificar = esqueci_senha(email, cpf)
        if verificar:
            messagebox.showinfo("Sucesso!", "Verificar caixa de e-mail")
            self.destroy()
        else:
            messagebox.showerror("Erro", "E-mail ou CPF incorreto!")

def esqueci_a_senha():
    janela_esqueci_senha = JanelaEsqueciSenha()
    janela_esqueci_senha.mainloop()