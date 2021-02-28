from tkinter import *;

root = Tk();

root.title("HC3.0")
root.resizable(1,1);
'''root.iconbitmap("logo.ico");'''

miFrame = Frame(root)
#miFrame.pack(side=BOTTOM, anchor="w")
miFrame.pack(fill="x", expand=1)
miFrame.pack(fill="y", expand=-1)
miFrame.config(width=780, height= 560)
miFrame.config(cursor="pirate")
miFrame.config(bg="gray")
miFrame.config(bd="20")
miFrame.config(relief="ridge")


root.config(cursor="boat")
root.config(bg="blue")
root.config(bd="15")
root.config(relief="sunken")


# Para que no cierre la ventana 
root.mainloop();
