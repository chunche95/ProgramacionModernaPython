# Pte de ver/saber esta parte








def SumatorioDobleClasico(l):
    resultado = 0
    for valor in l:
        resultado += valor *2
    return resultado

def ProductoTotal(l):
    resultado=1
    for valor in range l:
        resultado *=valor
    return resultado

lista = [1,4,56,8,-4]

sumatorio = reduce(lambda x,y: x + y, lista)
# Creo una copia de la lista
l = lista[:]
# Añado el neutro para la sima en la posición cero.
l.insert(0,0)
sumatorioDobles = reduce(lambda x,y: x+y*2,l)

print(sumatorio)
print(sumatorioDobles)






