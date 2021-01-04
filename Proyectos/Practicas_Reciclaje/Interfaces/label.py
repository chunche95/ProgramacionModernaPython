from tkinter import *;

root = Tk();


miTexto = StringVar()
miTexto.set("Python Programs --->")

root.title("HC3.0")
root.resizable(1,1);
root.config(width=900, height=670)

label = Label(root, text="Hola humano!")
label.place(x=100,  y = 50)
label.config(bg="red", fg="white", font=("Curier", 50))


label = Label(root, text="Terrícola prehistórico!")
label.place(x=250,  y = 200)
label.config(bg="green", fg="pink", font=("Tahoma", 50),
textvariable=miTexto)

frame = Frame(root, width=700,height = 500)
frame.pack();

entrada = Entry(frame)
entrada.pack()


label = Label(frame, text="Nombre")
label.pack()


# Para que no cierre la ventana 
root.mainloop();
