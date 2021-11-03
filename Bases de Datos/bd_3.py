import sqlite3

miConexion = sqlite3.connect("GestionProductos")
miCursor = miConexion.cursor()

miCursor.execute("CREATE TABLE IF NOT EXISTS PRODUCTOS (ID INTEGER PRIMARY KEY AUTOINCREMENT,NOMBRE_ARTICULO VARCHAR(50),PRECIO INTEGER,SECCION VARCHAR (20))")

productos=[
    ("Patin", 20 ,"juguetería"),
    ("Pantalón", 15 ,"confeccion"),
    ("Destornillador", 25 ,"ferrerteria"),
    ("Jarrón", 45 ,"cerámica")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)",productos)
miConexion.commit()

miConexion.close()