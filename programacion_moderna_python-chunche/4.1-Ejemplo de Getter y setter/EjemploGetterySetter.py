class ClaseConGetterySetter():
    def __init__(self):
        self.__propiedadPrivada = None
    # Definicion de un setter --> Asigno un valor
    def setPropiedadPrivada(self, valor):
        self.__propiedadPrivada = valor
    # Definicion de un getter --> Me devuelve el valor que tiene la variable definida
    def getPropiedadPrivada(self):
        return self.__propiedadPrivada
    # Getter y setter en conjunto
    def propiedad_Privada(self, valor=None):
        if calor==None:
            return self.__propiedadPrivada
        else:
            self.__propiedadPrivada = valor
                
    
    def __str__(self):
        return "Clase con getter y setter con propiedad privada: {}".format(self.__propiedadPrivada)

if __name__ == '__main__':
    c = ClaseConGetterySetter()
    
############
# Pruebas: #
############
v = ClaseConGetterySetter()
laV = v.getPropiedadPrivada() # --> Me da el valor actual, laV= None
print(laV)
laV = v.setPropiedadPrivada(25) # --> Asigno el valor 25 a 'v'
print(laV)
laV = v.getPropiedadPrivada() # --> Me da el valor actual de 'v', v=25
print(laV)