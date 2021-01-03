class ModuloPrincipal:
    
    def __init__(self, obligatorias, opcionales):
        self.obligatorias = obligatorias;
        self.opcionales = opcionales;
    def asignaturas(self):
        print("Asignaturas obligatorias: ", self.obligatorias);
        print("Asignaturas opcionales: ",self.opcionales);

