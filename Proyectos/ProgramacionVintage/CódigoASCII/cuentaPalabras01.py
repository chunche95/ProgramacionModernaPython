# Se añade un espacio al final de la frase para que se 'ponga a prueba' el contador de
# palabras.
miText = "Mi prueba de texto. "

cuentaPalabras = 0

for caract in miText:
    if caract == " ":
        print("Encuentro", cuentaPalabras ,"espacios.")
        cuentaPalabras += 1
# Si no encuentro un espacio vacio, voy sumando + 1 en cuentaPalabras.
# o
# Si encuentro mas de un espacio vacio termino de sumar.
if caract != " " :
    cuentaPalabras += 1
print("Total: ",cuentaPalabras , " palabras")