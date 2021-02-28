def operaciones():
        lista= [];
        resultado = 0;
        try:
            operacion = int(input("¿Que operacion desea realizar [número]? "));
        except ValueError:
            print("El valor introducido no es válido, vuelva a intentarlo de nuevo");
            operaciones();
        while True:            
            try:
                lista.append(input ("Escriba valor. "))
                valor=lista;
                print(valor);
                if("F" in lista):
                    lista.remove("F");
                    break;
            except ValueError:
                print("ERROR, no se puede operar la cadena introducida")
            except Exception as valor:
                print(type(valor).__name__)
        print(lista)
        art = len(lista)                           
        if (operacion == 1):
            # Recorro la longitud de la lista de argumentos de entrada y opero
            for i in lista:
                resultado += int(i);
        elif (operacion == 2):        
            for i in lista:
                resultado -= int(i);
        elif (operacion == 3):        
            for i in lista:
                resultado *= int(i);
        elif (operacion == 4):        
            try:
                for i in lista:
                    resultado /= int(i);
            except ZeroDivisionError: 
                print("No se puede dividir los valores entre 0.")
                return "Operacion no válida"
            except Exception as i:
                print(type(i).__name__)

        elif (operacion == 5):        
            for i in lista:
                resultado += int(i);
            resultado = (resultado*art)/100;
        else:
            print("Algo salió mal...");
        print(resultado);    
        exit();

def anuncio():
       
        print ('''Operaciones válidas.
            1- Sumar copmpra
            2- Resta cartera
            3- Multiplicacion articulos
            4- Division pedidos (yoq sé)
            5- Ahorro BlackDays        
            _________________________________________________ 
            "Escriba los valores, cuando termine escriba F 
            _________________________________________________
            ''')
        operaciones()
        
def main():    
    anuncio()
main()