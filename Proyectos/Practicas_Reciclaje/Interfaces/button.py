from tkinter import *;


def sumar():
    resultado.set(int(v1.get()) + int(v2.get()) + int(v3.get()))

def restar():
    resultado.set(int(v1.get()) - int(v2.get()) - int(v3.get()))


root = Tk();

frame = Frame(root);
frame.pack()

v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
resultado = StringVar()

entrada1 = Entry(frame)
entrada1.pack()
entrada1.config(bd=10, font=("Curier 20"), textvariable = v1)

entrada2 = Entry(frame)
entrada2.pack()
entrada2.config(bd=10, font=("Curier 20"), textvariable = v2)

entrada3 = Entry(frame)
entrada3.pack()
entrada3.config(bd=10, font=("Curier 20"), textvariable = v3)

entrada4 = Entry(frame)
entrada4.pack()
entrada4.config(bd=10, font=("Curier 20"), state="disable", textvariable = resultado)


button1= Button( frame, text="Sumar")
button1.pack()
button1.config(bd=5, font=("Curier 20"), command = sumar)

button2 = Button(frame, text="Restar")
button2.pack()
button2.config(bd=5, font=("Curier 20"), command = restar)

# Para que no cierre la ventana 
root.mainloop();
