import sqlite3

conexion = sqlite3.connect("BBDD.db") # Establecemos conexion

# Insertamos datos en la tabla SQL
cursor = conexion.cursor();

usuarios = [
    ('Sonia', 28, 'Femenino'),
    ('Brayan', 22, "Masculino"),
    ('Lucas', 45, 'Masculino'),
]

cursor.executemany("INSERT INTO USUARIOS VALUES( ?,?,?)", usuarios)

# Mostramos los datos
cursor.execute("SELECT * FROM USUARIOS")
USUARIOS = cursor.fetchall()
# print(USUARIOS)
for i in USUARIOS:
    print(i)
# Var para manipular los datos


conexion.commit();
conexion.close(); # Desconectamos