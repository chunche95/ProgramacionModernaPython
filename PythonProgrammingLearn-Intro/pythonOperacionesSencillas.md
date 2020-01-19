Operaciones sencillas.

Python tiene la capacidad de realizar cálculos. Ingresa una cuenta directamente en la consola de Python, y dará el resultado.
<code>
    >>> 2 + 2
    4
    >>> 5 + 4 - 3
    6
</code>
 Los espacions entre los signos más y menos aquí sin opcionales ( el código aún funcionaría sin ellos), pero facilitan la lectura.
 Las multiplicaciones y divisiones, utilizando un asterisco para indicar multiplicaciones y una barra para indicar divisiones.
 Usa paréntesis para determinar cuáles operaciones son realizadas primero.
 <code>
    >>> 2 * (3 + 4)
    14
    >>> 10 / 2
    5
</code>
El signo menos indica un número negativo. Las operaciones pueden ser realizadas con números negativos, de la misma forma que podrían ser realizadas con números positivos.
<code>
    >>> -7 
    -7 
    >>> (-7 + 2) * (-4)
    20
</code>
Los signos más (+) también se pueden poner delante de los números, pero esto no tiene efecto, y es mayormente utilizado para enfatizar que un número es positivo para incrementar la legitibilidad del código.

Dividir por cero en Python genera un error ya que no se puede calcular ninguna respuesta.
<code>
    >>>11 / 0
    Traceback (most recent call last): 
    File "<stdin>", line 1, in <module>
    ZeroDivisionError: division by zero
</code>
En Python, la última línea de un mensaje de error indica el tipo del error. 