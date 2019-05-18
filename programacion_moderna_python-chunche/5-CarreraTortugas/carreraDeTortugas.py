# @Title: Carreras de tortugas - POO
# @Description: Objetos tortugas que 'competiran' en la carrera.
# 
# @Author: Chunche

'''
    (Módulo Turtle) --> Nos ayuda a crear las imágenes para la representacion por pantalla
    de la carrera.
    
    + turtle()
    |---- pantalla --> turtle.Screen
    |---- corredor [x] --> turtle.TurtleX
    

    Screen__________________________________________________ 
   |                                                       |
   |-Pista-----------------------------------------------| |
   |||                                                  0| |
   |||->T1                ^                             0| |
   |||                    |                             0| |
   |||->T2                * ->                          0| |
   |||              (movimientos)                       0| |
   |||->T3                                              0| |
   |||                                                  0| |
   |||->T4                                              0| |
   |||                                                  0| |
   |-----------------------------------------------------| | 
   |_______________________________________________________|
   
'''
import turtle
class Circuito():
    # Atributos
    corredores = []
    # Tupla de la posicion inicial en Y
    __posStartY = (-30,-10, 10, 30, 60)
    # Color de las tortugas
    __colorTurtle =("red", "yellow","green", "blue","orange")
    # Constructor
    def __init__(self,width, heigth):
        # Creacion de una pantalla (Screen para la pista de carrera)
        self.__screen = turtle.Screen()
        self.__screen.setup(width, heigth)
        self.__screen.bgcolor('lightgray')
        # Punto de partida y fin máximo del 'circuito'
        self.__startline = (-width/2) + 20
        self.__finishline = (width/2) - 20
        
        # Una vez terminada la creacion del circuito donde corren las tortugas, procedo a
        # Creacion de las corredoras
        self.__createRunners()
        
    def __createRunners(self):       
        for i in range(5):
            new_turtle  = turtle.Turtle()
            new_turtle.shape('turtle')
            new_turtle.penup()
            new_turtle.setpos(self.__startline, self.__posStartY[i])
            new_turtle.color(self.__colorTurtle[i])
            
            self.corredores.append(new_turtle)
            
        
# Ejecucion como módulo principal, así si lo importo en otro programa, no me crea la pantalla Screen    
if __name__ == '__main__':
    circuito = Circuito(440, 280)
   
'''
print("La color rosa es la prueba de dibujo, para eliminarla sólo borrar t.Turtle()")
t = turtle.Turtle()
t.color('pink')
t.shape('turtle')
t.fd(0)
'''
# Pruebas - El orden por el que se muestra por pantalla es descendente.
#print(circuito.corredores[4].fd(333))
circuito.corredores[4].fd(333)
#print(circuito.corredores[3].fd(203))
circuito.corredores[3].fd(203)
#print(circuito.corredores[2].fd(85))
circuito.corredores[2].fd(85)
#print(circuito.corredores[1].fd(60))
circuito.corredores[1].fd(60)
#print(circuito.corredores[0].fd(30))
circuito.corredores[0].fd(30)



