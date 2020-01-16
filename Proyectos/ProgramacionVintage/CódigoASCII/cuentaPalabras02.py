miText = "Mi prueba    de texto.                Fin    del mensaje.  "

cuentaPalabras = 0

posicion = 0
caracterAnterior = " "
for caract in miText:
    if caract == " " and caracterAnterior != " ":
        print("Encuentro", cuentaPalabras ,"espacios.")
        cuentaPalabras += 1
    # Realizo un comparador de desface de contador de espacios.
    caracterAnterior = caract
# Si no encuentro un espacio vacio, voy sumando + 1 en cuentaPalabras.
# o
# Si encuentro mas de un espacio vacio termino de sumar.
if caract != " " :
    cuentaPalabras += 1
print("Total: ",cuentaPalabras , " palabras.")