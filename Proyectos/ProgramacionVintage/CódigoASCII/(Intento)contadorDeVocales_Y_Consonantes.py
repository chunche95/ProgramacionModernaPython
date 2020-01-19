# Titulo: Contador de caracteres.
# Descripcion:  Muestra el numero de veces que aparecen las vocales o las consonantes2 en una linea de texto.
# Usando un diccionario.
# @Version: 3.0
# @Autor: pauchino09 

texto="abbaccca bb cena"

frecuencias = dict()


for caracter in texto:
    vocales = ['a','e','i','o','u']
    # Bucle que recorre la lista de las vocales
    for v in vocales:
        vocal = v  # --> NO SE COMO ALMACENAR EN LA VARIABLE LOCAL PARA QUE COMPRUEBE LA LISTA DE VOCALES
    #if caracter in frecuencias:
    if frecuencias.get(caracter) != None and frecuencias.get(caracter) == vocal:
        frecuencias[caracter] += 1
        print("Vocal encontrada!", caracter)
    elif frecuencias.get(caracter) != None and frecuencias.get(caracter) != vocal:
        frecuencias[caracter] += 1
        print("Consonante encontrada!", caracter)
    else:
        frecuencias[caracter] = 1
        print("Nueva letra de entrada al diccionario", caracter)
for letra in frecuencias.keys():
    print(letra," --> ", frecuencias[letra])
