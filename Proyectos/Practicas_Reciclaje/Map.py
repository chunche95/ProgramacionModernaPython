def doblar(numero):
    return numero*2

numeros = [1,2,3,4,43,4]

i = map(doblar, numeros)

print(i)

print(list(i))


j = map(lambda x : x*2, numeros)
print(j)
print(list(j))


a = [1,2,3.4,67, 9.9999]
b = [23,45,6,65,67]

k = map(lambda x,y : x*y, a,b)
print(k)
print(list(k))

