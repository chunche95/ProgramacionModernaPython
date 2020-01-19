suma=0
contador=1

while contador <= 100:
    suma +=contador
    contador = contador+1
    
print ("Total ", suma)

"""
La suma de calcula de forma "rapida" sabiendo que:
1 + 100 = 101
2 + 99  = 101
3 + 98  = 101
[...]
50 + 51 = 101

Como son 50 parejas de numeros y todos ellos su suma es 101, tenemos que:

50 * 101 = 5050
"""