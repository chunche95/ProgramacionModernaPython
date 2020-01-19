# Creamos una función para la validación de los datos de entrada
def esDecimal(numero):
    try:
        float(numero)
        return True
    except:
        return False

# Entrada de parámetros:
B = input ("Base del triangulo: ")
if esDecimal(B):
    # Guardamos y convertimos los valores de entrada.
    b = float(B)
    
    H = input ("Altura del triangulo: ")
    if esDecimal(H):
        # Guardamos y convertimos los valores de entrada.
        h = float(H)
            # Realizamos la operacion de cálculo.
        area = ((b * h) / 2)
        # Saco por pantalla el resultado.
        print("Superficie del triángulo es: ", area)
    else:
        print(H,"<-- Debe ser un número. ")
        quit()

else:
    print(B,"<-- Debe ser un número. ")
    quit()




#        (algoritmo del triangulo)
#                    |
#                 (base)
#                    |
#                (base = numero)
#                    |
#        |----------------------|
#        |                      |
#        V                      V
#     (error base)          (altura)
#        |                      |
#        |               (altura = numero)
#        |                      |
#        |       |-------------------------|
#        |   (error altura)        (A<-- base * altura / 2)
#        |                                 |
#        |                                 V
#        |                                (A)
#        |                                 |
#        L-------fin dle algoritmo)--------|
#                