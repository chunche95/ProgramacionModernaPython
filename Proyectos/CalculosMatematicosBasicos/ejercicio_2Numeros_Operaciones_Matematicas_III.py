print("|--------------------------------------------------------|")
print("|            Bienvenido al ejercicio de Mates!           |")
print("|--------------------------------------------------------|")
print("")
print("Ejercicio basado en el anterior, pero aquí se hace la \nvalidación de los datos de entrada, se comprueba \nque sean números enteros.\n")

# #####################################  #
# Solicitud de los numeros al usuario.   #
# Validacion de los numeros de entrada.  #
# #####################################  #
def validacion(mensaje):
    num = input(mensaje)

    isvalid=False
    while not isvalid:
        if num.isdigit():
            numero = int(num)
            isvalid=True
        elif num != '' and num[0] == '-' and num[1:].isdigit(): # acepta nº negativos
            numero = int(num)
            isvalid=True
        else:
            print("ATENCION: Debe ingresar un número entero!")
            num = input(mensaje)
    # Pido de vuelta el valor del numero, si es valido
    return num

numUno = validacion("Ingrese un numero: ")
numDos = validacion("Ingrese un numero: ")
numTres = validacion("Ingrese un numero: ")
""" --------------------------------------------------------------------------- """

# #####################################  #
# Divido los numeros de entrada entre 10 #
# #####################################  #
uno = int(numUno)
dos = int(numDos)

uno=uno/10
dos=dos/10

print (numUno,"/ 10 =", uno)
print (numDos,"/ 10 = ", dos)
# ######################################################################## #
# Realizo las operaciones aritmeticas: suma,resta,multiplicacion,division. #
# ######################################################################## #

suma=(uno+dos)
resta=(uno-dos)
multi=(uno*dos)
divi=(uno/dos)
resto=(uno%dos)

# ###################################################################### #
# Salida de datos: Imprimo por pantalla el resultado de las operaciones. #
# ###################################################################### #

print("La suma es: ",suma)
print("La resta es: ",resta)
print("La multiplicación es: ",multi)
print("La división es: ",divi)
print("El resto es:" , resto)
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

resto=round(resto,2)
print("Resto redondeado es: ", resto)

print("El número 3 no sirve para mucho....Para nada, la verdad, gracias.")


