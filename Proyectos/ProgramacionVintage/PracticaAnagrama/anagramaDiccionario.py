def contarCaracteresDeCadena(cadena):
# Creacion de un nuevo diccionario de python
    resultado = dict()
    # Recorremos la cadena de las palabras introducidas por el parámetro p1 y p2 respectivamente
    for caracter in cadena:
        # Comprobacion de su existencia en el diccionario
        if caracter in resultado:
            resultado[caracter] += 1
        else:
            resultado[caracter] = 1
    # Devolucion de la respuesta del diccionario creado
    return resultado

def isAnagram(p1,p2):
    #Defino en unas variables nuevas el numero de caracteres que tienen mis palabras de entrada y las guardo en las mismas
    dP1 = contarCaracteresDeCadena(p1)
    dP2 = contarCaracteresDeCadena(p2)
    # Miro la longitud y realizo su comparacion
    if len(dP1) != len(dP2):
        return False
    # Bucle que indica la coincidencia de las palabras o no, cumpliendo siempre las condiciones anteriormente dichas.
    for caracter in dP1:
        if caracter in dP2 and dP1[caracter] == dP2[caracter]:
            pass
        else:
            return False
    return True



print(isAnagram('ama','rama'))
print(isAnagram('amar','rama'))

print(isAnagram('amar','arroz'))
print(isAnagram('am_r','arroz'))