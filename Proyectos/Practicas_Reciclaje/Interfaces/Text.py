from tkinter import *;

root = Tk();

texto = Text(root)
texto.pack()
texto.config( width=30,height = 20, padx=15, pady=15, font=("Curier, 12"), 
selectbackground="gray")
label = Label ( root, text="Escribe aqui")
label.pack()
label.config(bg="gray", font="Curier, 18")



# Para que no cierre la ventana 
root.mainloop();
