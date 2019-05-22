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
        self.rb1 = ttk.Radiobutton(self, text="Fahrenheit", variable=self.tipoUnidad, value="F").place(x=20,y=60)
        self.rb2 = ttk.Radiobutton(self, text="Celsius", variable=self.tipoUnidad, value="C").place(x=20,y=80)
        
        
    def start(self):
        self.mainloop()

    def validateTemperature(self, *args):
         print(self.temperatura.get())
         nuevoValor = self.temperatura.get()
         try:
             float(nuevoValor)
             self.__temperaturaAnt = nuevoValor
         except:
             self.temperatura.set(self.__temperaturaAnt)
         

if __name__ == '__main__':
    app = mainApp()
    # Creacion d ela ventana
    app.start()
