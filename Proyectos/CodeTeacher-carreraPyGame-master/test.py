import pygame

width = 640 
height = 480
screen = pygame.display.set_mode((width, height))
screen.fill((255,0,0))
pygame.display.set_caption("Juego de prueba")
 

pygame.init() #La inicialización de pygame comienza la comprobación de eventos

gameOver = False
clock = pygame.time.Clock() #  Reloj de pygame. Lo usaremos para fijar la velocidad del juego (independientemente de la velocidad del procesador)

signo = 1
while not gameOver:
  # Manejo de eventos
  for event in pygame.event.get(): #Vacía el buffer de eventos
    if event.type == pygame.QUIT:
      gameOver = True
      
  player = pygame.Rect(320+25*signo,240, 25, 25) # Rectángulo negro de 25x25
  screen.fill((255, 0, 0)) # Fondo de pantalla rojo
  pygame.draw.rect(screen, (0,0,0), player) # situar player en screen
  
  pygame.display.flip() # Refrescar pantalla
  signo *=-1
  clock.tick(24) # 1 Frame por segundo (ralentiza el parpadeo)
  
pygame.quit()
  

    
  
  
  