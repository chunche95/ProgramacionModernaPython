print("|--------------------------------------------------------|")
print("|            Bienvenido al ejercicio de Mates!           |")
print("|--------------------------------------------------------|")
print("")
print("Ejercicio basado en el anterior, pero aquí se hace la \nvalidación de los datos de entrada, se comprueba \nque sean números enteros.\n")

# #####################################  #
# Solicitud de los numeros al usuario.   #
# Validacion de los numeros de entrada.  #
# #####################################  #

numUno = input(" Ingrese el primer número: ")

isvalidN01=False
while not isvalidN01:
    if numUno.isdigit():
        uno = int(numUno)
        isvalidN01=True
    elif numUno != '' and numUno[0] == '-' and numUno[1:].isdigit():
        uno = int(numUno)
        isvalidN01=True
    else:
        print("ATENCION: Debe ingresar un número entero!")
        numUno = input(" Ingrese el primer número: ")

""" --------------------------------------------------------------------------- """

numDos = input(" Ingrese el segundo numero: ")

isvalidN02 = False
while not isvalidN02:
    if numDos.isdigit():
        dos = int(numDos)
        isvalidN02 = True
    elif numDos != '' and numDos[0] == '-' and numDos[1].isdigit():
        dos = int(numDos)
        isvalidN02=True
    else:
        print("ATENCION: Debe ingresar un número entero!")
        numDos = input(" Ingrese el primer número: ")
    
    
    # #####################################  #
    # Divido los numeros de entrada entre 10 #
    # #####################################  #
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
   

