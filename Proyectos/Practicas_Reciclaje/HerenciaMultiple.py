class Altavoces:
    def potencia(self,potencia):
        self.potencia  = potencia;
        print("Potencia de altavoces: {} W".format(potencia));
class Monitores:
    def marco(self, tipoPantalla, tamaño):
        self.tipoPantalla = tipoPantalla;
        self.tamaño = tamaño;
        print("Tipo de pantalla: {} \nTamaño: {}''".format(tipoPantalla, tamaño));
class SmartTV(Altavoces, Monitores): 
    def tdt(self, androidTV, mando):
        self.androidTV = androidTV;
        self.mando = mando;
        print("Android TV: {} \nContiene mando: ".format(androidTV, mando));

print("="*30,"Altavoces","="*30);
energySystem = Altavoces();
energySystem.potencia(60);
print("="*30,"Monitores","="*30);
msi = Monitores = Monitores();
msi.marco("Curva", 27);
print("="*30,"SMART TV","="*30);
sony = SmartTV();
sony.marco("Plana", 55);
sony.potencia(40);
sony.tdt(True,True);

