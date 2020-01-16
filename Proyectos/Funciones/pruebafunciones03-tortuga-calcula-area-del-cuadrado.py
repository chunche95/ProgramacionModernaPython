# Importacion de las librerias necesarias.
import turtle

# Realizamos los pasos que queremos que haga la 'tortuga'
############
# Bucle    #
############
# Creacion de una funcion para las repeticiones.

def cuadrado(lado):
    miT.forward(lado) # camina 50 'pasitos'
    miT.left(90)    # gira 90º
    # Camino 2
    miT.forward(lado)                    ###########
    miT.left(90)                         #  2 #  1 #
    # Camino 3                           #### >>####  
    miT.forward(lado)                    #  3 #  4 #
    miT.left(90)                         ###########
    # Camino 4
    miT.forward(lado)
    miT.left(90)
    # Devolvemos el resultado de la funcion
    return lado*lado 

# Inicializamos la variable de tortuga.
miT = turtle.Turtle()
##############################################################
#Creamos la tarea del calculo
area01 = cuadrado(25)
# Giro
miT.left(90) # Giro para volver a empezar
print (area01)
##############################################################
area02 = cuadrado(50)
# Giro
miT.left(90) # Giro para volver a empezar
print (area02)
##############################################################
area03 = cuadrado(75)
# Giro
miT.left(90) # Giro para volver a empezar
print (area03)
##############################################################
area04 = cuadrado(100)
# Giro
miT.left(90) # Giro para volver a empezar
print (area04)
##############################################################

