"""
Resumen
    1 Entrada de bebe por 0€
    2 Entradas de Adulto por 46€
    1 Entradas de Jubilado 18€
    --------------------------
1,Bebe,0.00€,2,Adulto,46.00€,1,Jubilado,18.00€
"""

import screen
from display import label
from validation import valid
from ticket import processTickets, collectData, saveData

def main():
    
    label()
    
    
    edad = valid("Introduzca edad: ")
    cantidad = valid("Introduzca cantidad: ")
    
    data = []
    
    while edad > 0 and cantidad > 0:
        ticket = processTickets(edad,cantidad)
        
        collectData(data, tickets)
        
        screen.Print(tickets[1], row = tickets[3][0], col = tickets[3][1])
        screen.Print('{:7.2f}€'.format(tickets[2]), row = tickets[4][0], col = tickets[4][1])
                     
        screen.Print(tickets[5], row = tickets[7][0], col = tickets[7][1], style='bold')
        screen.Print('{:7.2f}€'.format(ticket[6]),row = tickets[8][0], col = tickets[8][1], style = 'bold')
        
        edad = valid("Introduzca una edad: ")
        if edad == 0:
            continue
        else:
            cantidad = valid("Introduzca cantidad: ")
    saveData(data)
    
    screen.locate(15,1)
    
    main()
    
    
def processTickets(edad, cantidad):
    selection = setTickets(edad)
    
    # segun Tipos admitidos
    tipoAcumulado[selection[0]] += cantidad
    precioTotal = TipoAcumulado[0] * selection[3]
    localCantidad = (selection[1], selection[2] + len(selection[0]))
    localPrecioTotal = (localCantidad[0],  localCantidad[1] + 7)
    
    # segun Total
    
    cuentaTotal['unidades_totales'] += cantidad
    cuentaTotal['factura_total'] += cantidad * selection[3]
    localTotalUnidades = (9, len('Total.......................:') + 5)
    localTotalFactura = (9, len('Total.......................:') + 5 + 7)
        
    # segun Almacenado
    
    canti = cantidad
    pasta  cantidad * selection[3]
    
    return [selection[0],
            cuentaTipo[selection[0]], precioTotal,
            localCantidad['total_unidades'], cuentaTotal['total_factura'],
            edad, canti, selection[3], pasta]


# Procesamiento de los datos almacenados:
# Informacion guardada
def collectData(data, tickets):
    record =  [ticktes[0], tickets[9], tickets[10], tickets[11], tickets[12]]
    data.append(record)
# Almacenamiento de los datos --> commit
def saveData(data):
    dataset = open('transaccion.txt', 'a+')
    for i in range(len(data)):
        transaccion = '{},{},{},{},{}\n'.format(data[i][0], data[i][1],data[i][2],
                                                data[i][3],data[i][4])
        dataset.write(transaccion)
    
    dataset.close()