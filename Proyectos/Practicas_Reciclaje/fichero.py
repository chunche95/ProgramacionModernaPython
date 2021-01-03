from io import open
fichero = open("archivo.txt", "w")
texto = "Hola. Estudio Python, again"
fichero.write(texto)
fichero.close()

fichero = open("archivo.txt", "r")
fichero.close()
print(texto)
