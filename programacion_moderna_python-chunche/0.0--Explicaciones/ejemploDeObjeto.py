class Objeto():
    __atributoPrivado = None
    atributoPublico = None
    def __init__(self):
        self.__atributoPrivado = 0
        self.atributoPublico = "Atributo solicitado -- Soy público"
    
    def getAtributoPrivado(self):
        return self.__atributoPrivado
    def setAtributoPrivado(self, valor):
        self.__atributoPrivado = valor
    
    
    # Con este método el código queda más limpio y hace lo mismo que los dos métodos de arriba. (getAtributoPrivado y setAtributoPrivado).
    def atributoPrivado(self, valor=None):
        if valor == None:
            print("NO hay datos introducidos")
        else:
            print("Datos encontrados! ... Datos:", valor)
        
#Pruebas
        
o = Objeto()
# Muestro valor actual
print(o.getAtributoPrivado())
# Asigno (nuevo) valor al atributo
o.setAtributoPrivado(23)
# Muestro valor asignado
print(o.getAtributoPrivado())
# Ver atributo publico
print(o.atributoPublico)
# Ver atributo privado de la funcion
# o.__atributoPrivado # --> Cascotazo! XD
# Comprobacion de datos
o.atributoPrivado("Yo no sabia programar bien, antes")
