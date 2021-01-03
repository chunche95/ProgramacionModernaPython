import sys
if len(sys.argv)==3:
    texto = sys.argv[1]
    repeticiones = int(sys.argv[2])
    for i in range(repeticiones):
        print(texto)
else:
    print("ERROR: Entrada de datos erronea")
    print(''' Para aplicar la ejecucion correcta del programa debe introducir 2 argumentos.
    Ejemplo:
    archivo.py      "arg1"                  arg2
    (script)  (Elemento que repite) (Nº veces que se repite)

    Vuelva a intentarlo.
    ''')