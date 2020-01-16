# Importacion de las librerias necesarias.
import turtle

miT = turtle.Turtle()

# Realizamos los pasos que queremos que haga la 'tortuga'
############
# Bucle 1  #
############
# Creacion de una funcion para las repeticiones.

def cuadrado(lado):
    miT.forward(lado) # camina 50 'pasitos'
    miT.left(90)    # gira 90º
    # Camino 2
    miT.forward(lado)
    miT.left(90)
    # Camino 3
    miT.forward(lado)
    miT.left(90)
    # Camino 4
    miT.forward(lado)
    miT.left(90)


cuadrado(25)
# Giro
miT.left(90) # Giro para volver a empezar
cuadrado(50)
# Giro
miT.left(90) # Giro para volver a empezar
cuadrado(75)
# Giro
miT.left(90) # Giro para volver a empezar
cuadrado(100)
# Giro
miT.left(90) # Giro para volver a empezar
