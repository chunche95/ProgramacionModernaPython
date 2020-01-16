#
# Description: Elimina el exceso de espacios en blanco de una linea de texto
#  @version: 1.0
#  @autor pauchino09
#


miText = "Mi       prueba   de  texto. "\
        "Con exceso deee      e s p a c i o s en Blanco "\


caract = " ".join( miText.split() )
print (caract)
#    cuentaPalabras +=1
#print("Total: ",cuentaPalabras , " palabras")