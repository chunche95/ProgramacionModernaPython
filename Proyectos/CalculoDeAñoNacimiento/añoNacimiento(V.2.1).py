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

mes1 = 31 # Enero
mes2 = 28 # Febrero
mes3 = 31 # Marzo
mes4 = 30 # Abril
mes5 = 31 # Mayo
mes6 = 30 # Junio
mes7 = 31 # Julio
mes8 = 31 # Agosto
mes9 = 30 # Septiembre
mes10 = 31 # Octubre
mes11 = 30 # Noviembre
mes12 = 31 # Diciembre

transcurridos = 0 # Variable inicializada de los dias transcurridos, se usa como contador

if mes > 1:
    transcurridos += mes1
if mes > 2:
    transcurridos += mes2 
if mes > 3:
    transcurridos += mes3
if mes > 4:
    transcurridos += mes4
if mes > 5:
    transcurridos += mes5
if mes > 6:
    transcurridos += mes6
if mes > 7:
    transcurridos += mes7
if mes > 8:
    transcurridos += mes8
if mes > 9:
    transcurridos += mes9
if mes > 10:
    transcurridos += mes10
if mes > 11:
    transcurridos += mes11
if mes > 12:
    transcurridos
# GuardaDiasPasados= Ene  + Feb   + Mar   + Abr   + May   + Jun   + Jul   + Ago   + Sep   + Oct   + Nov   + Dic 
else:
    print("Error! Hay un error en la entrada del mes... Sólo pueden ser valores entre 1 y 12.")

transcurridos += dia # Almaceno el total de los dias transcurridos al final del condicional.

prob = (transcurridos / 365) * 100
nacimiento = anno - edad

print(nombre , " naciste en ", nacimiento , " con una probabilidad de " , prob)
print(" o en " , nacimiento - 1 , " con una probabilidad del " , 100 - prob)
