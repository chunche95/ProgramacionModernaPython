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
    def ingredientes(self, harina, azucar, mantequilla, dulce):
        self.harina = True;
        self.azucar = 1.2;
        self.mantequilla = True;
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
        print('''
        La galleta es de {},
        tiene color {},
        es de tamaño {}.        
        '''.format(self.sabor, self.color, self.tamaño));
    # Definimos el constructor de STR para escribir la salida por pantalla con todos los constructores juntos
    def __str__(self):
        return """La galleta es de sabor {}, de color {} y su tamaño de fabricacion es {}. Los ingredientes son:
        - Harina: {}
        - Azucar: {}
        - Mantequilla: {}
        - Dulce: {}
    Peso neto: {} g
        """.format(self.sabor, self.color, self.tamaño, self.harina, self.azucar, self.mantequilla, self.dulce, self.peso)
    def __del__(self):
        print("Galleta terminara y expuesta");
# Instanciamos la clase
galleta1 = Galleta("Chocolate", "Marrón", "Medio", 2);
# Mostramos en pantalla
print(galleta1.cocinar());
print(galleta1.ingredientes(True, 1, True, False));
print(str(galleta1));