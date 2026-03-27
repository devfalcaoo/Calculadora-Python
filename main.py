# Importando Tkinter
from tkinter import *
from tkinter import ttk

# Cores
cor1 = "#1a0f0f"
cor2 = "#3b0d0d"
cor3 = "#f2f2f2"
cor4 = "#d32f2f"
cor5 = "#b71c1c"

# Criando a janela principal
janela =Tk()
janela.title("Calculadora")
janela.geometry("235x309")
janela.config(bg=cor1)

# Criando os frames
frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268, bg=cor3)
frame_corpo.grid(row=1, column=0)


# Variável global todos_valores
todos_valores = ''

# Criando as funções
def entrar_valores(event):

    global todos_valores

    todos_valores = todos_valores + str(event)
    # para mostrar o resultado na tela
    valor_texto.set(todos_valores)

# Criando a função de calcular
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    
    valor_texto.set(str(resultado))

# Função para limpar a tela
def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")


def aplicador_hover(botao, bg_default, bg_hover):
    def on_enter(event):
        botao.config(bg=bg_hover)

    def on_leave(event):
        botao.config(bg=bg_default)

    botao.bind('<Enter>', on_enter)
    botao.bind('<Leave>', on_leave)


# Criando label/visor
valor_texto = StringVar()

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=("Ivy 18"), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)

# Criando os botões
b_C = Button(frame_corpo, command= limpar_tela, text="C", width=11, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
aplicador_hover(b_C, cor4, "#ffe6e6")
b_C.place(x=-1, y=0)
b_porcent = Button(frame_corpo, command= lambda: entrar_valores("%"), text="%", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
aplicador_hover(b_porcent, cor4, "#f0f0f0")
b_porcent.place(x=118, y=0)
b_div = Button(frame_corpo, command= lambda: entrar_valores("/"), text="/", width=5, height=2, bg=cor5, fg=cor2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
aplicador_hover(b_div, cor5, "#ffb74d")
b_div.place(x=177, y=0)

b_7 = Button(frame_corpo, command= lambda: entrar_valores("7"), text="7", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
aplicador_hover(b_7, cor4, "#f5f5f5")
b_7.place(x=0, y=52)
b_8 = Button(frame_corpo, command= lambda: entrar_valores("8"), text="8", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
aplicador_hover(b_8, cor4, "#f5f5f5")
b_8.place(x=59, y=52)
b_9 = Button(frame_corpo, command= lambda: entrar_valores("9"), text="9", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
aplicador_hover(b_9, cor4, "#f5f5f5")
b_9.place(x=118, y=52)
b_mult = Button(frame_corpo, command= lambda: entrar_valores("*"), text="*", width=5, height=2, bg=cor5, fg=cor2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
aplicador_hover(b_mult, cor5, "#ffb74d")
b_mult.place(x=177, y=52)

b_4 = Button(frame_corpo, command= lambda: entrar_valores("4"), text="4", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
aplicador_hover(b_4, cor4, "#f5f5f5")
b_4.place(x=0, y=104)
b_5 = Button(frame_corpo, command= lambda: entrar_valores("5"), text="5", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
aplicador_hover(b_5, cor4, "#f5f5f5")
b_5.place(x=59, y=104)
b_6 = Button(frame_corpo, command= lambda: entrar_valores("6"),text="6", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
aplicador_hover(b_6, cor4, "#f5f5f5")
b_6.place(x=118, y=104)
b_sub = Button(frame_corpo, command= lambda: entrar_valores("-"), text="-", width=5, height=2, bg=cor5, fg=cor2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
aplicador_hover(b_sub, cor5, "#ffb74d")
b_sub.place(x=177, y=104)

b_1 = Button(frame_corpo, command= lambda: entrar_valores("1"), text="1", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
aplicador_hover(b_1, cor4, "#f5f5f5")
b_1.place(x=0, y=156)
b_2 = Button(frame_corpo, command= lambda: entrar_valores("2"), text="2", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
aplicador_hover(b_2, cor4, "#f5f5f5")
b_2.place(x=59, y=156)
b_3 = Button(frame_corpo, command= lambda: entrar_valores("3"), text="3", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
aplicador_hover(b_3, cor4, "#f5f5f5")
b_3.place(x=118, y=156)
b_soma = Button(frame_corpo, command= lambda: entrar_valores("+"), text="+", width=5, height=2, bg=cor5, fg=cor2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
aplicador_hover(b_soma, cor5, "#ffb74d")
b_soma.place(x=177, y=156)

b_0 = Button(frame_corpo, command= lambda: entrar_valores("0"), text="0", width=11, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
aplicador_hover(b_0, cor4, "#f5f5f5")
b_0.place(x=-1, y=208)
b_ponto = Button(frame_corpo, command= lambda: entrar_valores("."), text=".", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
aplicador_hover(b_ponto, cor4, "#f5f5f5")
b_ponto.place(x=118, y=208)
b_result = Button(frame_corpo, command= calcular, text="=", width=5, height=2, bg=cor5, fg=cor2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
aplicador_hover(b_result, cor5, "#ffb74d")
b_result.place(x=177, y=208)



janela.mainloop()