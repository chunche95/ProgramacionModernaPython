print(__name__)
def area(b,h):
    return ((b*h)/2)

if __name__ == '__main__':
    base =  float(input("Base: "))
    altura = float(input("Altura: "))
 
    print(area(base, altura))