import pickle

# open("lista_nombres","rb") #leemos los datos del archivo binario

lista_nombres=["Pedro","Maria","Ana","Isabel"]#creamos una lista

fichero_binario = open("lista_nombres","wb")#abrimos y creamos un archivo binario para escribirlo

pickle.dump(lista_nombres, fichero_binario) #insertamos los datos de la lista en el archivo binario

fichero_binario.close()

del (fichero_binario)