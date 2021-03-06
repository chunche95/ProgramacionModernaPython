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

# Comparo que haya coincidencia entre p1,p2 = p2,p1
def isAnagram(p1,p2):
    return isAnagramE(p1,p2) and isAnagramE(p2,p1)
