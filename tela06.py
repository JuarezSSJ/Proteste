import tkinter as tk
from tkinter import Button, PhotoImage, ttk
from tkinter import messagebox
import top_screen

#def tela_01 ():

tela_06 = tk.Tk()

tela_06.title("Proteste")  # editar titulo
tela_06.geometry("1200x700")
tela_06.resizable(False, False)
tela_06.configure(bg="#04345C")

#valor do x para Login, Usuario, Senha
valorx = 0.02
valory = 0.02

top_screen.top(tela_06)

# botão de Próxima tela
botao_anterior = Button(tela_06, text="<= Anterior", command="",
                        width=10, height=5, bg="#6BD4CD", fg="#000000", font=("Tamoho", 18))
botao_anterior.place(relx=valorx, rely=valory+.11, relwidth=.15, relheight=.06)

# botão de Anterior tela
botao_proximo = Button(tela_06, text="Próximo =>", command="", width=10,
                       height=5, bg="#6BD4CD", fg="#000000", font=("Tamoho", 18))
botao_proximo.place(relx=valorx+0.2, rely=valory+.11,
                    relwidth=.15, relheight=.06)


#label do titulo da tela
labeltitulo = tk.Label(tela_06, text="Recursos",foreground="#000000", width="30", height="5", font=("Tamoho", 18), bg="#6BD4CD")
labeltitulo.place(relx = valorx+.1, rely=valory+.30, relwidth=.77, relheight=.05)

#label do sub-titulo da tela
labelsubtitulo_hardware = tk.Label(tela_06, text="Hardware:",foreground="#000000", width="30", height="5", font=("Tamoho", 18), bg="#6BD4CD")
labelsubtitulo_hardware.place(relx = valorx+.1, rely=valory+.37, relwidth=.26, relheight=.05)

labelsubtitulo_quantidade = tk.Label(tela_06, text="Quantidade:",foreground="#000000", width="30", height="5", font=("Tamoho", 18), bg="#6BD4CD")
labelsubtitulo_quantidade.place(relx = valorx+.38, rely=valory+.37, relwidth=.20, relheight=.05)

labelsubtitulo_descricao = tk.Label(tela_06, text="Descrição:",foreground="#000000", width="30", height="5", font=("Tamoho", 18), bg="#6BD4CD")
labelsubtitulo_descricao.place(relx = valorx+.6, rely=valory+.37, relwidth=.27, relheight=.05)

#caixas de texto da primeira linha
caixa_texto_hardware = tk.Text(
    tela_06, width=10, height=5, bg="#6BD4CD")
caixa_texto_hardware.place(relx=valorx+.1, rely=valory+.44,
                                         relwidth=.26, relheight=.20)

caixa_texto_quantidade = tk.Text(
    tela_06, width=10, height=5, bg="#6BD4CD")
caixa_texto_quantidade.place(relx=valorx+.38, rely=valory+.44,
                                         relwidth=.20, relheight=.20)

caixa_texto_descricao = tk.Text(
    tela_06, width=10, height=5, bg="#6BD4CD")
caixa_texto_descricao.place(relx=valorx+.6, rely=valory+.44,
                                         relwidth=.27, relheight=.20)


#label do segundo sub-titulo da tela
labelsubtitulo_software = tk.Label(tela_06, text="Software:",foreground="#000000", width="30", height="5", font=("Tamoho", 18), bg="#6BD4CD")
labelsubtitulo_software.place(relx = valorx+.1, rely=valory+.66, relwidth=.26, relheight=.05)

labelsubtitulo_quantidade_2 = tk.Label(tela_06, text="Quantidade:",foreground="#000000", width="30", height="5", font=("Tamoho", 18), bg="#6BD4CD")
labelsubtitulo_quantidade_2.place(relx = valorx+.38, rely=valory+.66, relwidth=.20, relheight=.05)

labelsubtitulo_descricao_2 = tk.Label(tela_06, text="Descrição:",foreground="#000000", width="30", height="5", font=("Tamoho", 18), bg="#6BD4CD")
labelsubtitulo_descricao_2.place(relx = valorx+.6, rely=valory+.66, relwidth=.27, relheight=.05)

#caixas de texto da primeira linha
caixa_texto_software = tk.Text(
    tela_06, width=10, height=5, bg="#6BD4CD")
caixa_texto_software.place(relx=valorx+.1, rely=valory+.73,
                                         relwidth=.26, relheight=.20)

caixa_texto_quantidade_2 = tk.Text(
    tela_06, width=10, height=5, bg="#6BD4CD")
caixa_texto_quantidade_2.place(relx=valorx+.38, rely=valory+.73,
                                         relwidth=.20, relheight=.20)

caixa_texto_descricao_2 = tk.Text(
    tela_06, width=10, height=5, bg="#6BD4CD")
caixa_texto_descricao_2.place(relx=valorx+.6, rely=valory+.73,
                                         relwidth=.27, relheight=.20)

tela_06.mainloop()  # mainloop = loop infinito para deixar a tela visivel