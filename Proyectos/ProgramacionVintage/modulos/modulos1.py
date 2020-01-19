import anagramas
from math import factorial as fact

p1 = input("Una palabra: ")
p2 = input("Otra palabra: ")

if anagramas.isAnagramDic(p1,p2):
    print("Son anagramas!")
else:
    print("No son anagramas!")
    
    
print ("PI vale: ".format(math.pi))
n = input ("Numero: ")

print(math.factorial(int(n)))

print(fact(int(n)))
