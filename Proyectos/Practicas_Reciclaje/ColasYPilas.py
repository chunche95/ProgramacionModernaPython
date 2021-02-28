cola = [1,2,3,5,6.7,8.8,9,9,2]
cola.append(256)
cola.append(10.4)
print(cola)

primero = cola.pop(0)
otro = cola.pop()
print(f"Valor de la cola es: {primero}")
print("Valor de var. otro es: {}".format(otro))
''' Insertamos en posicion 3 '''
cola.insert(3, 12)
print(cola)


listaNums = []
nombre= input("Introduzca su nombre: ")
edad = input("Introduzca su edad: ")
print (input (" Introduzca sus números de loteria a continuación. [Press ENTER]"))
for i in range(4):
    listaNums.append(input("Número: "))
print ("{} tiene {} y sus números de la ruleta son: {}".format(nombre, edad, listaNums))