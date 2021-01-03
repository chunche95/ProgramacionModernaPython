# Creamos una clase galleta ---> Molde 
class Galleta:
    # Constructores
    # Inicializador
    def __init__(self, sabor, color, tamaño, peso):
        self.sabor = sabor;
        self.color = color;
        self.tamaño = tamaño;
        self.peso = peso;  
    # Métodos para el objeto galleta
    # Ingredientes de una galleta
    def ingredientes(self, azucar, dulce):
        self.__harina = True;
        self.azucar = azucar;
        self.__mantequilla = True;
        self.dulce = True;
    # Componentes que forman la galleta
    def cocinar(self):
        if(self.tamaño == "Medio" or self.sabor == "Chocolate"):
            self.azucar = 2;
            self.dulce = True;
        elif(self.tamaño == "Pequeña" or self.sabor == "Leche"):
            self.mantequilla = False;
            self.dulce = False;
        else:
            self.mantequilla = True;
            self.azucar = 0.5;
            self.dulce = True
        # print('''
        # Especificaciones de sabor:
        # Es de {},
        # tiene color {},
        # es de tamaño {}.        
        # '''.format(self.sabor, self.color, self.tamaño));
        
    # Definimos el constructor de STR para escribir la salida por pantalla con todos los constructores juntos
    def __str__(self):
        return (""" COOKIES BASE
        Su pedido tiene sabor {}, de color {} y su tamaño de fabricacion es {}. Los ingredientes son:
        - Harina: {}
        - Azucar: {}
        - Mantequilla: {}
        - Dulce: {}
    Peso neto: {} g
    """.format(self.sabor, self.color, self.tamaño, self.__harina, self.azucar, self.__mantequilla, self.dulce, self.peso))

    
# Instanciamos la clase
galleta1 = Galleta("Chocolate", "Marrón", "Medio", 2);
# Mostramos en pantalla
print(galleta1.cocinar());
print(galleta1.ingredientes(1, False));
print(str(galleta1));

class Pastel(Galleta):
    def tarta(self,alturas,forma):
        self.alturas = alturas;
        self.forma = forma;
        print (''' PASTEL
        - Alturas: {}
        - Forma: {}
        '''.format(self.alturas, self.forma))
tartaCumple = Pastel("Merengue", "Rosa", "Mediana", 5);
tartaCumple.ingredientes(10,True);
tartaCumple.cocinar()

print(str(tartaCumple),tartaCumple.tarta(3,"Circulo"));