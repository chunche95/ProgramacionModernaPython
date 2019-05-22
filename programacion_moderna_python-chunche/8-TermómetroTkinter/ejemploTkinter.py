# @Title: Crear Termómetro Gráfico
# @Description: Creacion de un termometro con interfaz grafica de usuario, 
#
# Nota: En los proyectos tkinter principalmente suelen poner la palabra 'root' como objeto principal de inicio de los programas,
# sin embargo, puedo llamarlo como quiera.
#
# @Version: 1.0
# @Author: Chunche
#

from tkinter import *
from tkinter import ttk

#
# El constructor no necesita el metodo 'self' realmente, pero es recomendable, como una <<Buena práctica de programacion>>, python no necesita este paso
# pero otros lenguajes de programación si lo necesitan para trabajar.
# Además, en esta librería por defecto crea un método al que llama 'root' con lo cual, la clase que creamos llama a éste por defecto.
#

class mainApp():
    # Tamaño de la ventana a crear
    #size = "640x480" # Tamaño por defecto de la pantalla
    size = "1024x768"
    def __init__(self):
        # Ventana kinter
        self.root = Tk()
        # Tamaño de la pantalla
        self.root.geometry(self.size) # Llamo al método size declarado al inicio de la clase.
        self.root.title("Mi primera ventana")
        self.root.configure(bg = "lightblue")
    def start(self):
        self.root.mainloop()
if __name__ == '__main__':
    app = mainApp()
    # Creacion d ela ventana
    app.start()

