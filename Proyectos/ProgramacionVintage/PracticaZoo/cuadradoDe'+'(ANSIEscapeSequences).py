import ANSIEscapeSequences

def dibujaCuadrado(p1,p2,lado):
    lado = 8
    ANSIEscapeSequences.locate(p1,p2)
    print('+'*lado)
    for i in range(1,int(lado/2)):
        ANSIEscapeSequences.locate(p1+i,p2)
        print('+')
        ANSIEscapeSequences.locate(p1+i,p2+lado-1)
        print('+')
    ANSIEscapeSequences.locate(p1+int(lado/2),p2)
    print('+'*lado)
    
dibujaCuadrado(6,6,12)