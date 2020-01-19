import ANSIEscapeSequences
def calcularPrecioEntrada(miedad):
    # Valores segun edad:
    #
    # de 0 años a 2 años   =  0€
    # de 3 años a 12 años  = 14€
    # de 13 años a 64 años = 23€
    # de 65 años o más     = 18€
    #
    
    if miedad > 0 and miedad <= 2:
        precio = 0
    elif miedad <= 12:
        precio = 14
    elif miedad < 65:
        precio = 23
    else:
        precio = 18
    return precio

def validaEdad(cadena):
    try:
        n = int(cadena)
        if n >= 0:
            return True
        return False
    except:
        return False

def pedirEdad():
    ANSIEscapeSequences.locate(1,1)
    edad = input("Ingrese la edad de la persona  o marque 0 para salir: ")
    while validaEdad(edad) == False:
        print("Error Edad introducida inválida...Vuelva a intentarlo ")
        ANSIEscapeSequences.locate(1,1)
        edad = input("Ingrese la edad de la persona  o marque 0 para salir: ")
    return int(edad) 

ANSIEscapeSequences.clear()
edad = pedirEdad()
precioTotal = 0
linea = 4

while edad != 0:
    precioE = calcularPrecioEntrada(edad)
    ANSIEscapeSequences.locate(linea,1)
    print ("Precio entrada: {}".format(precioE))
    linea +=1
    precioTotal += precioE
    
    edad = pedirEdad()
   
    
ANSIEscapeSequences.locate(linea,1)
print("Total: {}".format(precioTotal))

#    if precioE  == 0:
#        linea = 4
#        numEntradasB +=1
#        ANSIEscapeSequences.locate(linea,1)
#        print ("Precio entrada: {}".format(precioE , numEntradasB))
#    if precioE == 14:
#        linea = 5
#        numEntradasN +=1
#        ANSIEscapeSequences.locate(linea,1)
#        print ("Precio entrada: {}".format(precioE , numEntradasN))
#    if precioE == 18:
#        linea = 6
#        numEntradasJ +=1
#        ANSIEscapeSequences.locate(linea,1)
#        print ("Precio entrada: {}".format(precioE, numEntradasJ))
#    if precioE == 23:
#        linea = 7
#        numEntradasA +=1
#        ANSIEscapeSequences.locate(linea,1)
#        print ("Precio entrada: {}".format(precioE, numEntradasA))
#    
#    ANSIEscapeSequences.locate(linea,1)
#    print ("Precio entrada: {}".format(precioE))
#    linea += 1
#    precioTotal += precioE
