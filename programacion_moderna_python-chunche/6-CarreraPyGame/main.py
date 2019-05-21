# @Title: Creación de carreras de tortugas con PyGame
# @Description: En este programa se creará una competición de carreras de tortugas con la ayuda de la libreria
# pygame. Para ello, es necesario instalar el paquete, por defecto no lo está, para ello:
#  > Tools
#  >> Manage packages..
#  >>> En la barra de  'Find package in PiPy' escribimos 'pygame' y damos a que lo busque
#  >>>> Install
""" Esquema:
        - class CreaciónDeClases:
            - def __crearLasFuncionesNecesarias__:
            - def __comprobarEventos:
            - renderizar la pantalla:
"""
# @Author: Chunche
#

import pygame
import sys
import random

class Runner():
    __customes = ("1","2","3","4","5",)
    def __init__(self, x=0, y=0, custome='2'):
        self.custome = pygame.image.load("img/{}.png".format(custome))
        self.position = [x,y]
        self.name = custome
    def avanzar(self):
        self.position[0] += random.randint(1,4) 
        
class Game():
    runners = []
    __posY = (160,200,240,280)
    __names = ("Nemo","Ninja", "Speedy Fast", "Octopus")
    __startLine = -5
    __finishLine = 620
    
    def __init__(self):
        # Creacion de atributos
        self.__screen = pygame.display.set_mode((640,480))
        self.__background = pygame.image.load("img/bg1.png")
        pygame.display.set_caption("Carrera de tortuguas")
        
        for i in range(4):
            theRunner = Runner(self.__startLine,self.__posY[i])
            theRunner.name = self.__names[i]
            #self.runners = pygame.image.load("img/6.png")
            self.runners.append(theRunner)
        
        #runners.append(firstRunner)
        #runners.append(Runner(self.__startLine, 240))
    def close(self):
        pygame.quit()
        sys.exit()
        
    def competir(self):
        # x = 0
        gameOver = False
        while not gameOver:
            # Comprobación de los eventos.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
            
            # Avance del corredor - Creamos el metodo para ello llamamos a avanzar()
            for activeRunner in self.runners:
                activeRunner.avanzar()
                if activeRunner.position[0] >= self.__finishLine:
                    print ("{} win!".format(activeRunner.name))
                    gameOver = True
            
            
            # Refresacar / renderizar la pantalla.
            self.__screen.blit(self.__background, (0,0))
            
            # Creacion de los 'n' corredores
            for runner in self.runners:
                self.__screen.blit(runner.custome, runner.position)
                
            # Inicializacion de la pantalla
            pygame.display.flip()
            
             # x += 3
             #if x >= 250:
             #   ganador = True
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT():
                    self.close()
        
if __name__ == '__main__':
    # Inicializamos el paquete
    game = Game()
    pygame.font.init() # Alternativa para versiones antiguas es: 'pygame.font.init()'
    game.competir()
    
    