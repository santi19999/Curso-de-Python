from tkinter import *
from tkinter import tix
import tkinter

#Creamos la ventana principal
raiz=Tk()
raiz.title("Window")
#Indicamos si se puede modificar el tamaño de la ventana
raiz.resizable(False, False) 

#Insertamos in icono en la parte superior de la ventana
#raiz.iconbitmap("icon.ico")

#Indicamos el tamaño de la ventana
#raiz.geometry("650x350")

#Indicamos el color de fondo de la ventana
raiz.config(bg="blue")

miFrame0 = Frame()
miFrame0.pack(side="top",fill="x")
miFrame0.config(bg="yellow",width=850,height=100)

miFrame1 = Frame()
miFrame1.pack(side="right",fill="both",expand=True)
miFrame1.config(bg="red",width=650,height=350)


miFrame2 = Frame()
miFrame2.pack(side="left",fill="y")
miFrame2.config(bg="green",width=200,height=350)


menu = tkinter.tix.OptionMenu(miFrame2,text="Menu")





raiz.mainloop()




'''
    Creamos la ventana principal sin usar .pack() funcion

#Creamos un frame para el encabezado 
miFrame3 = Frame()
miFrame3.config(bg="yellow",width="650",height=100)
miFrame3.grid(row=0,column=0)

#Contenedor de los frames principales
contentFrame=Frame()
contentFrame.config(width=650,height=350,bg="red")
contentFrame.grid(row=1,column=0)
contentFrame.pack(side="right")


#Creamos un frame para el contenido principal
miFrame = Frame(contentFrame)
miFrame.config(bg="brown",width="500",height=350)
miFrame.grid(row=1,column=1)


#Creamos un frame para la barra de navegacion lateral
miFrame2 = Frame(contentFrame)
miFrame2.config(bg="Green",width="150",height=350)
miFrame2.grid(row=1,column=0)'''