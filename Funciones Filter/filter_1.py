import sqlite3



def new_register(datos):
    miCursor.executemany("INSERT INTO REGISTROS VALUE(?,?)",datos)

def select_datos():
    miCursor.execute("SELECT * FROM REGISTROS WHERE EMAIL=")


miConexion = sqlite3.connect("DB_DATOS")
miCursor = miConexion.cursor()

miCursor.execute("CREATE TABLE REGISTROS IF NOT EXISTS (NOMBRE VARCHAR UNIQUE(50), EMAIL VARCHAR UNIQUE (50))")
datos = [
    ("Sergio Herrera","sergiodanielherrera23@gmail.com"),
    ("Santiago Herrera","santiherrera1999@gmail.com"),
    ("Martina Herrera"," martinaherrera@gmail.com")

]
new_register(datos)