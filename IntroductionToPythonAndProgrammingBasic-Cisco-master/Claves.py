import sqlite3

conexion = sqlite3.connect("ElMercao.db") # Establecemos conexion

# Insertamos datos en la tabla SQL
cursor = conexion.cursor();

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


# AUTOINCREMENTADO


conexion.commit();
conexion.close(); # Desconectamos