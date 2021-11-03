import sqlite3

miConexion = sqlite3.connect("GestionProductos")
miCursor   = miConexion.cursor()

#Seleccionamos todos los datos de una sola columna o campo
#miCursor.execute("SELECT NOMBRE_ARTICULO FROM PRODUCTOS")

#Seleccionamos todos los registros del campo SECCION que tienen ese dato en el campo 
#miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='juguetería'")

#ACTUALIZAR - UPDATE

#miCursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO='Pantalón'")
for a in range(0,9):
    nombre = input("Ingrese el nombre del articulo que desea borrar: ")
    miCursor.execute("DELETE FROM PRODUCTOS WHERE SECCION='confeccion'")
    miConexion.commit()


miConexion.close()