def funciones_decoradoras(funcion_parametro):
    
    def funcion_interior():
        print("Vamos a realizar Cálculos: ")
        
        funcion_parametro()
        
        print("Finalizaron los Cálculos. ")
        
        funcion_parametro()
        
        
    return funcion_interior


@funciones_decoradoras
def suma():
    
    print(15+20)

@funciones_decoradoras

def resta():
    
    print(10-20)
    


suma()
resta()



