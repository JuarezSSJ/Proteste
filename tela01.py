import tkinter as tk
from tkinter import Button, PhotoImage, ttk
from tkinter import messagebox
import top_screen, tela02

def tela_01 ():

    tela_01 = tk.Tk()

    tela_01.title("Proteste")  # editar titulo
    tela_01.geometry("1200x700")
    tela_01.resizable(False, False)
    tela_01.configure(bg="#04345C")

    #valor do x para Login, Usuario, Senha
    valorx = 0.02
    valory = 0.03

    top_screen.top(tela_01)

    #botão de Novo plano
    botao_novo_plano = Button(tela_01, text="Novo Plano", command="", width=10, height=5, bg="#6BD4CD", fg="#000000", font=("Tamoho", 18))
    botao_novo_plano.place(relx = valorx, rely=valory+.09, relwidth=.15, relheight=.06)

    #botão Editar plano
    botao_editar_plano = Button(tela_01, text="Editar Plano", command="", width=10, height=5, bg="#6BD4CD", fg="#000000", font=("Tamoho", 18))
    botao_editar_plano.place(relx = valorx+0.2, rely=valory+.09, relwidth=.15, relheight=.06)

    #botão de proxima tela
    botao_anterior = Button(tela_01, text="<= Anterior", command="", width=10, height=5, bg="#6BD4CD", fg="#000000", font=("Tamoho", 16))
    botao_anterior.place(relx = valorx, rely=valory+.16, relwidth=.15, relheight=.06)

    #botão de tela anterior
    botao_proximo = Button(tela_01, text="Próxima =>", command=tela02.tela_02, width=10, height=5, bg="#6BD4CD", fg="#000000", font=("Tamoho", 16))
    botao_proximo.place(relx = valorx+0.2, rely=valory+.16, relwidth=.15, relheight=.06)

    #label do sub-titulo da tela
    labelsubtitulo = tk.Label(tela_01, text="Planos de Testes",foreground="#000000", width="30", height="5", font=("Tamoho", 18), bg="#6BD4CD")
    labelsubtitulo.place(relx = valorx+.1, rely=valory+.30, relwidth=.77, relheight=.05)

    #label dos planos na tela
    labelgrade = tk.Label(tela_01, text="",foreground="#000000", width="30", height="5", font=("Tamoho", 18), bg="#6BD4CD")
    labelgrade.place(relx = valorx+.1, rely=valory+.38, relwidth=.77, relheight=.5)



#tela_01.mainloop()  # mainloop = loop infinito para deixar a tela visivel