dic = {
    "Marco":"Becario",
    "Susana":"Directora",
    "Richard":"Limpieza",
    "Pablo":"Secretario",
    "Pepi":"Conductora",
    "Martin":["Jefe Seccion", "Oficina"],
    "Paula":{
        "Mañanas":"Almacen", 
        "Tardes":"Ventas"
        }
}

print("_"*100+"\n")
print(dic)


''' Añadir 1 '''
dic["Sandro"] = "El nuevo"
print("_"*100+"\n")
print(dic)

''' Modificamos '''
dic["Sandro"] = "RRHH"
print("_"*100+"\n")
print(dic)

''' Eliminamos '''
del(dic["Marco"])
print("_"*100+"\n")
print(dic)

