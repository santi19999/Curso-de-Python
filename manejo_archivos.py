#Siempre que un archivo se termina de leer el cursor queda al final y no leera nada 
#porque está al final. Por esto es que utilizamos el metodo seek
from io import open 

archivo_texto=open("archivo.txt","r+") #con el mas le indicamos que es de lectura y erscritura

texto=archivo_texto.read()# si le indicamos una posición lee hasta ahí nomas
print(texto)
archivo_texto.seek(0) #posiciona el cursor donde le indicamos en el archivo 
print(texto)

archivo_texto.close()


