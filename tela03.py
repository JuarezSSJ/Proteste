import tkinter as tk
from tkinter import Button, PhotoImage, ttk
from tkinter import messagebox
import top_screen, tela04

def tela_03 ():

    tela_03 = tk.Tk()

    tela_03.title("Proteste")  # editar titulo
    tela_03.geometry("1200x700")
    tela_03.resizable(False, False)
    tela_03.configure(bg="#04345C")

    # valor do x para Login, Usuario, Senha
    valorx = 0.02
    valory = 0.03

    # parte superior da tela
    top_screen.top(tela_03)

    # botão de Próxima tela
    botao_anterior = Button(tela_03, text="<= Anterior", command="",
                            width=10, height=5, bg="#6BD4CD", fg="#000000", font=("Tamoho", 18))
    botao_anterior.place(relx=valorx, rely=valory+.1, relwidth=.15, relheight=.06)

    # botão de Anterior tela
    botao_proximo = Button(tela_03, text="Próximo =>", command=tela04.tela_04, width=10,
                        height=5, bg="#6BD4CD", fg="#000000", font=("Tamoho", 18))
    botao_proximo.place(relx=valorx+0.2, rely=valory+.1,
                        relwidth=.15, relheight=.06)

    # label do meio da tela - Itens de Teste:
    label_projetos = tk.Label(tela_03, text="Itens de Teste:", foreground="#000000",
                            width="10", height="5", font=("Tamoho", 12), bg="#6BD4CD")
    label_projetos.place(relx=valorx+.1, rely=valory+.30,
                        relwidth=.20, relheight=.05)

    # label do meio da tela - Fase de desenvolvimento
    label_fase_desenvolvimento = tk.Label(tela_03, text="Fase de desenvolvimento", foreground="#000000",
                                        width="10", height="5", font=("Tamoho", 12), bg="#6BD4CD")
    label_fase_desenvolvimento.place(relx=valorx+.32, rely=valory+.30,
                                    relwidth=.25, relheight=.05)

    # label do meio da tela - Caso de teste
    label_caso_teste = tk.Label(tela_03, text="Caso de teste", foreground="#000000",
                                width="10", height="5", font=("Tamoho", 12), bg="#6BD4CD")
    label_caso_teste.place(relx=valorx+.6, rely=valory+.30,
                        relwidth=.25, relheight=.05)


    # caixas de texto para as Fases de desenvolvimento
    caixa_texto_fase_desenvolvimento_1 = tk.Text(
        tela_03, width=10, height=5, bg="#6BD4CD")
    caixa_texto_fase_desenvolvimento_1.place(relx=valorx+.32, rely=valory+.36,
                                            relwidth=.25, relheight=.18)
    caixa_texto_fase_desenvolvimento_2 = tk.Text(
        tela_03, width=10, height=5, bg="#6BD4CD")
    caixa_texto_fase_desenvolvimento_2.place(relx=valorx+.32, rely=valory+.55,
                                            relwidth=.25, relheight=.18)

    caixa_texto_fase_desenvolvimento_3 = tk.Text(
        tela_03, width=10, height=5, bg="#6BD4CD")
    caixa_texto_fase_desenvolvimento_3.place(relx=valorx+.32, rely=valory+.74,
                                            relwidth=.25, relheight=.18)


    # botões para cadastrar os casos de teste - abrirá uma caixa para cadastro - falta criar o formulario
    botao_caso_teste_1 = Button(tela_03, text="<= Cadastro Caso de Teste", command="", width=10,
                                height=5, bg="#6BD4CD", fg="#000000", font=("Tamoho", 14))
    botao_caso_teste_1.place(relx=valorx+0.6, rely=valory+.42,
                            relwidth=.25, relheight=.06)

    botao_caso_teste_2 = Button(tela_03, text="<= Cadastro Caso de Teste", command="", width=10,
                                height=5, bg="#6BD4CD", fg="#000000", font=("Tamoho", 14))
    botao_caso_teste_2.place(relx=valorx+0.6, rely=valory+.61,
                            relwidth=.25, relheight=.06)

    botao_caso_teste_3 = Button(tela_03, text="<= Cadastro Caso de Teste", command="", width=10,
                                height=5, bg="#6BD4CD", fg="#000000", font=("Tamoho", 14))
    botao_caso_teste_3.place(relx=valorx+0.6, rely=valory+.8,
                            relwidth=.25, relheight=.06)

#tela_03.mainloop()  # mainloop = loop infinito para deixar a tela visivel
