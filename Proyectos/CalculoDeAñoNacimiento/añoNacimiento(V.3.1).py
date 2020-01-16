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

mes1 = 31 # Mes con 31 dias
mes2 = 28 # Mes con 28 dias
mes3 = 30 # Mes con 30 dias

transcurridos = 0
if mes > 1:
    transcurridos += mes1
if mes > 2:
    transcurridos += mes2 
if mes > 3:
    transcurridos += mes1
if mes > 4:
    transcurridos += mes3
if mes > 5:
    transcurridos += mes1
if mes > 6:
    transcurridos += mes3
if mes > 7:
    transcurridos += mes3
if mes > 8:
    transcurridos += mes1
if mes > 9:
    transcurridos += mes3
if mes > 10:
    transcurridos += mes1
if mes > 11:
    transcurridos += mes3
if mes > 12:
    transcurridos
# GuardaDiasPasados = Ene  + Feb   + Mar   + Abr   + May   + Jun   + Jul   + Ago   + Sep   + Oct   + Nov   + Dic 
# va haciendo una sumatoria de los meses hasta que se cumpla una condicion de comparacion adecuada. Su valor se va
# almacenando en la variable transcurridos, hasta que se cumpla la condición del if.
else:
    print("Error! Hay un error en la entrada del mes... Sólo pueden ser valores entre 1 y 12.")

transcurridos += dia # Almaceno el total de los dias transcurridos al final del condicional.

prob = (transcurridos / 365) * 100
nacimiento = anno - edad

print(nombre , " naciste en ", nacimiento , " con una probabilidad de " , prob)
print(" o en " , nacimiento - 1 , " con una probabilidad del " , 100 - prob)
