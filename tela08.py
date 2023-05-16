import tkinter as tk
from tkinter import Button, PhotoImage, ttk
from tkinter import messagebox
import top_screen

# def tela_01 ():

tela_08 = tk.Tk()

tela_08.title("Proteste")  # editar titulo
tela_08.geometry("1200x700")
tela_08.resizable(False, False)
tela_08.configure(bg="#04345C")

# valor do x para Login, Usuario, Senha
valorx = 0.02
valory = 0.03

top_screen.top(tela_08)

# botão de Próxima tela
botao_anterior = Button(tela_08, text="<= Anterior", command="",
                        width=10, height=5, bg="#6BD4CD", fg="#000000", font=("Tamoho", 18))
botao_anterior.place(relx=valorx, rely=valory+.11, relwidth=.15, relheight=.06)

# botão de Anterior tela
botao_proximo = Button(tela_08, text="Próximo =>", command="", width=10,
                       height=5, bg="#6BD4CD", fg="#000000", font=("Tamoho", 18))
botao_proximo.place(relx=valorx+0.2, rely=valory+.11,
                    relwidth=.15, relheight=.06)


# label do titulo da tela
labeltitulo = tk.Label(tela_08, text="Relatórios", foreground="#000000",
                       width="30", height="5", font=("Tamoho", 18), bg="#6BD4CD")
labeltitulo.place(relx=valorx+.1, rely=valory+.30, relwidth=.77, relheight=.05)

# label do sub-titulo da tela
labelsubtitulo_tipo_relatorio = tk.Label(tela_08, text="Tipo de Relatório:", foreground="#000000",
                                         width="30", height="5", font=("Tamoho", 14), bg="#6BD4CD")
labelsubtitulo_tipo_relatorio.place(
    relx=valorx+.1, rely=valory+.37, relwidth=.15, relheight=.05)

labelsubtitulo_objetivos = tk.Label(
    tela_08, text="Objetivos:", foreground="#000000", width="30", height="5", font=("Tamoho", 14), bg="#6BD4CD")
labelsubtitulo_objetivos.place(
    relx=valorx+.26, rely=valory+.37, relwidth=.3, relheight=.05)

labelsubtitulo_destinatarios = tk.Label(tela_08, text="Destinatários:",
                                        foreground="#000000", width="30", height="5", font=("Tamoho", 14), bg="#6BD4CD")
labelsubtitulo_destinatarios.place(
    relx=valorx+.57, rely=valory+.37, relwidth=.15, relheight=.05)

labelsubtitulo_periodicidade = tk.Label(tela_08, text="Periodicidade:",
                                        foreground="#000000", width="30", height="5", font=("Tamoho", 14), bg="#6BD4CD")
labelsubtitulo_periodicidade.place(
    relx=valorx+.73, rely=valory+.37, relwidth=.14, relheight=.05)

# caixas de texto da primeira linha
caixa_texto_tipo_relatorio = tk.Text(
    tela_08, width=10, height=5, bg="#6BD4CD")
caixa_texto_tipo_relatorio.place(relx=valorx+.1, rely=valory+.44,
                                 relwidth=.15, relheight=.20)

caixa_texto_objetivos = tk.Text(
    tela_08, width=10, height=5, bg="#6BD4CD")
caixa_texto_objetivos.place(relx=valorx+.26, rely=valory+.44,
                            relwidth=.3, relheight=.20)

caixa_texto_destinatarios = tk.Text(
    tela_08, width=10, height=5, bg="#6BD4CD")
caixa_texto_destinatarios.place(relx=valorx+.57, rely=valory+.44,
                                relwidth=.15, relheight=.20)

caixa_texto_periodicidade = tk.Text(
    tela_08, width=10, height=5, bg="#6BD4CD")
caixa_texto_periodicidade.place(relx=valorx+.73, rely=valory+.44,
                                relwidth=.14, relheight=.20)

# caixas de texto da segunda linha
caixa_texto_tipo_relatorio_2 = tk.Text(
    tela_08, width=10, height=5, bg="#6BD4CD")
caixa_texto_tipo_relatorio_2.place(relx=valorx+.1, rely=valory+.66,
                                   relwidth=.15, relheight=.20)

caixa_texto_objetivos_2 = tk.Text(
    tela_08, width=10, height=5, bg="#6BD4CD")
caixa_texto_objetivos_2.place(relx=valorx+.26, rely=valory+.66,
                              relwidth=.3, relheight=.20)

caixa_texto_destinatarios_2 = tk.Text(
    tela_08, width=10, height=5, bg="#6BD4CD")
caixa_texto_destinatarios_2.place(relx=valorx+.57, rely=valory+.66,
                                  relwidth=.15, relheight=.20)

caixa_texto_periodicidade_2 = tk.Text(
    tela_08, width=10, height=5, bg="#6BD4CD")
caixa_texto_periodicidade_2.place(relx=valorx+.73, rely=valory+.66,
                                  relwidth=.14, relheight=.20)

tela_08.mainloop()  # mainloop = loop infinito para deixar a tela visivel
