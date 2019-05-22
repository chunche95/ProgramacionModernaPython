# @Title: Creación de termómetro con Tkinter.
# @Description: Creación del termometro de conversion de Farhenheit a Celsius usando Tkinter.
# @Version: 1.0
# @Author: Chunche

'''
 Esquema:
    
    +--------------------------------------------+
    |           TERMOMETRO    ______             |
    |         +--------------+      |            |
    |         |  123 {Entry} |      |            |
    |         +--------------+      |            |
    |                               |> Widgets   |
    |         Grados:  {Label}      |            |
    |           o F                 |            |
    |           o C           ______|            |
    |                                            |
    |                                            | --> Tk()
    |                                            |
    +--------------------------------------------+


'''


from tkinter import *
from tkinter import ttk

class mainApp(Tk):
    entrada = None
    tipoUnidad = None
    
    __temperaturaAnt = ''
    
    def __init__(self):
        Tk.__init__(self)
        self.title("Termómetro")
        # Tamaño de la pantalla
        self.geometry("180x130")
        # Color de fondo
        #self.configure(bg="#DED798")
        # Evitar la rendimension
        self.resizable(0,0)
        
        # Variables de control: Variables que responden a eventos, controlan cambios
        self.temperatura = StringVar(value="")
        self.temperatura.trace("w", self.validateTemperature) # write,read,unset
        self.tipoUnidad = StringVar(value="F")
        
        # Creacion del método que hace el diseño
        self.createLayout()
        
    def createLayout(self):
        self.entrada = ttk.Entry(self, textvariable=self.temperatura).place(x=15, y=15) # --> cuadrado almacenado en memoria. {Entry}
        # Texto de 'Grados:'
        self.lblUnidad = ttk.Label(self, text="Grados:").place(x=15, y=45)
        # Botones
        self.rb1 = ttk.Radiobutton(self, text="Fahrenheit", variable=self.tipoUnidad, value="F", command=self.selected).place(x=20,y=60)
        self.rb2 = ttk.Radiobutton(self, text="Celsius", variable=self.tipoUnidad, value="C", command=self.selected).place(x=20,y=80)
        
        
    def start(self):
        self.mainloop()

    def validateTemperature(self, *args):
         print(self.temperatura.get())
         #for item in args:
         #    print(item)
         #print(args[0])
         #print(args[1])
         
         nuevoValor = self.temperatura.get()
         print("Nuevo Valor: ", nuevoValor , " vs valor Anterior" , self.__temperaturaAnt)
         try:
             float(nuevoValor)
             self.__temperaturaAnt = nuevoValor
             print("EEEY! Fijamos Valor anterior: ", self.__temperaturaAnt)
         except:
             self.temperatura.set(self.__temperaturaAnt)
             print("CHEEE! OJO! Recuperando Valor anterior: ", self.__temperaturaAnt)
             
             
    def selected(self):
        resultado = 0
        toUnidad = self.tipoUnidad.get()
        grados = float(self.temperatura.get())
        
        if toUnidad == 'F':
            resultado = grados * 9/5 + 32
        elif toUnidad == 'C':
            resultado = (grados - 32 ) * 5
        else:
            print("No se ha seleccionado ni 'C' ni 'F'")
            resultado = grados
        # Devolvemos el valor convertido
        self.temperatura.set(resultado)

if __name__ == '__main__':
    app = mainApp()
    # Creacion d ela ventana
    app.start()
