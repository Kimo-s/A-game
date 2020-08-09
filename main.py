import numbers as np
import pygame
import math
import sys
from vectorClass import Vector, findOrginial
from player import Player

size = width, height = 800,800
black = 0, 0, 0
yellow = 228, 235, 27

pygame.init()
screen = pygame.display.set_mode(size)



player = Player([width/2,height/2], screen,yellow)

while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(black)

    key = pygame.key.get_pressed()
    player.move(key)
    player.show()

    pygame.display.flip()
    pygame.display.update()

