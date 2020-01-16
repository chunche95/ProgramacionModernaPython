notas =(2,4,6,8)
        
def contenido(lista,indice):
    try:
        resultado = lista[indice]
    except:
        resultado = None
    return resultado


# Contar los elementos de notas.

indice=0
while contenido(notas, indice) != None:
    indice = indice + 1
print ("Número de elementos(items): ", indice)