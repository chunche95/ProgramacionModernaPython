def calcularPrecioEntrada(edad):
    # Valores segun edad:
    #
    # de 0 años a 2 años   =  0€
    # de 3 años a 12 años  = 14€
    # de 13 años a 64 años = 23€
    # de 65 años o más     = 18€
    #
    
    if edad > 0 and edad <= 2:
        precio = 0
    elif edad <= 12:
        precio = 14
    elif edad < 65:
        precio = 23
    elif edad >= 65 and edad < 120:
        precio = 18
    else:
        print("Error Edad introducida inválida ")
    
    return precio

def pedirEdad():
    edad = input("Ingrese la edad de la persona  o marque 0 para salir: ")
    edad = int(edad)
    return edad

edad = pedirEdad()
precioTotal = 0

while edad != 0:
    precioE = calcularPrecioEntrada(edad)
    print ("Precio entrada: {}".format(precioE))
    precioTotal += precioE
    
    edad = pedirEdad()
    
print("Total: {}".format(precioTotal))