# Creo una funcion que guarda las operaciones de comprobracion del anagrama
def isAnagram(p1,p2):
    # Inicializo una lista que guarda las comparaciones de las letras
    listaComparacionLetras = []
    # Inicio un bucle for para la primera palabra
    for caracter1 in p1:
        # Guardo una variable para saber si hay una igualdad entre p1 y p2
        noAnadirFalse = False
        for caracter2 in p2:
            if caracter1 == caracter2:
                noAnadirFalse = True
                listaComparacionLetras.append(True)
                
        if not noAnadirFalse:
            listaComparacionLetras.append(False)    
    return listaComparacionLetras
        
isAnagram('amor','roma')        


