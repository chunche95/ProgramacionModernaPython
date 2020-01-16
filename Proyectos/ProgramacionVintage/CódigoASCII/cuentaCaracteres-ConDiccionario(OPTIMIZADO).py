# Titulo: Contador de caracteres.
# Descripcion:  Muestra el numero de veces que aparece un caracter en una linea de texto.
# Usando un diccionario.
# @Version: 2.0
# @Autor: pauchino09 

texto="tres palabras son"

frecuencias = dict()

for caracter in texto:
    if caracter in frecuencias:
    #if frecuencias.get(caracter) != None:
        frecuencias[caracter] += 1
    else:
        frecuencias[caracter] = 1
        
for letra in frecuencias.keys():
    #print("\033[3;33;31m")
    print( letra," --> ", frecuencias[letra] )
    #print("\033[0;37;40m")
    