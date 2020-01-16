def esMedia(lista):
    suma = 0
    for n in lista:
        suma += n
    return suma/len(lista)

def calculaMedia(*items):
    suma = 0
    for n in items:
        suma += n
    return suma/len(items)