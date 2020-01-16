# Funcion que nos indica el tiempo de ejecucion de cada una  de las funciones del programa
import timeit
# Creo una funcion que guarda las operaciones de comprobracion del anagrama
def isAnagramE(p1,p2):
    # Inicializo una lista que guarda las comparaciones de las letras
    listaComparacionLetras = []
    # Comparo la longitud de las palabras para que sean iguales, en  numero de letras
    if len(p1) != len(p2):
        return False
    # Inici un bucle anidado con la comparacion de las letras
    for caracter1 in p1:
        noAnadirFalse = False
        for caracter2 in p2:
            # Si no hay una igualdad entre las letras salta fuera
            if caracter1 == caracter2:
                noAnadirFalse = True
                listaComparacionLetras.append(True)
        if not noAnadirFalse:
            listaComparacionLetras.append(False)
    if False in listaComparacionLetras:
        return False
    else:
        return True


def isAnagramDef(p1,p2):
    return isAnagramE(p1,p2) and isAnagramE(p2,p1)
def cuentaCaracteres(cadena):
    count = dict()
    
    for caracter in cadena:
        if caracter in count:
            count[caracter] += 1
        else:
            count[caracter] = 1
    return count

def isAnagramDic(p1,p2):
    dicP1 = cuentaCaracteres(p1)
    dicP2 = cuentaCaracteres(p2)
    
    return dicP1 == dicp2

t = timeit.Timer("isAnagramE('amar', 'amor')", "from __main__ import isAnagramE")
timeAnagramE = t.timeit()
t = timeit.Timer("isAnagramDef('amar', 'amor')", "from __main__ import isAnagramDef")
timeAnagramDef = t.timeit()
t = timeit.Timer("isAnagramDic('amar','amor')", "from __main__ import isAnagramDef")
timeAnagramDic = t.timeit()


print("Simple: {}".format(timeAnagramE))
print("Duplo : {}".format(timeAnagramDef))
print("Diccio: {}".format(timeAnagramDic))