fEntradas  = open("transacciones.txt", 'r') # Fichero en formato lectura

todas = fEntradas.readlines()

# Lee el fichero  y lo imprime en una sola linea
for transaccion in todas:
    print (transaccion)
    
# Imprime linea a linea, con un salto de linea
for transaccion in todo.split('\n') :
    print (transaccion)
fEntradas.close()


# Todas las lineas las devuelve

fEntradas = open("transacciones.txt", 'r')
# Bucle de lectura con un bucle for --> recomendable para ficheros cortos
for todasLasLineas in readlines():
    print todasLasLineas
    
fEntradas.close()

clear or cls


fEntradas.open("transacciones.txt")
linea = fEntradas.readLine()
print (linea)
# Recomndables para ficheros mas grandes a la giba 1GB
while linea != '':
    print (linea)
    linea = fEntradas.readline()
    
# ReadTodo no es aconsejable


