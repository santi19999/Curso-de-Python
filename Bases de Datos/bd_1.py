import sqlite3



miConexion = sqlite3.connect("PrimeraBase")
miCursor = miConexion.cursor()

miCursor.execute("CREATE TABLE IF NOT EXISTS PRODUCTOS (id INTEGER (20) , nombre VARCHAR (100), apellido VARCHAR(100))")

misDatos=[
    (3,"Noelia","Gauna"),
    (4,"Sergio","Gauna"),
    (5,"Denis","Gauna"),
    (6,"Martina","Herrera Gauna")
]

#Seleccionamos todos los datos de la tabla y los almacenamos en una lista
miCursor.execute("SELECT * FROM PRODUCTOS")
misDatos = miCursor.fetchall()
print(misDatos)
miConexion.close()