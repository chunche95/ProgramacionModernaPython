import sqlite3

conexion = sqlite3.connect("BBDD.db") # Establecemos conexion

# Creamos tabla SQL
cursor = conexion.cursor();
cursor.execute("DROP TABLE USUARIOS")
cursor.execute("CREATE TABLE USUARIOS(NOMBRE VARCHAR(50), EDAD INTEGER, SEXO VARCHAR(10))")


conexion.close() # Desconectamos