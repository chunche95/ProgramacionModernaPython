suma=0
# range no incluye el ultimo numero que se le indica, por ello se ha de sumar +1 si quiero que
# sume los 100 primeros números.
for contador in range(1, 101):
    suma+=contador
    
print (suma)