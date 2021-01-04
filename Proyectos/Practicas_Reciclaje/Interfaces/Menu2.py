from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

# ###################################################################    
def abrir():
    archivo = filedialog.askopenfilename(title="Abrir")
    print(archivo)
def salir():
    i = messagebox.askquestion("Salir", " ¿Seguro desea salir?")
    if i == "yes":
        root.destroy()
def acerca():
    messagebox.showinfo("Informacion", """  ACERCA DE.
    
    Programita de interfaces gráficas en Python
    Se desarrolla e este caso una sección con alertas y mensajes por pantallas emergentes haciendo uso de la libreria 'tkinter'.
    Curso de 13h - Python 3 de 0.
    Creado por Brian De Vita. 

        [
            * El contenido de estos ficheros se amplia con Advanced Python - 1h
            * Network Automation with Python and Ansible - 4h
            * Python for Data Science - 22h
            and 
            * Bootcamp Ultimate Python - 16h
        ]
    
    @url: https://paulinobermudez.github.io/home/
    @LinkedIn: https://www.linkedin.com/in/paulinoestebanbr
    
    @Author: Paulino Esteban Bermúdez R.

    Licencia: 2021.
    """)

def actualizaciones():
    messagebox.showinfo("Actualizaciones", "Actualmente no hay actualizaciones disponibles.")

def error():
    messagebox.showerror("Error", "Se ha producido un error inesperado, la acción no se ha podido realizar")

def deshacer():
    i = messagebox.askquestion("Deshacer", "¿Desea deshacer todos los cambios?")
    if i == "yes":
        messagebox._show("Terminado", "Dehechos los cambios...")

# ###################################################################    
root = Tk()

barraMenu = Menu(root)

root.config(menu=barraMenu)

archivoMenu=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
archivoMenu.add_command(label = "Abrir archivo", command=abrir)
archivoMenu.add_separator()
archivoMenu.add_command(label = "Nuevo archivo")
archivoMenu.add_command(label = "Nueva ventana", command = error)
archivoMenu.add_command(label = "Nuevo fichero")
archivoMenu.add_separator()
archivoMenu.add_command(label = "Salir", command=salir)


archivoEditar = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label = "Editar", menu= archivoEditar)
archivoEditar.add_command(label = "Deshacer", command = deshacer)
archivoEditar.add_command(label = "Rehacer")

archivoAyuda = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label = "Ayuda", menu= archivoAyuda)
archivoAyuda.add_command(label = "Buscar actualizaciones", command=actualizaciones)
archivoAyuda.add_command(label = "Acerca de", command=acerca)



root.mainloop()