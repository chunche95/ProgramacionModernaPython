# Title: funciones anónimas - Lambda.
# Description: Creación de funciones anónimas con la importación de sumaTodos del programa funcionesPrimerNivel
# Autor: chunche

from funcionesPrimerNivel import sumaTodos 
# Procesamiento de datos que no van a ser reutilizadas, si quiero reutilizarlas, uso un 'def'
doble = lambda x: x*2
triple = lambda x: x*3


# Por ejemplo: Bloque de código de números del 0 al 3 sumando solo los pares
print(sumaTodos(3, doble))
# Ahora el triple, hasta el 100
print(sumaTodos(100, triple))

for v=0 to 3:
    print v
