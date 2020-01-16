# Titulo: Contador de caracteres.
# Descripcion:  Muestra el numero de veces que aparece un caracter en una linea de texto.
# Usando una lista.
# @Version: 1.0
# @Autor: pauchino09 

def existe(letra,lista):
    posicion = 0
    while posicion < len(lista):
        if lista[posicion] == letra:
            return posicion
        posicion += 1
    return None
        

texto="tres palabras son"

letras = []
frecuencias = []

for caracter in texto:
    posicion = existe(caracter, letras)
    if posicion!= None:
        frecuencias[posicion] += 1
    else:
        letras.append(caracter)
        frecuencias.append(1)
        
indice = 0
while indice < len(letras):
    print(letras[indice], " --> ", frecuencias[indice])
    indice +=1