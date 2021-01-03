conjuntos = set()
conjuntos = {
    "naranjas",
    1,
    2.03,
    3.0,
    1.1,
    "Python",
    True
}
print(conjuntos)
''' Añadir elemento '''
conjuntos.add("Añado_1")
print(conjuntos)
''' Borrar elemento '''
conjuntos.discard(1)
print(conjuntos)
''' Buscar elemnto '''
print ( 'Python' not in conjuntos )
print ( 'python' in conjuntos )