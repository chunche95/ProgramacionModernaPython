import pygame
import sys
import random

class Runner():
    imgfile = {
        'turtle' : '002-turtle',
        'prawn'  : '004-prawn',
        'octopus': '003-octopus',
        'fish'   : '001-fish',
        'moray'  : '005-moray'
        }
    
    def __init__(self, character='turtle', x=0, y=0):
        if character not in self.imgfile:
            character = 'turtle'
        self.character = character
        self.costume = pygame.image.load("images/{}.png".format(self.imgfile[character]))
        self.__position = (x,y)
        self.__name = "noName"
        
    def __str__(self):
        return "{} ({})".format(self.__name, self.character)
    
    def name(self, value=None):
        if value == None:
            return self.__name
        else:
            self.__name = value
    
    def advance(self):
        movement = random.randint(1,6)
        self.__position = (self.__position[0]+movement, self.__position[1])
        
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
                pass
    

class Game():
    
    runners = []
    customes = ('prawn', 'turtle', 'fish', 'octopus', 'moray')
    names = ('Johny', 'Diane', 'Ferdinan', 'Luzbella', 'Sinf')
    posY = (150, 195, 240, 290)
    __startLine = 20
    __finishLine = 620
    
    def __init__(self):
        
        self.__screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Carrera de bichos")
        self.background = pygame.image.load("images/background.png")
        
        for i in range(4):
            theRunner = Runner(self.customes[random.randint(0,4)], self.__startLine, self.posY[i])
            theRunner.name(self.names[i])
            self.runners.append(theRunner)

    def __on_render(self):
        self.__screen.blit(self.background, (0,0))
        for runner in self.runners:
            self.__screen.blit(runner.costume, runner.pos())
        pygame.display.flip()

    def __on_turn(self):
        gameOver = False
        for runner in self.runners:
            runner.advance()
            if runner.posx() >= self.__finishLine:
                print("The winner is {}".format(runner))
                gameOver = True
        return gameOver
    
    def __on_close(self):
        pygame.quit()
        sys.exit()


    def competir(self):
        
        gameOver = False
        
        while not gameOver:
            # comprobacion de los eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__on_close()                    
            # Dinámica de personajes
            gameOver = self.__on_turn()
                    
            # Refrescar / renderizar la pantalla
            self.__on_render()
                    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__on_close()                    


if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.competir()
    