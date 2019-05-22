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

class NumberInput():
    # Atributos
    __value = 0
    __strValue = "0"
    __position = [0,0]
    __size = [0,0]
    # Constructor
    def __init__(self,value = 0):
        self.__font = pygame.font.SysFont("Arial", 24)
        # Entrada del valor numerico
        self.value(value)
        # Esto hace lo mismo que el value value
#        try:
#            self.__value = int(value) # Comprueba que sea un integer
#            self.__strValue = str(value) # Conversion a string
#        except:
#            print("Error en los datos de entrada - Evaluación realizada en las lineas de la clase __init__ (line:29) ")
#            pass
    def render(self):
        # Renderizar cajon de texto de la temperatura --> font.render solo pinta cadenas de texto
        textBlock = self.__font.render(self.__strValue, True, (74,74,74))
        rect = textBlock.get_rect()
        rect.left = self.__position[0]
        rect.top = self.__position[1]
        rect.size = self.__size
        
        # Devolver valor por diccionario
#        return {
#            "fondo": rect,
#            "texto": textBlock
#            }

        # Devolver valor por tupla/lista
        return (rect, textBlock)
    
    # Constructores getter y setter
    def value(self, val= None):
        if val == None:
            return self.__value
        else:
            val = str(val)
            try:
                self.__value = int(val)
                self.__strValue = val
            except:
                print("Uy! hay un error! Miratelo -- Zona value")
                pass
            
    def width(self, val=None):
        if val == None:
            return self.__size[0]
        else:
            try:
                self.__size[0] = int(val)
            except:
                print("Uy! hay un error! Miratelo -- en zona def width")
                pass
    
    def height(self, val=None):
        if val == None:
            return self.__size[1]
        else:
            try:
                self.__size[1] = int(val)
            except:
                print("Uy! hay un error! Miratelo -- en zona def height")
                pass
            
    
    def size(self, val= None):
        if val == None:
            return self.__size
        else:
            try:
                # w = int(val[0])
                # h = int(val[1])
                self.__size = [int(val[0]), int(val[1])]
            except:
                print("Uy! hay un error! Miratelo -- en zona def size")
                pass
            
    def posX(self, val=None):
        if val == None:
            return self.__position[0]
        else:
            try:
                self.__position[0] = int(val)
            except:
                print("Uy! hay un error! Miratelo -- en zona def width")
                pass
        
    def posY(self, val=None):
        if val == None:
            return self.__position[1]
        else:
            try:
                self.__position[1] = int(val)
            except:
                print("Uy! hay un error! Miratelo -- en zona def width") 
                pass
            
    def pos(self, val=None):
        if val == None:
            return self.__position
        else:
            try:
                self.__position = [int(val[0]), int(val[1])]
            except:
                print("Uy! hay un error! Miratelo -- en zona def width")
                pass
                        
            
   
class mainApp():
    termometro = None
    entrada = None
    selector = None
    
    def __init__(self):
        # Pantalla principal - dimensiones
        self.__screen = pygame.display.set_mode((290,415))
        # Titulo
        pygame.display.set_caption("Termómetro")
        # Fondo de pantalla - Actualizacion del fondo de pantalla para que no queden restos, por si hay movimientos en las imagenes que trabajan sobre el
        # fondo.
        self.__screen.fill((240,236,200))
        
        self.termometro = Termometro()
        self.entrada = NumberInput()
        self.entrada.pos((106,58))
        self.entrada.size((133,28))
        
    def __on_close(self):
        pygame.quit()
        sys.exit()
        
    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.__on_close()
                
            # Dibujamos el termometro en su posicion    
            self.__screen.blit(self.termometro.custome, (50,34))
            
            # Dibujamos el cuadro de texto
            # Renderizacion de la tupla con el fondo del text block
            # Obtenemos el rectángulo blanco y foto de texto y  lo asignamos a la variable text
            text = self.entrada.render()
            
            # Pintamos el rectangulo blanco con sus datos, posicion y tamaño que estan en text[0]
            pygame.draw.rect(self.__screen, (255,255,255), text[0])
            
            #Pintamos la foto del texto(text[1])
            self.__screen.blit(text[1],self.entrada.pos())
            
            # Renderizacion de pantalla
            pygame.display.flip()
                    
                    
if __name__ == "__main__":
    pygame.init()
    app = mainApp()
    app.start()