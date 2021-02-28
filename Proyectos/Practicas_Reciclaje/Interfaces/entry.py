from tkinter import *;

root = Tk();

frame = Frame(root, width=800,height = 600)
frame.pack();

entrada = Entry(frame)
entrada.grid(row=0, column=1, sticky="w", padx=5, pady=5)
entrada.config(justify="center", state = "normal")

entrada2 = Entry(frame)
entrada2.grid(row=1, column=1, sticky="w", padx=5, pady=5)
entrada2.config(justify="center")

entrada3 = Entry(frame)
entrada3.grid(row=2, column=1, sticky="w", padx=5, pady=5)
entrada3.config(justify="center", show="*")


label1 = Label(frame, text="Nombre");
label1.grid(row=0, column=0, sticky="w", padx=5, pady=5)

label2 = Label(frame, text="Apellido");
label2.grid(row=1, column=0, sticky="w", padx=5, pady=5)

label3 = Label(frame, text="Password");
label3.grid(row=2, column=0, sticky="w", padx=5, pady=5)


# Para que no cierre la ventana 
root.mainloop();
