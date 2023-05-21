import tkinter as tk
from tkinter import Button, PhotoImage, ttk
from tkinter import messagebox
import top_screen

def tela_07 ():

    tela_07 = tk.Tk()

    tela_07.title("Proteste")  # editar titulo
    tela_07.geometry("1200x700")
    tela_07.resizable(False, False)
    tela_07.configure(bg="#04345C")

    # valor do x para Login, Usuario, Senha
    valorx = 0.02
    valory = 0.02

    top_screen.top(tela_07)

    # botão de Próxima tela
    botao_anterior = Button(tela_07, text="<= Anterior", command="",
                            width=10, height=5, bg="#6BD4CD", fg="#000000", font=("Tamoho", 18))
    botao_anterior.place(relx=valorx, rely=valory+.11, relwidth=.15, relheight=.06)

    # botão de Anterior tela
    botao_proximo = Button(tela_07, text="Próximo =>", command="", width=10,
                        height=5, bg="#6BD4CD", fg="#000000", font=("Tamoho", 18))
    botao_proximo.place(relx=valorx+0.2, rely=valory+.11,
                        relwidth=.15, relheight=.06)


    # label do titulo da tela
    labeltitulo = tk.Label(tela_07, text="Recursos Humano", foreground="#000000",
                        width="30", height="5", font=("Tamoho", 18), bg="#6BD4CD")
    labeltitulo.place(relx=valorx+.1, rely=valory+.30, relwidth=.77, relheight=.05)

    # label do sub-titulo da tela
    labelsubtitulo_papel = tk.Label(tela_07, text="Papel:", foreground="#000000",
                                    width="30", height="5", font=("Tamoho", 14), bg="#6BD4CD")
    labelsubtitulo_papel.place(
        relx=valorx+.1, rely=valory+.37, relwidth=.26, relheight=.05)

    labelsubtitulo_recursos_minimos = tk.Label(
        tela_07, text="Recursos Mínimos:", foreground="#000000", width="30", height="5", font=("Tamoho", 14), bg="#6BD4CD")
    labelsubtitulo_recursos_minimos.place(
        relx=valorx+.38, rely=valory+.37, relwidth=.20, relheight=.05)

    labelsubtitulo_responsabilidade = tk.Label(tela_07, text="Responsabilidades Específicas:",
                                            foreground="#000000", width="30", height="5", font=("Tamoho", 14), bg="#6BD4CD")
    labelsubtitulo_responsabilidade.place(
        relx=valorx+.6, rely=valory+.37, relwidth=.27, relheight=.05)

    # caixas de texto da primeira linha
    caixa_texto_papel = tk.Text(
        tela_07, width=10, height=5, bg="#6BD4CD")
    caixa_texto_papel.place(relx=valorx+.1, rely=valory+.44,
                            relwidth=.26, relheight=.20)

    caixa_texto_recursos_minimos = tk.Text(
        tela_07, width=10, height=5, bg="#6BD4CD")
    caixa_texto_recursos_minimos.place(relx=valorx+.38, rely=valory+.44,
                                    relwidth=.20, relheight=.20)

    caixa_texto_responsabilidade = tk.Text(
        tela_07, width=10, height=5, bg="#6BD4CD")
    caixa_texto_responsabilidade.place(relx=valorx+.6, rely=valory+.44,
                                    relwidth=.27, relheight=.20)


    # label do segundo sub-titulo da tela
    labelsubtitulo_componentes_teste = tk.Label(tela_07, text="Componentes de Testes De Integração:",
                                                foreground="#000000", width="30", height="5", font=("Tamoho", 14), bg="#6BD4CD", wraplength=220)
    labelsubtitulo_componentes_teste.place(
        relx=valorx+.1, rely=valory+.66, relwidth=.26, relheight=.1)

    # caixas de texto da primeira linha
    caixa_texto_componentes_teste = tk.Text(
        tela_07, width=10, height=5, bg="#6BD4CD")
    caixa_texto_componentes_teste.place(relx=valorx+.38, rely=valory+.66,
                                        relwidth=.49, relheight=.25)

#tela_07.mainloop()  # mainloop = loop infinito para deixar a tela visivel
