import numpy as np
import sys
import matplotlib.pyplot as plt
from matplotlib import animation

lifes=[]

def play_life(a):
    xmax, ymax = a.shape
    b = a.copy()
    for x in range(xmax):
        for y in range(ymax):
            n = np.sum(a[max(x - 1, 0):min(x + 2, xmax), max(y - 1, 0):min(y + 2, ymax)]) - a[x, y] # Definimos vecindad
            if a[x, y]:
                if n < 2 or n > 3:
                    b[x, y] = 0 # regla 1 and 3
            elif n == 3:
                b[x, y] = 1 # regla 4
            # Sigue viva cuando hay 2 o tres células en su vecindad
    return(b)

def play(size, times):
    life = np.zeros((size, size), dtype=np.byte)

    lifem = []
    for x in range(size):
        for y in range(size):
            life[x,y]=np.random.binomial(1, 0.2)


    for i in range(times):
        life = play_life(life)
        lifem.append(life.copy())
    return lifem

def animate(i): 
    m = lifes[i]
    out = plt.imshow(m, interpolation='nearest', cmap=plt.cm.gray)
    return out  
