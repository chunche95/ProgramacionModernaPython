'''
Description: First commit in console for git
Version: 1.0
Author: Chunche
'''

def cuentaNum(numero):
    contador = 0
    for i in range(0, numero+1):
        contador += 1
    
    return contador

print(cuentaNum(1000))
print(list(range(0, 101)))
print(list(range(0, 101, 2)))