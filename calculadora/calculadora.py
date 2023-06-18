from tkinter import *



def bt_soma():

     entrada1 = float(ent1.get())
     entrada2 = float(ent2.get())
     soma = (entrada1 + entrada2)
     resultado['text']= soma


def bt_subtrair():

     entrada1 = float(ent1.get())
     entrada2 = float(ent2.get())
     subtrair = (entrada1 - entrada2)
     resultado['text']= subtrair

def bt_multiplicar():

     entrada1 = float(ent1.get())
     entrada2 = float(ent2.get())
     multiplicar = (entrada1 * entrada2)
     resultado['text']= multiplicar

def bt_dividir():

     entrada1 = float(ent1.get())
     entrada2 = float(ent2.get())
     dividir = (entrada1 / entrada2)
     resultado['text']= dividir

def bt_limpar():
    ent1.delete(0, END)
    ent2.delete(0, END)
    
janela = Tk()
janela.title('Programa para Calcular Operações Matemáticas')
janela.geometry('500x350')
janela['bg'] = '#008080'

     
#Texto inicial
inicio = Label(janela, text='>>>> Insira seus dados >>>>',fg='#FFFFFF', bg='#008080')
inicio.pack()

num1 = Label(janela, text=' Insira o primeiro número:',fg='#FFFFFF', bg='#008080')
num1.pack()
ent1 = Entry(janela,width=33)
ent1.pack()

num2 = Label(janela, text='Insira o segundo número:',fg='#FFFFFF', bg='#008080')
num2.pack()
ent2 = Entry(janela,width=33)
ent2.pack()

#resultado
resultado = Label(janela,text='Confira o Resultado!',fg='#FFFFFF', bg='#008080')
resultado.pack()

#botão soma
bt_soma = Button(janela, text='Somar', bg= '#F0FFF0', fg='black', width='29', command= bt_soma)
bt_soma.pack()


#botão subtrair
bt_subtrair = Button(janela, text='Subtrair', bg= '#F0FFF0', fg='black', width='29', command= bt_subtrair)
bt_subtrair.pack()

#botão multiplicar
bt_multiplicar = Button(janela, text='Multiplicar', bg= '#F0FFF0', fg='black', width='29', command= bt_multiplicar)
bt_multiplicar.pack()

#botão dividir
bt_dividir = Button(janela, text='Dividir', bg= '#F0FFF0', fg='black', width='29', command= bt_dividir)
bt_dividir.pack()

#botão Limpar
bt_limpar = Button(janela, text='Limpar Tela', bg= '#008080', fg='white', width='10', command= bt_limpar)
bt_limpar.pack()

janela.mainloop()