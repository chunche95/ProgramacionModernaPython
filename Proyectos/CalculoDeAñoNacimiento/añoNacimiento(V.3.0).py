nombre = input ("¿Cómo te llamas? ")
print("Hola ", nombre)
strEdad = input ("¿Cuántos años tienes? ")
strAnno = input ("¿En qué año estamos? ")
strMes = input ("¿En qué mes estamos? ")
strDia = input ("¿En qué dia estamos? ")

edad = int(strEdad)
anno = int(strAnno)
mes = int(strMes)
dia = int(strDia)

mes28 = 28 # Mes con 28 dias
mes30 = 30 # Mes con 30 dias
mes31 = 31 # Mes con 31 dias

if mes == 1:
    transcurridos = dia
elif mes == 2:
    transcurridos = mes31 + dia
elif mes == 3:
    transcurridos = mes31 + mes28 + dia
elif mes == 4:
    transcurridos = mes31 + mes28 + mes31 + dia
elif mes == 5:
    transcurridos = mes31 + mes28 + mes31 + mes30 + dia
elif mes == 6:
    transcurridos = mes31 + mes28 + mes31 + mes30 + mes31 + dia
elif mes == 7:
    transcurridos = mes31 + mes28 + mes31 + mes30 + mes31 + mes30 + dia
elif mes == 8:
    transcurridos = mes31 + mes28 + mes31 + mes30 + mes31 + mes30 + mes30 + dia
elif mes == 9:
    transcurridos = mes31 + mes28 + mes31 + mes30 + mes31 + mes30 + mes30 + mes31 + dia
elif mes == 10:
    transcurridos = mes31 + mes28 + mes31 + mes30 + mes31 + mes30 + mes30 + mes31 + mes30 + dia
elif mes == 11:
    transcurridos = mes31 + mes28 + mes31 + mes30 + mes31 + mes30 + mes30 + mes31 + mes30 + mes31 + dia
elif mes == 12:
    transcurridos = mes31 + mes28 + mes31 + mes30 + mes31 + mes30 + mes30 + mes31 + mes30 + mes31 + mes30 + dia
# GuardaDiasPasados= Ene  + Feb   + Mar   + Abr   + May   + Jun   + Jul   + Ago   + Sep   + Oct   + Nov   + Dic 
else:
    print("Error! Hay un error en la entrada del mes... Sólo pueden ser valores entre 1 y 12.")

prob = (transcurridos / 365)  * 100
nacimiento = anno - edad

print(nombre , " naciste en ", nacimiento , " con una probabilidad de " , prob)
print(" o en " , nacimiento - 1 , " con una probabilidad del " , 100 - prob)
