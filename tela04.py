import tkinter as tk
from tkinter import Button, PhotoImage, ttk
from tkinter import messagebox
import top_screen

# def tela_01 ():

tela_04 = tk.Tk()

tela_04.title("Proteste")  # editar titulo
tela_04.geometry("1200x700")
tela_04.resizable(False, False)
tela_04.configure(bg="#04345C")

# valor do x para Login, Usuario, Senha
valorx = 0.02
valory = 0.03

# parte superior da tela
top_screen.top(tela_04)

# botão de Próxima tela
botao_anterior = Button(tela_04, text="<= Anterior", command="",
                        width=10, height=5, bg="#6BD4CD", fg="#000000", font=("Tamoho", 18))
botao_anterior.place(relx=valorx, rely=valory+.1, relwidth=.15, relheight=.06)

# botão de Anterior tela
botao_proximo = Button(tela_04, text="Próximo =>", command="", width=10,
                       height=5, bg="#6BD4CD", fg="#000000", font=("Tamoho", 18))
botao_proximo.place(relx=valorx+0.2, rely=valory+.1,
                    relwidth=.15, relheight=.06)

# label do meio da tela - Premissas:
label_premissas = tk.Label(tela_04, text="Premissas:", foreground="#000000",
                           width="10", height="5", font=("Tamoho", 12), bg="#6BD4CD")
label_premissas.place(relx=valorx+.1, rely=valory+.30,
                      relwidth=.20, relheight=.05)

# caixas de texto para as Premissas:
caixa_texto_premissas = tk.Text(
    tela_04, width=10, height=5, bg="#6BD4CD")
caixa_texto_premissas.place(relx=valorx+.32, rely=valory+.30,
                                         relwidth=.55, relheight=.28)

# label do meio da tela - Restrições:
label_restricoes = tk.Label(tela_04, text="Restrições:", foreground="#000000",
                            width="10", height="5", font=("Tamoho", 12), bg="#6BD4CD")
label_restricoes.place(relx=valorx+.1, rely=valory+.60,
                       relwidth=.20, relheight=.05)

# caixas de texto para as Restrições:
caixa_texto_restricoes = tk.Text(
    tela_04, width=10, height=5, bg="#6BD4CD")
caixa_texto_restricoes.place(relx=valorx+.32, rely=valory+.60,
                                         relwidth=.55, relheight=.28)

tela_04.mainloop()  # mainloop = loop infinito para deixar a tela visivel
