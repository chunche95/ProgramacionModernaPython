# Description: Inicio de creacion de clases en python
# Version: 1.0
# Author: Chunche


class Perro():
    # Siempre es necesario iniciar la funcion __init__ para los metodos de la clase
    def __init__(self, n , e, p):
        self.nombre = n
        self.edad = e
        self.peso = p
    # Funciones metodos que no se definen en el init pero si pertenecen a la clase 'perro'
    def ladrar(self):
        if self.peso >= 8:
            print("GUAU, GUAU")
        else:
            print("guau guau")
    
    # Sirve para redefinir la variable, en este caso la variable nombre
    def __str__(self):
        return "Soy el perro {}".format(self.nombre)
    # Un uso más adecuado para cuando se hacen 'debugs' (por ejemplo)
    def __str__(self):
        return "Perro {}, e: {}, p: {}".format(self.nombre,self.edad,self.peso)
    