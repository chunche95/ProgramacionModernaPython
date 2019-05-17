# @Title: Creación de un conversor de temperaturas.
# @Description: Crear un programa que convierta la temperatura Farenhei a Celsius y viceversa. 
#               El programa pedirá que tipo de conversión queremos y la mostrará.
#               ~~~Restricciones~~~
#               - Se puede elegir el tipo de conversión en mayúsculas o minúsculas.
#               - Reducir el número de sentencias al mínimo y no repetir 'prints'.
#
# @Version: 1.0
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
    
    def conversor(self, temperatura, unidad):
        if unidad == 'C':
            return "{} ºF".format(temperatura * 9/5 + 32)
        elif unidad == 'F':
            return "{} ºC".format((temperatura -32) * 5/9)
        else:
            return "Temperatura incorrecta!"

    def __str__(self):
        return "{} º {}".format(self.temperatura, self.unidad)

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
        if uniM == None or uniM == self.unidadM:
            return self.__str__()
        else:
            return self.conversor(self.temperatura, uniM)

# Creacion de un objeto de tipo termometro llamado 'c'.
c = Termometro()
# Conversion
print(c.conversor(0,"C"))
print(c.conversor(32,"F"))



