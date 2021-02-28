def indefinido(**kwargs):
    for kwarg in kwargs:
        print(kwarg, "-->", kwargs)
indefinido(a = "Hola", b = "¿Cómo va?", c = "para las certificaciones")


def saludar(mensaje, nombre):
    saludo = mensaje + nombre;
    return saludo
print (saludar("Bienvenido de nuevo, ",  "Marcos"))

def infinito (*args):
    for arg in args:
        print(arg)
infinito("Hola", "python", [1,2,3,2,4,3,4], {1,2,3,4,56,9})    