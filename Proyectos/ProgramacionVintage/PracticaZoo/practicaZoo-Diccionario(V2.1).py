import ANSIEscapeSequences
entradas = {
        'baby':{'cantidad':0,'precio':0},
        'niño':{'cantidad':0,'precio':14},
        'adulto':{'cantidad':0,'precio':23},
        'jubilado':{'cantidad':0,'precio':18}
}

lineaPantalla = {'baby':4, 'niño':5,'jubilado':6,'adulto':7}

def tipoEntrada(miedad):
    # Segun edad, el precio de la entrada
    #
    # Valores segun edad:
    #
    # de 0 años a 2 años   =  0€
    # de 3 años a 12 años  = 14€
    # de 13 años a 64 años = 23€
    # de 65 años o más     = 18€
    #
    
    if miedad > 0 and miedad <= 2:
        tipo = 'baby'
    elif miedad <= 12:
        tipo = 'niño'
    elif miedad < 65:
        tipo = 'adulto'
    else:
        tipo = 'jubilado'
    
    return tipo

def validaEdad(cadena):
    # Comprueba que se pueda convertir en un numero entero y sea positivo
    try:
        n = int(cadena)
        if n >= 0:
            return True
        return False
    except:
        return False

def pedirEdad():
    ANSIEscapeSequences.clear()
    ANSIEscapeSequences.locate(1,1)
    edad = input("Ingrese la edad de la persona  o marque 0 para salir: ")
    while validaEdad(edad) == False:
        ANSIEscapeSequences.locate(1,1)
        print("Error Edad introducida inválida...Vuelva a intentarlo ")
        edad = input("Ingrese la edad de la persona  o marque 0 para salir: ")
    edad = int(edad)
    return edad

ANSIEscapeSequences.clear()
edad = pedirEdad()
precioTotal = 0
#linea = 4
while edad != 0:
    
    #ANSIEscapeSequences.locate(linea,1)
    tipo = tipoEntrada(edad)
    entradas[tipo]['cantidad'] += 1
    precio = entradas[tipo]['precio']
    cantidad = entradas[tipo]['cantidad']
    #linea += 1
    precioTotal += precio
    
    linea = lineaPantalla(tipo)
    ANSIEscapeSequences.locate(linea,1)
    
    print("Precio Entrada: {}€ x {}persona = {}€".format(precio,cantidad,precio*cantidad))
    edad = pedirEdad()
    
linea += 4
ANSIEscapeSequences.locate(linea,10)
print ("============================")
print("Total: {}".format(precioTotal))

