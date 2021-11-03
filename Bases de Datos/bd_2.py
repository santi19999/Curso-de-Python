import sqlite3 

miConexion=sqlite3.connect("PrimeraBase") #Se  crea la base de datos PrimeraBase si no existe y si existe se conecta a ella

miCursor=miConexion.cursor()
miCursor.execute("CREATE TABLE productos FROM PrimeraBase")
miCursor.execute("SELECT * FROM productos")
variosDatos=miCursor.fetchall()
print(variosDatos)



miConexion.commit()
miConexion.close()