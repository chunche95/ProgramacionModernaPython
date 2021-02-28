def genPares(limite):
    n = 1;
    lista = []
    while n < limite:
        yield n*2
        n+=1
devuelvePares = genPares(15)
print(next(devuelvePares))
print("Paro hasta que me llamen de nuevo")
print(next(devuelvePares))
print("Sino me llaman paro...")
print(next(devuelvePares))
print(next(devuelvePares))
print(next(devuelvePares))
print(next(devuelvePares))
print(next(devuelvePares))



def daPaises(*paises):
    for elemento in paises:
        yield from elemento

paises = daPaises("Brasil", "Argentina", "Colombia"," Venezuela", "España", "Japon")
print(next(paises))
print(next(paises))
print(next(paises))
print(next(paises))
print(next(paises))
print(next(paises))
