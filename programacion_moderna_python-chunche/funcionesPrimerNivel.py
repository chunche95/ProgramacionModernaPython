# Multiplicacion de 1 en 1
def normal(x):
    return x
# Multiplicacion del cuadrado
def cuadrado(x):
    return x * x
# Multiplicacion del cubo
def cubo(x):
    return (x**3)

def sumaTodos(limitTo, f):
    resultado = 0
    for i in range(limitTo+1):
        resultado += f(i)
    return resultado

# Se ejecuta esta zona si se lanza como programa principal
if __name__ == '__main__':
    print(sumaTodos(100, normal))
    print(sumaTodos(4, cuadrado))
    print(sumaTodos(6, cubo))
