import ANSIEscapeSequences

precioE = {
    'bebe':0,
    'niño':14.00,
    'adulto':23.00,
    'jubilado':18.00
    }
entradasQ = {
    'bebe':(4,22),
    'niño':(5,22),
    'adulto':(6,22),
    'jubilado':(7,22)
    }


def tipoEntrada(edad):
    if edad > 0 and edad <= 2:
        tipo = 'bebe'
    elif edad <= 12:
        tipo = 'niño'
    elif edad < 65:
        tipo = 'adulto'
    else:
        tipo = 'jubilado'
    return tipo

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

def printScreen():
    ANSIEscapeSequences.locate(3,17)
    print("Entradas")
    ANSIEscapeSequences.locate(3,27)
    print("Precio")
    ANSIEscapeSequences.locate(4,5)
    print("Bebe.......:         -")
    ANSIEscapeSequences.locate(5,5)
    print("Niño.......:         -")
    ANSIEscapeSequences.locate(6,5)
    print("Adulto.....:         -")
    ANSIEscapeSequences.locate(7,5)
    print("Jubilado...:         -")
    ANSIEscapeSequences.locate(9,5)
    print("Total......:")
    
ANSIEscapeSequences.clear()
printScreen()
edad = pedirEdad()
precioTotal = 0       # Capa de Negocio
linea = 4             # Capa de Presentación

while edad != 0:
    tipoE = tipoEntrada(edad)
    precioE = precioE[tipoE]
    ANSIEscapeSequences.locate(entradasQ[tipoE][0], entradasQ[tipoE][1]) 
 '''   
    if precioE == 0:
        ANSIEscapeSequences.locate(4,18)
        print(1)
        ANSIEscapeSequences.locate(4,28)
        print(precioE)
    if precioE == 14:
        ANSIEscapeSequences.locate(5,18)
        print(1)
        ANSIEscapeSequences.locate(5,28)
        print(precioE)
    if precioE == 23:
        ANSIEscapeSequences.locate(6,18)
        print(1)
        ANSIEscapeSequences.locate(6,28)
        print(precioE)
    if precioE == 18:
        ANSIEscapeSequences.locate(7,18)
        print(1)
        ANSIEscapeSequences.locate(7,28)
        print(precioE)
  '''  
    precioTotal += precioE
    
    edad = pedirEdad()
   
    
ANSIEscapeSequences.locate(9,28)
print("{}".format(precioTotal))
