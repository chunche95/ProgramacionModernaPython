# Suma de los elementos de una lista de items.
notas =(2,4,6,8)       
def contenido(lista,indice):
    try:
        resultado = lista[indice]
    except:
        resultado = None
    return resultado

# Sumar notas
indice=0
suma=0
while contenido(notas, indice) != None:
    suma = suma + notas[indice]
    indice = indice + 1
# Calculo de la media.
media = suma / indice
# Imprimo por pantalla el resultado
print("Número de items....: ", indice)
print("Nota total.........: ", suma)
print("La media es........: ", media)

