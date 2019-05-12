# @Title: Funciones map,filter
# @Description: Aplicación de 'map' sobre una lista, toma una función y un iterable como
#   argumentos, y devuelve un nuevo iterable con la funcion aplicada a cada argumento.  
#   uso de filtros 'filter' en la obtención de resultados, forma 'elegante' de filtrar los elmentos de
#   una lista, para los que la función devuelve 'True'.
#   Por último, el operador reduce, minimiza los valores de la lista a un solo valor aplicando una funcion reductora.
#   Es necesario importar el módulo 'functools' para usar 'reduce'.
# @Autor: Chunche

from functools import reduce


lista = [1,3,5,8,-1,-4,-6]

# map actua sobre cada uno de los items del operador de 'lista'
listaDobles = map(lambda x: x*2, lista)
# filter actua como filtro en el resultado del programa
listaPares = filter(lambda x: x % 2 == 0, lista)
# reduce actua como 'resumen' del resultado a obtener
resultadoRed = reduce(lambda x,y: x + y, lista)



# Devuelvo valores

print("Lista del doble: " )
print(list(listaDobles))
print("Lista de los pares: ")
print(list(listaPares))
print("Solución devuelta de 'reduce' :")
print(resultadoRed) # 1+3+5+4+8-1-4-6=6