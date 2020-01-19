print("|--------------------------------------------------------|")
print("|            Bienvenido al ejercicio de Mates!           |")
print("|--------------------------------------------------------|")
print("")
print(" En este apartado tan sólo se realiza las tareas aritméticas, \n aún no se implementa la comprobación de los datos de entrada, \n se supone que los datos de entrada son números enteros. \n")
# #####################################  #
# Solicitud de los numeros al usuario.   #
# Validacion de los numeros de entrada.  #
# #####################################  #

numUno = int(input(" Ingrese el primer número: "))
numDos = int(input(" Ingrese el segundo numero: "))


# #####################################  #
# Divido los numeros de entrada entre 10 #
# #####################################  #

uno = (numUno/10)
dos = (numDos/10)
print (numUno,"/ 10 =", uno)
print (numDos,"/ 10 = ", dos)
# ######################################################################## #
# Realizo las operaciones aritmeticas: suma,resta,multiplicacion,division. #
# ######################################################################## #

suma=(uno+dos)
resta=(uno-dos)
multi=(uno*dos)
divi=(uno/dos)


# ###################################################################### #
# Salida de datos: Imprimo por pantalla el resultado de las operaciones. #
# ###################################################################### #

print("La suma es: ",suma)
print("La resta es: ",resta)
print("La multiplicación es: ",multi)
print("La división es: ",divi)

print("\n --------------------------------------------------------")

##########################
# Formateo de los datos  #
##########################

suma=round(suma,2)
print("Suma redondeo: ", suma)

resta=round(resta,2)
print("Resta redondeo: ", resta)

multi=round(multi,2)
print("Multiplicación redondeo: ", multi)

divi=round(divi,2)
print("División redondeo", divi)


