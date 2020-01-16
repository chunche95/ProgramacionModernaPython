import sys

print(__name__)

def area(b,h):
    return ((b*h)/2)
# Ejecucion como modulo principal
if __name__ = '__main__':
    if len(sys.argv) >= 3:
        base = float(sys.argv[1])
        altura = float(sys.argv[2])
    else:
        # Sino se llegan a 3 parametros, pido los datos por teclado 
        base =  float(input("Base: "))
        altura = float(input("Altura: "))
 
     print("Superficie: {}".format(area(base,altura))