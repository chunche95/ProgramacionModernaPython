# Pedida de datos
strunidades = input ("Cantidad: ")
strprecio = input("Precio unidad €: ")
# Conversion de unidades string a float
unidades = float(strunidades)
precio = float(strprecio)
# Inicio de las variables
totalItems=0
precioTotal=0

#Bucle While
while unidades > 0 and precio > 0:
# Operacion del bucle -- "de la lista de la factura" -- imprime linea a linea.
    totalUnitario = unidades * precio
    print ("Precio ", precio, "€ - Cantidad: ", unidades,"- Total: ", totalItems,"€")
    
    totalItems += unidades # totalItems = totalItems + unidades
    precioTotal += totalUnitario
    
    strunidades = input ("Cantidad: ")
    strprecio = input("Precio unidad €: ")
    # Conversion de unidades string a float
    unidades = float(strunidades)
    precio = float(strprecio)
    
print("----------------------------------")
print("Total:", precioTotal)
print("Unidades:", totalItems)