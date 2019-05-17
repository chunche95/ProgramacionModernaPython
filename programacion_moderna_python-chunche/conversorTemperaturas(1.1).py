# @Title: Creación de un conversor de temperaturas.
# @Description: Crear un programa que convierta la temperatura Farenhei a Celsius y viceversa. 
#               El programa pedirá que tipo de conversión queremos y la mostrará.
#               ~~~Restricciones~~~
#               - Se puede elegir el tipo de conversión en mayúsculas o minúsculas.
#               - Reducir el número de sentencias al mínimo y no repetir 'prints'.
#              ~~~~~~Retos~~~~~~
#               - Asegurar que las entradas son numéricas.
#               - Modificar el programa para que acepte grados kelvin ('K').
# @Version: 1.1
# @Author: Chunche
#
#
#  |~~~~~~~~~~~~~~~~~~~~~~~~~|
#  |     unidadM[C,F]        |  ----\                        ESTADO.
#  |     temperatura         |       > (Salida por pantalla de la temperatura convertida.)
#  |-------------------------|  ----/
#  |   mide(unid opcional)   | --> (medida)
#  | conversor(temp,inidadM) |
#  |_________________________|
#
#

class Termometro():
    def __init__(self):
        self.__unidadM = 'C'
        self.__temperatura = 0
    
    def __conversor(self, temperatura, unidad):
        if unidad == 'C':
            return "{} ºF".format(temperatura * 9/5 + 32)
        elif unidad == 'F':
            return "{} ºC".format((temperatura -32) * 5/9)
        else:
            return "Temperatura incorrecta!"

    def __str__(self):
        return "{}º {}".format(self.__temperatura, self.__unidadM)

    # Creacion de los getter y setter
    def unidadMedida(self, uniM=None):
        if uniM == None:
            return self.__unidadM
        else:
            if uniM == 'F' or uniM == 'C':
                self.__unidadM = uniM
    def temp(self, temperatura = None):
        if temperatura == None:
            return self.__temperatura
        else:
            self.__temperatura = temperatura
            
    def mide(self, uniM = None):
        if uniM == None or uniM == self.__unidadM:
            return self.__str__()
        else:
            return self.__conversor(self.__temperatura, self.__unidadM)




#t = Termometro()
# Unidades de medida
#print(t.unidadMedida())

# Inicializamos con una temperatura de entrada
#t.temp(32)

#Sacamos por pantalla la conversion del dato inicializado
#t.mide('F')
#t.mide('C')

# Ver conversion 
# print(t.__conversor(0,"C"))
# print(t.__conversor(32,"F"))




