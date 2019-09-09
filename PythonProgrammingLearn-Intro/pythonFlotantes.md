Flotantes.

Los flotantes son utilizados en Python para representar números que no son enteros. Algunos ejemplos de números que son representados como flotantes son 0.5 y -7.823.
Pueden ser creados directamente introduciendo un número con un punto decimal, o utilizando operaciones tales como división de números enteros. 
Los ceros adicionales al final del número son ignorados.
<code>
    >>> 3/4
    0.75
    >>> 9.8743
    9.8743
</code>
Los ordenadores no pueden almacenar flotantes con perfecta precisión, de la misma manera en que no podemos escribir la expansión decimal de 1/3 (0.33333333...) Ten en cuenta esto porque muchas veces conlleva a errores exasperantes.

Como viste anteriormente, dividir cualquier par de enteros produce un flotante. 
Un flotante también es producto al ejecutar una operación sobre dos flotante, o sobre un flotante y un entero.
<code>
    >>>  8 / 2
    4.0
    >>> 6 * 7.0
    42.0
    >>> 4 + 1.65
    5.65
</code>
Un flotante puede ser sumado a un entero porque Python silenciosamente convierte un entero en un flotante. Sin embargo, esta conversión implícita es excepción y no la regla en Python - normalmente tienes que convertir los valores manualmente si quieres operarlos. 