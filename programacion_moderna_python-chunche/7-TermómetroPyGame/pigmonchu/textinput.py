import pygame, sys
from pygame.locals import *

def name():
    pygame.font.init()
    screen = pygame.display.set_mode((480, 360))
    pygame.display.set_caption("Number Input")
    name = ""
    font = pygame.font.SysFont("Arial", 24)
    commascount = 0
    while True:
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                print(evt.unicode)
                if len(name)<10 and evt.unicode.isdigit() or (evt.unicode == ',' and commascount == 0):
                    if evt.unicode == ',':
                        commascount += 1
                    name += evt.unicode
                elif evt.key == K_BACKSPACE:
                    if name[-1] == ',':
                        commascount = 0
                    name = name[:-1]
                elif evt.key == K_RETURN:
                    print(name)
                    name = ""
            elif evt.type == QUIT:
                return
        screen.fill((244, 236, 203))
        
        textBlock = font.render(name, True, (60, 60, 60))
        rect = textBlock.get_rect()
        rect.top = 100
        rect.left = 50
        rect.width = 133
        rect.height = 24
        
#        rect = block.get_rect()
#        rect.center = screen.get_rect().center
        pygame.draw.rect(screen, (255, 255, 255), rect)
        screen.blit(textBlock, rect)
        pygame.display.flip()

if __name__ == "__main__":
    name()
    pygame.quit()
    sys.exit()