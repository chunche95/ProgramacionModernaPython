# @Title: Practica Tierra
# @Description: Enviar un mensaje con numeracion Hexadecimal de la Tienrra a Marte.
# @Version 1.0
# @Autor: Pauchino09


digitos16=('0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f')
anguloCircunf = 360/16

# mensaje recibido
angulos =(90,180,135,337.5,135,270,135,22.5)

# Indice de la lista hexadecimal
indiceHexadecimal = 0
cadenaHex =  ? # Error de traduccion, no se como corregirlo aun.***

#Recepcion del mensaje
for angulo in angulos:
    indiceHexadecimal = round(angulo/anguloCircunf)
    cadenaHex.append(digitos16[indiceHexadecimal])
    
dig1 = 0
dig2 = 0
letraHex = '00'
posicion = 0
cadena = ? # Error de traduccion***

# Agrupamos los digitos hex en pares formando las letras. Las almacenamos en cadena.

while posicion < len(angulos):
    if posicion % 2 == 0:
        dig1 = cadenaHex[posicion]
    else:
        dig2 = cadenaHex[posicion]
        letraHex = dig1 + dig2
        cadena.append(letraHex)
    posicion += 1
palabra = ""
 
# convertimos de Hexadecimal a letras
for letra in cadena:
    palabra += chr(int(letra,16))

# Imprimo por pantalla el resultado
print("Dígitos transmitidos: ", cadenaHex)
print("Letras Hexadecimales: ", cadena)
print("Mensaje traducido: ", palabra)