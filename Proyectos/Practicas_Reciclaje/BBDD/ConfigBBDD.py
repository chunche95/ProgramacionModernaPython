import sqlite3

conexion = sqlite3.connect("BBDD.db") # Establecemos conexion

# Insertamos datos en la tabla SQL
cursor = conexion.cursor();
cursor.execute("INSERT INTO USUARIOS VALUES('Paulino', '25', 'Masculino')");
cursor.execute("INSERT INTO USUARIOS VALUES('Paula', '22', 'Femenino')");
cursor.execute("INSERT INTO USUARIOS VALUES('Jade', '1', 'Femenino')");
# Mostramos los datos
cursor.execute("SELECT * FROM USUARIOS")
# Var para manipular los datos
usuarios = cursor.fetchone()
print(usuarios)
print(usuarios[0])
print(usuarios[1])
print(usuarios[2])


conexion.commit();
conexion.close(); # Desconectamos