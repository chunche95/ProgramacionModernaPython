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

class Runner():
    def __init__(self, x=0, y=0):
        self.custome = pygame.image.load("img/2.png")
        self.position = (x,y)
        self.name = "Tortugui"
    def avanzar(self):
        self.position[0] += random.randint(1,6) 
        
class Game():
    runners = []
    __startLine = -10
    __finishLine = 620
    
    def __init__(self):
        # Creacion de atributos
        self.__screen = pygame.display.set_mode((640,480))
        self.__background = pygame.image.load("img/bg1.png")
        pygame.display.set_caption("Carrera de tortuguas")
        
        
        firstRunner = Runner(self.__startLine,240)
        firstRunner.name = "Speedy Fast"
        
        #self.runners = pygame.image.load("img/6.png")
        self.runners.append(firstRunner)
        
        #runners.append(firstRunner)
        #runners.append(Runner(self.__startLine, 240))
    
        
    def competir(self):
        # x = 0
        gameOver = False
        while not gameOver:
            # Comprobación de los eventos.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
                    
            # Refresacar / renderizar la pantalla.
            self.__screen.blit(self.__background, (0,0))
            self.__screen.blit(self.runners[0].custome, self.runners[0].position)
            pygame.display.flip()
            
             # x += 3
             #if x >= 250:
             #   ganador = True
        
        pygame.quit()
        sys.exit()
        
if __name__ == '__main__':
    # Inicializamos el paquete
    game = Game()
    pygame.font.init() # Alternativa para versiones antiguas es: 'pygame.font.init()'
    game.competir()
    
    