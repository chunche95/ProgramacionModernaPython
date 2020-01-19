cadenaUnidades = input("Cantidad: ")
unidades = float(cadenaUnidades)

cadenaPrecio = input("Precio Unitario (€): ")
precio = float(cadenaPrecio)

totalItems = 0
precioTotal = 0
cadenaAImprimir= "\n"
while unidades > 0 and precio > 0:
    totalUnitario = unidades * precio
    cadenaAImprimir += str(precio) + " € - " + str(unidades) + " Unidades - " + str(totalUnitario) + " € \n"
    # cadenaAImprimir += "{}€ - {} unidades - {}€ \n".format(precio,unidades)
    # print(precio, " € - ", unidades, " Unidades - ", totalUnitario, "€")
    
    totalItems += unidades
    precioTotal += totalUnitario
    
    cadenaUnidades = input(" Cantidad: ")
    unidades = float(cadenaUnidades)
    cadenaPrecio = input("Precio unitario (€) : ")
    precio = float(cadenaPrecio)

print(cadenaAImprimir)
print("------------------------------")
print("Total:          ", precioTotal , " €")
print("Unidades:       ",totalItems   , " Items")
