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

class runner():
    pass 

class Game():
    corredores = []
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640,480))
        pygame.display.set_caption("Carrera de tortuguas")
        # Creacion de atributo
        self.background = pygame.image.load("img/bg1.png")
        self.runner = pygame.image.load("img/6.png")
        
    
        
    def competir(self):
        x = 0
        ganador = False
        while True:
            # Comprobación de los eventos.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            # Refresacar / renderizar la pantalla.
            self.__screen.blit(self.background, (0,0))
            self.__screen.blit(self.runner, (x,240))
            pygame.display.flip()
            
            x += 3
            if x >= 250:
                ganador = True
        
        pygame.quit()
        sys.exit()
        
if __name__ == '__main__':
    # Inicializamos el paquete
    pygame.init()
    game = Game()
    game.competir()
    
    
    
    
    
    
    
    