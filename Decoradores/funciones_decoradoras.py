def funciones_decoradoras(funcion_parametro):
    
    def funcion_interior(*args): #Debenos tener el parametro *args para recibir argumentos
        print("Vamos a realizar Cálculos: ")
        
        funcion_parametro(*args)
        
        print("Finalizaron los Cálculos. ")        
        
    return funcion_interior


@funciones_decoradoras
def suma(num1,num2,num3):
    
    print(num1+num2+num3)


@funciones_decoradoras

def resta(num1,num2,num3):
    
    print(num1-num2-num3)
    


suma(10,10,10)
resta(60,10,5)



