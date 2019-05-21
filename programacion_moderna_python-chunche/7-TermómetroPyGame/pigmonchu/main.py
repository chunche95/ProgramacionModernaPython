import pygame, sys
from pygame.locals import *


class Selector():
    __tipoUnidad = None
    
    def __init__(self, unidad="C"):
        self.__customes = []
        
        self.__customes.append(pygame.image.load("images/posiF.png"))
        self.__customes.append(pygame.image.load("images/posiC.png"))
        self.unidad(unidad)

    def on_click(self):
        if self.__tipoUnidad == "C":
            return self.__change("F")
        else:
            return self.__change("C")

    def unidad(self, value=None):
        if value == None:
            return self.__tipoUnidad
        else:
            if value == 'C' or value == 'F':
                return self.__change(value)
            return False
    
    def __change(self, value):
        self.__tipoUnidad = value
        self.custome = self.__customes[0] if value == 'F' else self.__customes[1]
        return self.__tipoUnidad
        

class NumberInput():
    __commasCount = 0
    __value = 0
    __strValue = "0"
    __maxLength = 10
    __position = (0,0)
    __size = (0, 0)
    
    def __init__(self, value=0):
        self.__font = pygame.font.SysFont("Arial", 24)
        self.backgroundColor = (255, 255, 255)
        self.fontColor = (74, 74, 74)
    
    def __str__(self):
        return "({}, {}) - {}".format(self.__position[0], self.__position[1], self.__value)
    
    def on_change(self, event):
        if len(self.__strValue) < self.__maxLength and event.unicode.isdigit() or (event.unicode == ',' and self.__commasCount == 0):
            if event.unicode == ',':
                self.__commasCount += 1
            self.__strValue += event.unicode
        elif event.key == K_BACKSPACE:
            if self.__strValue[-1] == ',':
                self.__commasCount = 0
            self.__strValue = self.__strValue[:-1]
        elif event.key == K_DELETE:
            self.__strValue = ""
            self.__commasCount = 0
        else:
            pass
        self.value(self.__strValue)
        print(self)
            
    def render(self):
        textBlock = self.__font.render(self.__strValue, True, self.fontColor)
        rect = textBlock.get_rect()
        rect.left = self.__position[0]
        rect.top = self.__position[1]
        rect.size = self.__size
        return {
                'textBlock': textBlock,
                'rect': rect
            }
    
    def value(self, val=None):
        if val == None:
            return self.__value
        else:
            val = str(val)
            val = val.replace(",", ".")
            try:
                self.__value = float(val)
                self.__strValue = val
            except:
                pass

    def width(self, value=None):
        if value == None:
            return self.__size[0]
        else:
            try:
                value = int(value)
                self.__size = (value, self.__size[1])
            except:
                pass
    
    def height(self, value=None):
        if value == None:
            return self.__size[1]
        else:
            try:
                value = int(value)
                print(self.__size)
                self.__size = (self.__size[0], value)
            except:
                pass
    
    def size(self, value=None):
        if value == None:
            return self.__size
        else:
            try:
                self.__size = (int(value[0]), int(value[1]))
            except:
                print("Error al asignar tamaño")

    def posx(self, value=None):
        if value == None:
            return self.__position[0]
        else:
            try:
                value = int(value)
                self.__position = (value, self.__position[1])
            except:
                pass
    
    def posy(self, value=None):
        if value == None:
            return self.__position[1]
        else:
            try:
                value = int(value)
                print(self.__position)
                self.__position = (self.__position[0], value)
            except:
                pass
    
    def pos(self, value=None):
        if value == None:
            return self.__position
        else:
            try:
                self.__position = (int(value[0]), int(value[1]))
            except:
                print("Error al asignar posición")


            

class Termometro():
    def __init__(self):
        self.custome = pygame.image.load("images/termo1.png")
        
    def conversor(self, temperatura, toUnidad):
        resultado = 0
        if toUnidad != 'C'  and toUnidad != 'F':
            resultado = temperatura
        elif toUnidad == 'F':
            resultado = temperatura * 9/5 + 32
        else:
            resultado = (temperatura - 32) * 5/9

        return "{:6.2f}".format(resultado)

        

class mainApp():

    termometro = None
    entrada = None
    selector = None
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((290, 415))
        pygame.display.set_caption("Termómetro")
        
        self.termometro = Termometro()
        self.entrada = NumberInput()
        self.entrada.pos((106, 58))
        self.entrada.size((133, 28))
        self.selector = Selector('C')
    
    def __on_close(self):
        pygame.quit()
        sys.exit()
        
    def __on_render(self):
        self.__screen.fill((244, 236, 203))
        self.__screen.blit(self.termometro.custome, (50, 34))
        self.__screen.blit(self.selector.custome, (112, 153))
        text = self.entrada.render()
        pygame.draw.rect(self.__screen, self.entrada.backgroundColor, text['rect'])
        self.__screen.blit(text['textBlock'], text['rect'])
        
        pygame.display.flip()
    
    def __event_process(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__on_close()
                
            if event.type == KEYDOWN:
                self.entrada.on_change(event)
            
            if event.type == MOUSEBUTTONDOWN:
                unidad = self.selector.on_click()
                newValue = self.termometro.conversor(self.entrada.value(), unidad)
                print("{} a {} es {}".format(self.entrada.value(), unidad, newValue))

                self.entrada.value(newValue)
                
    
    def maincycle(self):
        while True:
            self.__event_process()
            self.__on_render()
            
if __name__ == '__main__':
    pygame.font.init()
    app = mainApp()
    app.maincycle()


        
        