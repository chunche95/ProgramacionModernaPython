cadenaUnidades = input("Cantidad: ")
unidades = float(cadenaUnidades)

cadenaPrecio = input("Precio Unitario (€): ")
precio = float(cadenaPrecio)

totalItems = 0
precioTotal = 0

listaPrecios = []
listaUnidades = []

cadenaAImprimir= "\n"
while unidades > 0 and precio > 0:
    totalUnitario = unidades * precio
    listaPrecios.append(precio)
    listaUnidades.append(unidades)
    
    totalItems += unidades
    precioTotal += totalUnitario
    
    cadenaUnidades = input("Cantidad: ")
    unidades = float(cadenaUnidades)
    cadenaPrecio = input("Precio unitario (€) : ")
    precio = float(cadenaPrecio)

for precio, unidades in zip(listaPrecios, listaUnidades):
    print(precio, " € - ", unidades, " unidades - ", precio * unidades , " € \n")


print("------------------------------")
print("Total:          ", precioTotal , " €")
print("Unidades:       ",totalItems   , " Items")


