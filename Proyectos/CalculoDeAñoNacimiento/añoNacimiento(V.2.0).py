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

if mes == 1:
    transcurridos = dia
if mes == 2:
    transcurridos = 31 + dia
if mes == 3:
    transcurridos = 31 + 28 + dia
if mes == 4:
    transcurridos = 31 + 28 + 31 + dia
if mes == 5:
    transcurridos = 31 + 28 + 31 + 30 + dia
if mes == 6:
    transcurridos = 31 + 28 + 31 + 30 + 31 + dia
if mes == 7:
    transcurridos = 31 + 28 + 31 + 30 + 31 + 30 + dia
if mes == 8:
    transcurridos = 31 + 28 + 31 + 30 + 31 + 30 + 30 + dia
if mes == 9:
    transcurridos = 31 + 28 + 31 + 30 + 31 + 30 + 30 + 31 + dia
if mes == 10:
    transcurridos = 31 + 28 + 31 + 30 + 31 + 30 + 30 + 31 + 30 + dia
if mes == 11:
    transcurridos = 31 + 28 + 31 + 30 + 31 + 30 + 30 + 31 + 30 + 31 + dia
if mes == 12:
    transcurridos = 31 + 28 + 31 + 30 + 31 + 30 + 30 + 31 + 30 + 31 + 30 + dia

prob = (transcurridos / 365) * 100
nacimiento = anno - edad

print(nombre , " naciste en ", nacimiento , " con una probabilidad de " , prob)
print(" o en " , nacimiento - 1 , " con una probabilidad del " , 100 - prob)
