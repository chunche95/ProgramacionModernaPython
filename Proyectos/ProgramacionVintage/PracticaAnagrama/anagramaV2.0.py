def comparaLetras(p1,p2):
    import sys
    
    anagrama = True
    coincidencia = 0
    if len(p1) == len(p2):
        caracter1 = list(p1)
        caracter1.sort()
        caracter2 = list(p2)
        caracter2.sort()
        
        posicion1 = 1
        for posicion1 in range(len(p1)):
            if caracter1[posicion1] == caracter2[posicion1]:
                anagrama = True
            else:
                anagrama = False
    return anagrama

print(comparaLetras('minions' , 'snoinim'))