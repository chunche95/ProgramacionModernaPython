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
else:
    print("Debe ser un número. ")
    quit()
H = input ("Altura del triangulo: ")
if esDecimal(H):
    # Guardamos y convertimos los valores de entrada.
    h = float(H)
else:
    print("Debe ser un número. ")
    quit()

# Realizamos la operacion de cálculo.
area = ((b * h) / 2)

# Saco por pantalla el resultado.
print("Superficie del triángulo es: ", area)
