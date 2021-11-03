import sqlite3



miConexion = sqlite3.connect("PrimeraBase")
miCursor = miConexion.cursor()

'''miCursor.execute("CREATE TABLE PRODUCTOS ,(id INTEGER PRIMARY, nombre VARCHAR (100), apellido VARCHAR(100))")
miConexion.commit()'''
miConexion.close()