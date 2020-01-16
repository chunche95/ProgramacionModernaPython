notas =(2,4,6,8)
        
def existe(lista,indice):
    try:
        resultado = lista[indice]
    except:
        resultado = None
    return resultado

# No imprime nada pero guarda el valor de la lista, si consulto en la terminal:
# Ej:
# existe(notas,2) --> Devuelve 'Numero de elementos(items): 4'