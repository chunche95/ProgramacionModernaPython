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

import pygame, sys, random
from pygame.locals import *

class Runner():
    __customes = ("1","2","3","4","5",)
    def __init__(self, x=0, y=0):
        ixCustome = random.randint(0,4)
        self.custome = pygame.image.load("img/{}.png".format(self.__customes[ixCustome]))
        self.position = [x,y]
        self.name = ""
        
class Game():
    def __init__(self):
        # Creacion de atributos
        self.__screen = pygame.display.set_mode((640,480))
        self.__background = pygame.image.load("img/bg1.png")
        pygame.display.set_caption("C@rrer@$ de Bich0$")
        
        # Creacion de corredor
        self.runner = Runner(320,240)
        
    def start(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_UP:
                        # Mover hacia arriba runner
                        # runner = self.runner.position[1]
                        # runnerY += 1
                        self.runner.position[1] -= 5
                        # self.runner.position[1] += 1
                    elif event.key == K_DOWN:
                        # Mover hacia abajo runner
                        self.runner.position[1] += 5
                    elif event.key == K_LEFT:
                        # Mover hacia la izquierda
                        self.runner.position[0] -= 5
                    elif event.key == K_RIGHT:
                        # Mover hacia la derecha
                        self.runner.position[0] += 5
                    else:
                        pass
            self.__screen.blit(self.__background, (0,0))
            self.__screen.blit(self.runner.custome, self.runner.position)
            
            pygame.display.flip()
                
print("My name is {}".format(__name__))

if __name__ == '__main__':
    game = Game()
    pygame.init()
    game.start()