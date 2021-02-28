import sqlite3

conexion = sqlite3.connect("Productos.db") # Establecemos conexion

# Insertamos datos en la tabla SQL
cursor = conexion.cursor();

cursor.execute('''
    DROP TABLE PRODUCTOS;
''');
cursor.execute('''

CREATE TABLE PRODUCTOS(
    CODIGO_P VARCHAR(10) PRIMARY KEY,
    NOMBRE_P VARCHAR(50),
    SECCION_P VARCHAR(20)
);

''')

productos=[
    ('ART.1', 'Leche', 'Lacteos'),
    ('ART.2', 'Arroz', 'Cereales'),
    ('ART.3', 'Manzana Golden', 'Frutas y Verduras'),
    ('ART.4', 'Cerveza', 'Bebidas'),
    
]

cursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)", productos)


conexion.commit();
conexion.close(); # Desconectamos