# @Title: Practica Marte
# @Description: Enviar un mensaje con numeracion Hexadecimal de Marte a la Tierra.
# @Version 1.0
# @Autor: Pauchino09


digitos16=('0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f')
angulo = 360/16

# cadena enviada
cadena="Hola"

#Enviamos cada caracter convertido en hexadecimal bajo el angulo que le corresponde a la circunferencia
for caracter in cadena:
    #Traduzco el string 'Hola' en hexadecimal
    valorHexadecimal = hex(ord(caracter))
    
    # Guardo el valor hex de cada caracter, eliminando la parte (0X).
    dig1 = valorHexadecimal[2]
    angulo1 = digitos16.index(dig1) * angulo
    #
    dig2 = valorHexadecimal[3]
    angulo2 = digitos16.index(dig2) * angulo
    
    #Tomo el valor de los caracteres entero cortando la parte 0x y uniendo los digitos
    segundopar = valorHexadecimal[2:4]
    
    # Imprimo por pantalla cada resultado
    print("----------")
    print(valorHexadecimal)
    print(dig1," --> ",angulo1)
    print(dig2," --> ",angulo2)
    print(segundopar)


