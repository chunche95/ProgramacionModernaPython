edades = [12,23,43,54,13,2,4,45,65,76,5,6,78,9]

def mayores(edad):
    return edad >= 18;

entrar = list (filter(mayores, edades))
print(entrar)