# Operadores logicos
# la tupla toma los valores:
#   Clave ==> Valor
#     A        1
#     B        2
#    ...      ...

# Creo la lista
tupla = ('A','B','C','D','E','F','G','H','I')
# Inicio un contador
indice = 0

# Genero un bucle while para eliminar las letras con valores 3,6,9
# Leo la lista 
# while indice < len(tupla):
#    # Condicional que me elimina los valores 2,6,9 de la tupla
#    if indice+1 == 2 or indice+1 == 6 or indice+1 == 9:
#        mataletra()
#    indice += 1
        



# Creo un bucle que lea la lista tantas veces como sea necesario hasta que su valor sea igual o menor que la longitud total de la tupla
while indice <= len(tupla):
    # Creo un condicional que saque por pantalla las claves que cumplan la condicion
    if (indice +1) % 2 == 0:
        # Imprimo por pantalla el valor de la clave
        print(tupla[indice])
    # Incremento en valor del indice para que vaya sumando y no cree un bucle infinito
    indice += 1
