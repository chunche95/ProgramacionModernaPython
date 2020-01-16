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
    edad = input("Ingrese la edad de la persona  o marque 0 para salir: ")
    while validaEdad(edad) == False:
        print("Error Edad introducida inválida...Vuelva a intentarlo ")
        edad = input("Ingrese la edad de la persona  o marque 0 para salir: ")
    return int(edad) 

edad = pedirEdad()
precioTotal = 0

while edad != 0:
    precioE = calcularPrecioEntrada(edad)
    print ("Precio entrada: {}".format(precioE))
    precioTotal += precioE
    
    edad = pedirEdad()
    
print("Total: {}".format(precioTotal))
