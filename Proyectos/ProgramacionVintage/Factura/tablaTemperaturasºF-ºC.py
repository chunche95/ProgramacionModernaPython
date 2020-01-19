# Ejercicio while I - Tabla de temperaturas.
# 
# Construir un programa que muestre a peticion del usuario:
#   - La tabla de conversion de grados Centigrados en Fahrenheit desde 0 a 230 en multiplos de 10.
#   - La tabla de conversion de grados Fahrenheit a Centigrados desde 0 a 100 en multiplos de 100.
#
# F --> C
#  C=(F-32)*5/9
# C --> F
#  F= (C*9/5) + 32
#
# +Si entrada = 'C' 
# |  Centigrados (0,230)
# +Si entrada = 'F'
# | Fahrenheit (0,100)
# +Sino 
# | Error tipo incorrecto
# + Fin

import os
def fahrenheitToCelsius(g):
    f1 = (g- 32) * 5/9
    f2 = round(f1 ,2)
    return f2

def celsiusToFahrenheit(g):
    c1 = (g *9/5) -32
    c2 = round(c1 ,2)
    return c2

def centigrados(ini,fin):
    for grados in range(ini,fin+10, 10):
        print("{}ºF ===> {}ºC".format(grados, fahrenheitToCelsius(grados)))

def fahrenheit(ini,fin):
    for grados in range(ini,fin+10,10):
        print("{}ºC ===> {}ºF".format(grados, celsiusToFahrenheit(grados)))
def menu():
    
    
    
    print ("""
    Bienvenido a la tabla de conversion de Fahrenheit a Celcius y viceversa
    -----------------------------------------------------------------------
    
    Opciones disponibles:
     *  Fahrenheit a Celcius -> C")
     *  Celcius a Fahrenheit -> F")
     *  Salir del programa   -> S")
    \n""")

while True:
    os.system('cls' or 'clear')
    menu()
    salida = input("Opción: ")
    if salida == 'c' or salida == 'C':
        centigrados(0,230)
    elif salida == 'f'  or salida == 'F':
        fahrenheit(0,100)
    elif salida == "S" or salida =='s':
        print("Fin del programa, gracias por usar nuestra trabla de temperaturas...")
        break
    else:
        print("Error en el tipo de entrada, por favor vuelva a intentarlo")
    
print ("\n")
print("I´m Learning Python with KeepCoding, thanks!")
