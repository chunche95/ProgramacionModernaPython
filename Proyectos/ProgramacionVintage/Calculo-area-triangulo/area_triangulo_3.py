# Creamos una función para la validación de los datos de entrada
def esDecimal(numero):
    try:
        float(numero)
        return True
    except:
        return False

# Entrada de parámetros con validación de los datos de entrada: 
B = input ("Base del triangulo: ")
while not esDecimal(B):
    print(B,"<-- Debe ser un número. ")
    B = input ("Base del triangulo: ")
H = input ("Altura del triangulo: ")
while not esDecimal(H):
    print(H,"<-- Debe ser un número. ")
    H = input ("Altura del triangulo: ")
    
# Guardamos y convertimos los valores de entrada.    
b = float(B)
# Guardamos y convertimos los valores de entrada.
h = float(H)
# Realizamos la operacion de cálculo.
area = ((b * h) / 2)
# Saco por pantalla el resultado.
print("Superficie del triángulo es: ", area)
    


#        (algoritmo del triangulo)
#                    |
#      ----------->(base)
#      |              |
#      |        (NO esDecimal) ----| [False]
#      |              |            |
#      |        (error base)       |
#      |              |            |
#      |           (base)          |
#      |____________I              |
#                                  |
#                                  |
#                                  V
#                    --------->(altura)
#                    |             |
#                    |        (NO esDecimal)-| [False]
#                    |             |         |
#                    |             V         |
#                    |       (error altura)  |
#                    |             |         |
#                    |             V         |
#                    |          (altura)     |
#                    |_____________|         |
#                                            |
#                                  |---------|
#                                  |
#                                  V
#                       (A<-- base * altura / 2)
#                                  |
#                                  V
#                                 (A)
#                                  |
#                         (fin dle algoritmo)
#                
