# Description: Creacion de clases con herencia en python - Usando la clase perro.
# Version: 1.2
# Author: Chunche

# Clase sin argumentos de entrada
class Dog():
    # Siempre es necesario iniciar la funcion __init__ para los metodos de la clase
    def __init__(self):
        self.nombre = ""
        self.edad = None
        self.peso = None
    # Funciones metodos que no se definen en el init pero si pertenecen a la clase 'perro'
    def ladrar(self):
        if self.peso == None:
            print("Soy un fantasma! Booh!")
        if self.peso >= 8:
            print("GUAU!! GUAU!!")
        else:
            print("guau! guau!")
    
    # Sirve para redefinir la variable, en este caso la variable nombre
    #   def __str__(self):
    #      return "Soy el perro {}".format(self.nombre)
    # Un uso más adecuado para cuando se hacen 'debugs' (por ejemplo)
    def __str__(self):
        return "Perro {}, edad: {}, peso: {}".format(self.nombre,self.edad,self.peso)

# Clase con definicion de atributos, (n,e,p).
class Perro():
    # Siempre es necesario iniciar la funcion __init__ para los metodos de la clase
    def __init__(self, n , e, p):
        self.nombre = n
        self.edad = e
        self.peso = p
    # Funciones metodos que no se definen en el init pero si pertenecen a la clase 'perro'
    def ladrar(self):
        if self.peso >= 8:
            print("GUAU!!!, GUAU!!!")
        else:
            print("guau! guau!")
    
    # Un uso más adecuado para cuando se hacen 'debugs' (por ejemplo)
    def __str__(self):
        return "Perro {}, edad: {}, peso: {}".format(self.nombre,self.edad,self.peso)
 

# Herencia de los métodos de la clase Perro
class PerroAsistente(Perro):
    # Definicion del cosntructor
    def __init__(self, nombre, edad, peso, amo):
        Perro.__init__(self, nombre, edad, peso)
        self.amo = amo
        self.__trabajando = False # Ahora es un atributo privado
    # Sobreescribir un método
    def __str__(self):
        return "Perro de asistencia de {}".format(self.amo)
    # Definicion de nuevos métodos propios de la nueva clase
    def pasear(self):
        print("{} ayudo a mi dueño {} a paser".format (self.nombre, self.amo))
    
    def ladrar(self):
        if self.trabajando:
            print("Ssshhh, no puedo ladrar")
        else:
            Perro.ladrar(self)
            
    # Creacion de un método getter y setter para acceder a un atributo privado.
     def trabajando(self, valor=None):
         if valor == None:
             return self.__trabajando
        else:
            self.__trabajando = valor
