import sqlite3

conexion = sqlite3.connect("CRUD.db") # Establecemos conexion

# Insertamos datos en la tabla SQL
cursor = conexion.cursor();

cursor.execute("DROP TABLE PRODUCTOS")

# AUTOINCREMENTADO
cursor.execute('''

CREATE TABLE PRODUCTOS(
    CODIGO_P INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_P VARCHAR(50),
    SECCION_P VARCHAR(20)
);

''')  

productos=[
    ('Leche', 'Lacteos'),
    ('Arroz', 'Cereales'),
    ('Manzana Golden', 'Frutas y Verduras'),
    ('Cerveza', 'Bebidas'),
    
]

cursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?)", productos)
conexion.commit();
# Vemos los datos
cursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION_P='Bebidas'")
producto = cursor.fetchall()
print(producto)

# Actualizar 
cursor.execute("UPDATE PRODUCTOS SET SECCION_P='B.Alcoholicas' WHERE SECCION_P='Bebidas'")


productos2=[
    ('Maiz', 'Verduras'),
    ('Pan de leche', 'Panaderia'),
    ('Nutella', 'Dulces'),
    ('Agua', 'Bebidas'),
    
]
cursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?)", productos2)
# Vemos los datos
cursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION_P='Bebidas'")
producto2 = cursor.fetchall()
print(producto2)
conexion.commit();
# Borrar
cursor.execute("DELETE FROM PRODUCTOS WHERE CODIGO_P=1")

# Vemos los datos
cursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION_P='Bebidas'")
producto3 = cursor.fetchall()
print(producto3)

conexion.commit();
conexion.close(); # Desconectamos