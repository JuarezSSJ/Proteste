import tkinter as tk
from tkinter import Button

def top(tela_01):

    valorx = 0.02
    valory = 0.03

    #label da marca
    labelmarca = tk.Label(tela_01, text="PROTESTE",foreground="#6BD4CD", width="30", height="5", font=("Tamoho", 24), bg="#04345C")
    labelmarca.place(relx = valorx+.79, rely=valory+.05, relwidth=.15, relheight=.05)

    #label slogan
    labelslogan = tk.Label(tela_01, text="SOFTWARE DE TESTE",foreground="#6BD4CD", width="30", height="5", font=("Tamoho", 10), bg="#04345C")
    labelslogan.place(relx = valorx+.8, rely=valory+.1, relwidth=.13, relheight=.05)

    #label do titulo da tela
    labelmarca = tk.Label(tela_01, text="PLANOS DE TESTES",foreground="#000000", width="30", height="5", font=("Tamoho", 18), bg="#6BD4CD")
    labelmarca.place(relx = valorx+.025, rely=valory+.02, relwidth=.3, relheight=.05)

    #label dos planos de fundo tela
    labelplano_fundo = tk.Label(tela_01, text="",foreground="#000000", width="30", height="5", font=("Tamoho", 18), bg="#195473")
    labelplano_fundo.place(relx = valorx+.05, rely=valory+.24, relwidth=.85, relheight=.7)

