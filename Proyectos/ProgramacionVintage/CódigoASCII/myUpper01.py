# 
# +--Entrada ==> "hola" ==> Salida "HOLA"
# |
# | <upper(entrada)>
# |
# +--Interpretación ==> ('h')('o')('l')('a') ==> ('H')('O')('L')('A')
# |
# | <for(caracter)>
# |
# +-- Traducción ASCII ==> [104][111][108][97] ==> [72][79][76][75]
# |
# | <resultado>
# |
# +--Imprimir por pantalla ==> <resultado>
# 

def myUpper(cadena):
    resultado = ""
    for caracter in cadena:
        codigoCaracter = ord(caracter)
        if codigoCaracter >= 97 and codigoCaracter <= 122:
            codigoCaracter -= 32
            codigoMays = chr(codigoCaracter)
            resultado += codigoMays
        else:
            resultado += caracter
    return resultado

entrada = input ("Introduce un codigo en minusculas: ")
print (" Yo te lo devuelvo en mayúsculas: ",myUpper(entrada))



