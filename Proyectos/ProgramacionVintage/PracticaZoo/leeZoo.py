from config import preciosE

fEntradas = open("transacciones.txt",'r')

numEntradasBebe = 0
numEntradasNiño = 0
numEntradasAdulto = 0
numEntradasJubilado = 0

linea = fEntradas.readline()

while linea != '':
    entradas = linea.split(',')
    numEntradasBebe += int(entradas[0])
    numEntradasNiño += int(entradas[1])
    numEntradasAdulto += int(entradas[2])
    numEntradasJubilado += int(entradas[3])
    
    totalEntradas = totalEntradas  + int(entradas[0])
    totalEntradas = totalEntradas  + int(entradas[1])
    totalEntradas = totalEntradas  + int(entradas[2])
    totalEntradas = totalEntradas  + int(entradas[3])
    
    linea = fEntradas.readline()
    
print("Entradas de Bebe:...... {:3d} - {:7.2f}€".format(numEntradasBebe, numEntradas *  precioE['bebe']))
print("Entradas de Niño:...... {:3d} - {:7.2f}€".format(numEntradasNiño, numEntradas *  precioE['niño']))
print("Entradas de Adulto:.... {:3d} - {:7.2f}€".format(numEntradasAdulto, numEntradas *  precioE['adulto']))
print("Entradas de Jubilado:.. {:3d} - {:7.2f}€".format(numEntradasJubilado, numEntradas *  precioE['jubilado']))

print("\nTotal: {:3d} - {:7.2f}€".format(numEntradasBebe+numEntradasNiño+numEntradasAdulto+numEntradasJubilado,
                                         numEntradasBebe * precioE['bebe']+numentradasNiño * precioE['niño']+\
                                         numEntradasAdulto * precioE['adulto']+numEntradasJubilado * precioE['jubilado']))


