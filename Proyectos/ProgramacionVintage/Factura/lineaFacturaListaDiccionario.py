# Constantes
_UNIDADES = 1
_PRECIO = 0

cadenaUnidades = input("Cantidad: ")
unidades = float(cadenaUnidades)

cadenaPrecio = input("Precio Unitario (€): ")
precio = float(cadenaPrecio)

totalItems = 0
precioTotal = 0

listaPrecios = []
listaUnidades = []

listaLineasFact= []
while unidades > 0 and precio > 0:
    totalUnitario = unidades * precio
    item = dict()
    item['precio'] = precio
    item['unidades']= unidades
    
    listaPrecios.append(item)
    
    totalItems += unidades
    precioTotal += totalUnitario
    
    cadenaUnidades = input("Cantidad: ")
    unidades = float(cadenaUnidades)
    cadenaPrecio = input("Precio unitario (€) : ")
    precio = float(cadenaPrecio)

for item in listaPrecios:
    print(item['precio'], " € - ", item['unidades'], " unidades - ", item['unidades'] * item['precio'] , " € \n")


print("------------------------------")
print("Total:          ", precioTotal , " €")
print("Unidades:       ",totalItems   , " Items")




