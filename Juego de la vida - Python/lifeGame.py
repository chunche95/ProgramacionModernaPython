#!/bin/python 
import os
import pygame
import numpy as np 
import time
os.system('clear')
os.system('cls')
# @author: [ Paulino Bermúdez R.]
# @Description: Programando en Python el famosos Juego de la Vida de Conway, uno de los sistemas de autómatas celulares más famosos.

# Centramos la ventana
os.environ["SDL_VIDEO_CENTERED"] = "1"
# Inicializamos pygame.
pygame.init()

# Tamaño de pantalla & fondo de pantalla
width, height = 500, 500
# La creo
screen = pygame.display.set_mode((height, width))
# Color
bg = 25,25,25 
screen.fill(bg)

# Tamaño de la celda
nxC, nyC = 35,35
dimCW = width / nxC
dimCH = height / nyC 


# Estructura de datos que contiene todos los estados de las diferentes celdas:
# Estados de las celdas: 
#   - Vivas = 1
#   - Muertas = 0
# Inicio de la matriz con ceros.
gameState = np.zeros((nxC, nyC))

# Autómatas.
# => Palo.
#   0   1   0
#   0   1   0
#   0   1   0
# gameState[5,3] = 1
# gameState[5,4] = 1
# gameState[5,5] = 1
# => Móvil
#   0   1   0
#   0   0   1
#   1   1   1
# gameState[21,21] = 1
# gameState[22,22] = 1
# gameState[22,23] = 1
# gameState[21,23] = 1
# gameState[20,23] = 1

# Versión de mi autómata que siempre aparece centrada: Mi autómata.
posInitX = int((nxC/2)-3)
posInitY = int((nyC/2)-5)

gameState[posInitX    , posInitY] = 1
gameState[posInitX + 1, posInitY] = 1
gameState[posInitX + 2, posInitY] = 1
gameState[posInitX + 3, posInitY] = 1

gameState[posInitX + 3, posInitY + 1] = 1
gameState[posInitX + 3, posInitY + 2] = 1

gameState[posInitX    , posInitY + 3] = 1
gameState[posInitX + 3, posInitY + 3] = 1

gameState[posInitX    , posInitY + 4] = 1
gameState[posInitX + 1, posInitY + 4] = 1
gameState[posInitX + 2, posInitY + 4] = 1
gameState[posInitX + 3, posInitY + 4] = 1

# Control de ejecución - En True se inicia pausado (Para  poder ver la forma inicial de los autómatas)
pauseExec = True
# Control de fin de jjuego.
endGame = False
# Acumulador de cantidad de iteraciones.
iteration = 0 
# Bucle de ejecución de refrescos de pantalla (Main Loop)
while not endGame:
    newGameState = np.copy(gameState)
    # Colorea la pantalla
    screen.fill(bg)
    # Agrego pausa para minimizar el trabajo de CPU, evito el 100%
    time.sleep(0.1)
    # Registro de eventos de teclado y mouse.
    ev = pygame.event.get()
    # Contador de población.
    population = 0

    for event in ev:
        # Si se cierra la ventana finaliza el programa.
        if event.type == pygame.QUIT:
            endGame = True
            break
        if event.type == pygame.KEYDOWN:
            # ESC -> fin del programa.
            if event.key == pygame.K_ESCAPE:
                endGame = True
                break
            # Si pulsa N limpia la grill y tomo nuevas medidas.
            if event.key == pygame.K_n:
                iteration = 0
                gameState = np.zeros((nxC, nyC))
                newGameState = np.zeros((nxC,nyC))
                pauseExec = True
            else:
                # Si tocan cualquier tecla no contemplada, pauso o reanulo el juego.
                pauseExec = not pauseExec
        # Detección de click de mouse.
        mouseClick = pygame.mouse.get_pressed()
        # Obtener la posición del cursos en pantalla 
        if sum(mouseClick) > 0:
            # Click del medio pausa / reanuda el juego 
            if mouseClick[1]:
                pauseExec = not pauseExec
            else:
                # Obtengo las coordenadas del cursor
                posX, posY = pygame.mouse.get_pos()
                # Convierto las coordenadas en pixeles a celda clickeada a la grill
                celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
                # Click izquierdo y derecho permutan entre vida y muerte
                newGameState[celX, celY] = not gameState[celX, celY]
    if not pauseExec:
        # Incremento el contador de generaciones.
        iteration += 1
    # Recorro cada una de las celdas generadas.
    for y in range(0, nyC):
        for x in range(0, nxC):
            if not pauseExec:
                # Cálculo del número de vecinos cercanos
                n_neigh = (
                    gameState[(x - 1) % nxC, (y - 1) % nyC]
                    + gameState[x % nxC, (y - 1) % nyC]
                    + gameState[(x + 1) % nxC, (y - 1) % nyC]
                    + gameState[(x - 1) % nxC, y % nyC]
                    + gameState[(x + 1) % nxC, y % nyC]
                    + gameState[(x - 1) % nxC, (y + 1) % nyC]
                    + gameState[x % nxC, (y + 1) % nyC]
                    + gameState[(x + 1) % nxC, (y + 1) % nyC]
                )
                # Una célula muerta con exactamente 3 células vecinas vivas "nace" => Seguirá 'viva'
                if gameState[x,y] == 0 and n_neigh == 3:
                    newGameState[x,y] = 1
                # Una célula viva con 2 o 3 célulcas vecinas vivas sigue viva, en otro caso, muere, o bien por soledad o sobrepoblación.
                elif gameState[x,y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newGameState[x,y] = 0
            # Incremento del contador de población
            if gameState[x,y] == 1:
                population += 1
            # Creación del polígono de cada celda a pintar
            poly = [
                (int(x       * dimCW), int(y       * dimCH)),
                (int((x + 1) * dimCW), int(y       * dimCH)),
                (int((x + 1) * dimCW), int((y + 1) * dimCH)),
                (int(x       * dimCW), int((y + 1) * dimCH))
            ]
            if newGameState[x,y]==0:
                # Dibujo celda para cada par de 'x' y de 'y'
                # Puntos que definen al polígono que esta pintando.
                pygame.draw.polygon(screen(128,128,128), poly, 1)
            else:
                if pauseExec:
                    # Pintamos de gris las celdas.
                    pygame.draw.polygon(screen, (128,128,128), poly,1 )
                else:
                    # pinto de blanco las celdas
                    pygame.draw.polygon(screen, (255,255,255) , poly,0 )
    # Actualizacion de los datos
    title = "JUEGO DE LA VIDA - Población: {population} - Generación: {iteration} "
    if pauseExec:
        title += " - [PAUSADO]"
    pygame.display.set_caption(title)

    # Actualizo gameState
    gameState = np.copy(newGameState)

    # Muestro y actualizo los fotogramas en cada iteración del bucle principal
    pygame.display.flip()

print("Juego finalizado")