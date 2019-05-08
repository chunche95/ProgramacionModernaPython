'''
Description: Funciones de primera clase y funciones de nivel superior
Version: 1.0
Author: Chunche
'''

# Son funciones de primera clase si pueden invocar, y trabajar con los valores de la misma, pueden asignarse, guardarse
# en otras funciones y variables.
# funcion de primera clase -> son equivalentes a los datos

def cuentaNum(numero):
    contador = 0
    for i in range(0, numero+1):
        contador += 1
    
    return contador

print(cuentaNum(1000))
print("----------------------------------------------------------------------------------------------------------")
print(list(range(0, 101)))
print("----------------------------------------------------------------------------------------------------------")
print(list(range(0, 101, 2)))

addAll = cuentaNum
addAll(4)

print("----------------------------------------------------------------------------------------------------------")
# Funciones de nivel superior son funciones que reciben parametros o como resultado es otra funcion
# Por ejemplo:

def sumaTodosLosCuadrados(limitTo):
    resultado = 0
    for i in range(limitTo+1):
        resultado += i*i
    return resultado


print(sumaTodosLosCuadrados(3))
        