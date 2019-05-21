#
# @Title: Termómetro con PyGame
#
# @Description: Utilizando la interfaz gráfica del módulo de pygame para crear un termómtero igual a los ejemplos realizados en clase.
# Repasaremos como utilizar objetos y en este caso el funcionamiento deberá responder a dos eventos. La entrada de la temperatura en el campo
# de entrada deberemos ser capaz de alamcenar ese valor en una variable para luego transformarla si se hcae necesario.
# El selector de grados nos permitirá cambiar la entrada y si existe un valor debe transformarlo.
# Así que nuestro programa deberá responder a dos eventos:
#  - Entrada del teclado
#  - Clic del ratón sobre el selector de unidades 
#
# @Version: 1.0
# @Author: Chunche

import pygame, sys
from pygame.locals import *

class Termometro():
    def __init__(self):
        self.custome = pygame.image.load("pigmonchu/images/termo1.png")

class mainApp():
    termometro = None
    entrada = None
    selectro = None
    
    def __init__(self):
        # Pantalla principal - dimensiones
        self.__screen = pygame.display.set_mode((290,415))
        # Titulo
        pygame.display.set_caption("Termómetro")
        # Fondo de pantalla - Actualizacion del fondo de pantalla para que no queden restos, por si hay movimientos en las imagenes que trabajan sobre el
        # fondo.
        self.__screen.fill((240,236,200))
        
        self.termometro = Termometro()
        
    def __on_close(self):
        pygame.quit()
        sys.exit()
        
    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.__on_close()
                    
            self.__screen.blit(self.termometro.custome, (50,34))
            # Renderizacion de pantalla
            pygame.display.flip()
                    
                    
if __name__ == "__main__":
    pygame.init()
    app = mainApp()
    app.start()