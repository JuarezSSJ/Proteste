import tkinter as tk
from tkinter import Button, PhotoImage, ttk
from tkinter import messagebox
import top_screen, tela03

def tela_02 ():

    tela_02 = tk.Tk()

    tela_02.title("Proteste")  # editar titulo
    tela_02.geometry("1200x700")
    tela_02.resizable(False, False)
    tela_02.configure(bg="#04345C")

    # valor do x para Login, Usuario, Senha
    valorx = 0.02
    valory = 0.03

    # parte superior da tela
    top_screen.top(tela_02)

    # botão de Anterior tela
    botao_anterior = Button(tela_02, text="<= Anterior", command="",
                            width=10, height=5, bg="#6BD4CD", fg="#000000", font=("Tamoho", 18))
    botao_anterior.place(relx=valorx, rely=valory+.1, relwidth=.15, relheight=.06)

    # botão de  tela Próxima
    botao_proximo = Button(tela_02, text="Próximo =>", command=tela03.tela_03, width=10,
                        height=5, bg="#6BD4CD", fg="#000000", font=("Tamoho", 18))
    botao_proximo.place(relx=valorx+0.2, rely=valory+.1,
                        relwidth=.15, relheight=.06)

    # label do meio da tela - projetos:
    label_projetos = tk.Label(tela_02, text="Projetos:", foreground="#000000",
                            width="10", height="5", font=("Tamoho", 12), bg="#6BD4CD")
    label_projetos.place(relx=valorx+.1, rely=valory+.30,
                        relwidth=.15, relheight=.05)

    caixa_texto_projetos = tk.Text(width=10, height=5, bg="#6BD4CD")
    caixa_texto_projetos.place(relx=valorx+.27, rely=valory+.30,
                        relwidth=.60, relheight=.05)

    # label do meio da tela - Requisitante:
    label_requisitante = tk.Label(tela_02, text="Requisitante:", foreground="#000000",
                            width="10", height="5", font=("Tamoho", 12), bg="#6BD4CD")
    label_requisitante.place(relx=valorx+.1, rely=valory+.39,
                        relwidth=.15, relheight=.05)

    caixa_texto_requisitante = tk.Text(width=10, height=5, bg="#6BD4CD")
    caixa_texto_requisitante.place(relx=valorx+.27, rely=valory+.39,
                        relwidth=.60, relheight=.05)

    # label do meio da tela - Gerente de Projetos:
    label_gerente_pj = tk.Label(tela_02, text="Gerente de Projetos:", foreground="#000000",
                            width="10", height="5", font=("Tamoho", 12), bg="#6BD4CD")
    label_gerente_pj.place(relx=valorx+.1, rely=valory+.48,
                        relwidth=.15, relheight=.05)

    caixa_texto_gerente_pj = tk.Text(width=10, height=5, bg="#6BD4CD")
    caixa_texto_gerente_pj.place(relx=valorx+.27, rely=valory+.48,
                        relwidth=.60, relheight=.05)

    # label do meio da tela - Cenário Operacional:
    label_cenario_Op = tk.Label(tela_02, text="Cenário Operacional:", foreground="#000000",
                            width="10", height="5", font=("Tamoho", 12), bg="#6BD4CD")
    label_cenario_Op.place(relx=valorx+.1, rely=valory+.57,
                        relwidth=.15, relheight=.05)

    caixa_texto_cenario_Op = tk.Text(width=10, height=5, bg="#6BD4CD")
    caixa_texto_cenario_Op.place(relx=valorx+.27, rely=valory+.57,
                        relwidth=.60, relheight=.31)



#tela_02.mainloop()  # mainloop = loop infinito para deixar a tela visivel
