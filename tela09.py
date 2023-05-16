import tkinter as tk
from tkinter import Button, PhotoImage, ttk
from tkinter import messagebox
import top_screen

# def tela_01 ():

tela_09 = tk.Tk()

tela_09.title("Proteste")  # editar titulo
tela_09.geometry("1200x700")
tela_09.resizable(False, False)
tela_09.configure(bg="#04345C")

# valor do x para Login, Usuario, Senha
valorx = 0.02
valory = 0.03

# parte superior da tela
top_screen.top(tela_09)

# botão de Próxima tela
botao_anterior = Button(tela_09, text="<= Anterior", command="",
                        width=10, height=5, bg="#6BD4CD", fg="#000000", font=("Tamoho", 18))
botao_anterior.place(relx=valorx, rely=valory+.1, relwidth=.15, relheight=.06)

# botão de Anterior tela
botao_proximo = Button(tela_09, text="Próximo =>", command="", width=10,
                       height=5, bg="#6BD4CD", fg="#000000", font=("Tamoho", 18))
botao_proximo.place(relx=valorx+0.2, rely=valory+.1,
                    relwidth=.15, relheight=.06)

# label do meio da tela - Marcos:
label_marcos = tk.Label(tela_09, text="Marcos:", foreground="#000000",
                           width="10", height="5", font=("Tamoho", 12), bg="#6BD4CD")
label_marcos.place(relx=valorx+.1, rely=valory+.30,
                      relwidth=.20, relheight=.05)

# caixas de texto para os Marcos:
caixa_texto_marcos = tk.Text(
    tela_09, width=10, height=5, bg="#6BD4CD")
caixa_texto_marcos.place(relx=valorx+.32, rely=valory+.30,
                                         relwidth=.55, relheight=.28)

# label do meio da tela - Riscos:
label_riscos = tk.Label(tela_09, text="Riscos:", foreground="#000000",
                            width="10", height="5", font=("Tamoho", 12), bg="#6BD4CD")
label_riscos.place(relx=valorx+.1, rely=valory+.60,
                       relwidth=.20, relheight=.05)

# caixas de texto para as Riscos:
caixa_texto_riscos = tk.Text(
    tela_09, width=10, height=5, bg="#6BD4CD")
caixa_texto_riscos.place(relx=valorx+.32, rely=valory+.60,
                                         relwidth=.55, relheight=.28)

tela_09.mainloop()  # mainloop = loop infinito para deixar a tela visivel
