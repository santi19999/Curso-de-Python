import sqlite3



miConexion = sqlite3.connect("PrimeraBase")
miCursor = miConexion.cursor()

miCursor.execute("CREATE TABLE IF NOT EXISTS PRODUCTOS (id INTEGER (20) , nombre VARCHAR (100), apellido VARCHAR(100))")
miCursor.execute("INSERT INTO PRODUCTOS VALUES(1,'sERGIO','hERRERA')")

miConexion.commit()
miConexion.close()