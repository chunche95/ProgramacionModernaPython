# Suma de los elementos de una lista de items.
notas =(2,4,6,8)       

# Sumar notas
indice=0
suma=0
while indice < len(notas):
    suma = suma + notas[indice]
    indice = indice + 1
# Calculo de la media.
media = suma / indice
# Imprimo por pantalla el resultado
print("Número de items....: ", indice)
print("Nota total.........: ", suma)
print("La media es........: ", media)


