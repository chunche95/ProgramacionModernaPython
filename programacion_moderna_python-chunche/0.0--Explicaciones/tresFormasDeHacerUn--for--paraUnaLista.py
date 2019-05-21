# @Title: Ciclo for, recorriendo listas
# @Description: Formas de recorrer una lista con un bucle 'for'.
# @Author: Chunche
lista=("Pantalla","Teclado","Raton","Disco","LED's","USB","Altavoces")
# Primero --> Conozco la longitud de la lista
for i in range (0,4):
    print(lista[i])
print ("+++++++++++")
# Segundo --> Llamo a la sentencia de la longitud para que cuente la lista de objetos
for i in range ( 0, len(lista)):
    print(lista[i])
print ("+++++++++++")
# Tercera --> Llamo la lista, se cuenta y se imprime todo en conjunto
for regalo in lista:
    print(regalo)
print ("+++++++++++")