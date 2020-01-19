# Determinar el precio de un conjunto de entradas al Zoo.
#
# Hacer un programa qe muestre el precio total de las entradas de un grupo de personas al zoo.
# Teniendo en cuenta los siguientes precios:
# - Niños de 2 o menos años: no pagan
# - Hasta los 12 años: 14€
# - Jubilados de 65 o más años: 18€
# - Entrada estandar: 23€
#
# El programa pedirá la edad de los componentes del grupo,
# > primero pedirá una edad y sucesivamente las demás.
# > En el momento en el qe se introduzca un 0 se consoderará el final
#
# Se devolverá:
# 
# 1 entradas de baby (0€):      0.00€
# 3 entradas de menores(14€):  42.00€
# 2 entradas normales (23€):   46.00€
# 1 entradas jubilado (18€):   18.00€
#                             --------
#                             106.00€
#
# ------------------------------------------
# edad <- Entrada a introducir
# precio = 0 
# while edad = final
#   precioE <-
#

import sys
import math

def esEntero(n):
    try:
        int(n)
        return True
    except:
        return False

strEdad = input(" Ingrese la edad de las personas a ingresar o MARQUE 0 PARA SALIR: ")
entradasB = 0
entradasM = 0
entradasJ = 0
entradasE = 0

if esEntero(strEdad) == True and strEdad != '0':
    while esEntero(strEdad) == True and  strEdad != '0':
        edad = int(strEdad)
        if edad >= 0 and edad <= 2:
            entradasB +=1
            totalEntradasB = entradasB * 0
        elif edad >= 2 and edad <= 12:
            entradasM += 1
            totalEntradasM = entradasM * 14
        elif edad >= 65:
            entradasJ += 1
            totalEntradasJ = entradasJ * 18
        else:
            entradasE += 1
            totalEntradasE = entradasE * 23
        strEdad = input("Ingrese la edad de las personas a ingresar o MARQUE 0 PARA SALIR: ")
        

print(entradasB, " Entradas de baby (0€): ", totalEntradasB)
print(entradasM, " Entradas de menores:   " , totalEntradasM)
print(entradasJ, " Entradas de jubilados: ", totalEntradasJ)
print(entradasE, " Entradas normales:     ",  totalEntradasE)
print("----------------------------------------------------")
print(" TOTAL: ",totalEntradasB + totalEntradasM + totalEntradasJ + totalEntradasE)