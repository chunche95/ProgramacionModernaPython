from tkinter import *;

root = Tk();

frame = Frame(root);
frame.pack()

entrada1 = Entry(frame)
entrada1.pack()
entrada2 = Entry(frame)
entrada2.pack()
entrada3 = Entry(frame)
entrada3.pack()
entrada4 = Entry(frame)
entrada4.pack()


button1= Button( frame, text="Sumar")
button1.pack()
button2 = Button(frame, text="Restar")
button2.pack()

# Para que no cierre la ventana 
root.mainloop();
