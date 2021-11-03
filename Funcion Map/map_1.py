#Aplica una funcion a cada elemento de una lista iterable
#listas,tuplas etc
#devolviedo una lista con los resultados


class Empleado:
    def __init__(self,nombre,cargo,salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
    
    def __str__(self):
        return "{} que trabaja como {} tiene un salario de $$ {}".format(self.nombre,self.cargo,self.salario)



listaEmpleados = [
    Empleado("Juan","Director",7500),
    Empleado("Ana","Presidenta",8500),
    Empleado("Roberto","Administrativo",2500),
    Empleado("Sara","Secretaria",2700),
    Empleado("Mario","Botones",2100)
]


def calculo_comision(empleado):
    if empleado.salario<=3000: 
        empleado.salario=empleado.salario*1.03 #Agregamos el 3% al salario
    return empleado

listadeempleadosComision=map(calculo_comision,listaEmpleados) #Primer Argumento funcion y el segundo la lista


for empleado in listadeempleadosComision:
    print(empleado)
