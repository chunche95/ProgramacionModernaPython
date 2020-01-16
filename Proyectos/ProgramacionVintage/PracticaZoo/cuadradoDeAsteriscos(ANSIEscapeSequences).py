import ANSIEscapeSequences

def dibujaCuadrado(lado,columna,ancho):
    p1=lado
    p2=columna
    
    while p1 <= (lado + ancho):
        ANSIEscapeSequences.locate(p1,columna)
        print('*')
        p1+=1
        ANSIEscapeSequences.locate(p1,(columna+ancho))
        print('*')
        p1+=2
    while p2 <= (columna + ancho):
        ANSIEscapeSequences.locate(lado,p2)
        print('*')
        p2+=1
        ANSIEscapeSequences.locate((lado+ancho),p2)
        print('*')
        p2+1

dibujaCuadrado(4,4,5)

