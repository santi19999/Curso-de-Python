from tkinter import *
from tkinter import ttk

class Window():
    def __init__(self):
        self.ventana = Tk()     
        i=1
        self.new_Frame("Encabezado",450,350)
        self.new_Label("Soy la Imagen {}: ".format(i),10,20)
        self.new_Label("Soy la Imagen {}: ".format(i+1),10,120)
        self.new_Label("Soy la Imagen {}: ".format(i+2),10,220)

        '''Creamos Botones Inicando la cantidad, los crea automaticamente
        cant_b = int(input("Indique cuantos botones desea agregar"))
        for a in range(0,cant_b):
            
                texto = (" Boton {} ").format(a+1)
                posicion = int(a*(450/cant_b))
                print(posicion)
                self.new_button(texto,posicion,10)
         '''





        self.ventana.mainloop()



    def new_Frame(self,nombre,ancho,alto):
        self.nombre=Frame(self.ventana, width=ancho , height=alto)
        self.nombre.config(bg="red")
        self.nombre.pack()

    def new_Label(self,texto,xx,yy):
        Label(self.nombre, text=texto,fg="red",font=("Comic Sans MS",12)).place(x=xx,y=yy)

    def new_button(self,text,xx,yy):
        btn=ttk.Button(text=text,width=10)
        btn.place(x=xx,y=yy)





ventana1=  Window()  

