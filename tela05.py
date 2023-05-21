import tkinter as tk
from tkinter import Button, PhotoImage, ttk
from tkinter import messagebox
import top_screen

def tela_05 ():

    tela_05 = tk.Tk()

    tela_05.title("Proteste")  # editar titulo
    tela_05.geometry("1200x700")
    tela_05.resizable(False, False)
    tela_05.configure(bg="#04345C")

    # valor do x para Login, Usuario, Senha
    valorx = 0.02
    valory = 0.03

    # parte superior da tela
    top_screen.top(tela_05)

    # botão de Próxima tela
    botao_anterior = Button(tela_05, text="<= Anterior", command="",
                            width=10, height=5, bg="#6BD4CD", fg="#000000", font=("Tamoho", 18))
    botao_anterior.place(relx=valorx, rely=valory+.1, relwidth=.15, relheight=.06)

    # botão de Anterior tela
    botao_proximo = Button(tela_05, text="Próximo =>", command="", width=10,
                        height=5, bg="#6BD4CD", fg="#000000", font=("Tamoho", 18))
    botao_proximo.place(relx=valorx+0.2, rely=valory+.1,
                        relwidth=.15, relheight=.06)

    # label do meio da tela - Abordagem de testes:
    label_abordagem_testes = tk.Label(tela_05, text="Abordagem de testes:", foreground="#000000",
                            width="10", height="5", font=("Tamoho", 12), bg="#6BD4CD")
    label_abordagem_testes.place(relx=valorx+.1, rely=valory+.30,
                        relwidth=.20, relheight=.05)

    # caixas de texto para as Abordagem de testes:
    caixa_texto_abordagem_testes = tk.Text(
        tela_05, width=10, height=5, bg="#6BD4CD")
    caixa_texto_abordagem_testes.place(relx=valorx+.32, rely=valory+.30,
                                            relwidth=.55, relheight=.28)

    # label do meio da tela - Artefatos de saída:
    label_artefatos_saida = tk.Label(tela_05, text="Artefatos de saída:", foreground="#000000",
                                width="10", height="5", font=("Tamoho", 12), bg="#6BD4CD")
    label_artefatos_saida.place(relx=valorx+.1, rely=valory+.60,
                        relwidth=.20, relheight=.05)

    # caixas de texto para as Artefatos de saída:
    caixa_texto_artefatos_saida = tk.Text(
        tela_05, width=10, height=5, bg="#6BD4CD")
    caixa_texto_artefatos_saida.place(relx=valorx+.32, rely=valory+.60,
                                            relwidth=.55, relheight=.28)

#tela_05.mainloop()  # mainloop = loop infinito para deixar a tela visivel
