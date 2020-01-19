notas = (2,4,6,8,10,4,6,8,10,4,6,8,10,4,6,8,10,4,6,8,10,4,6,8,10,4,6,8,10)

def contenido(lista,indice):
    try:
        resultado = lista[indice]
    except:
        resultado = None
    return resultado

def longitud(lista):
    indice = 0
    while contenido (lista,indice) != None:
        indice = indice +1
    return indice

# Calculo de la media
suma = 0
longitudNotas = longitud(notas)
for indice in range(0, longitud(notas)): # Python usa un rango de la longitud total de la lista -1, que es lo que buscamos
    suma = suma + notas[indice]

media = suma / longitud(notas)

# Imprimo resultado
print("Numero de elementos:", longitudNotas)
print("Nota total.........:", suma)
print("Nota Media.........:", media)