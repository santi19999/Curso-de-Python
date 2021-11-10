#Las expresiones regulares son una secuencia de caracteres que forman un patron de búsqueda.
#Sirven para el trabajo y el procesamiento de texto
#Ejemplos:
#   *Buscar un texto que se ajusta a un formato determinado (correo electronico)
#   *Buscar si existe o una una cadena de caracteres dentro de un texto
#   *Contar el numero de coincidencias denrto de un texto
import re

cadena = ['Ana Gómez',
          'María Martín',
          'Sandra López',
          'Santiago Martín']

for elemento in cadena:
    
    if re.findall('>', cadena) != None:
        print("Si se encontró la cadena")
    else:
        print("No se encontró la cadena")