import numpy as np
import pygame
import math
import time
import sys
from vectorClass import Vector, findOrginial
from player import Player
from polygon import Polygon

size = width, height = 800,800
black = 0, 0, 0
yellow = 228, 235, 27

pygame.init()
screen = pygame.display.set_mode(size)


cords = [[152, 190], [152, 230], [200, 230], [300,100]]
player = Player([width/2,height/2], screen, yellow)
pol = Polygon(screen, cords)

FPS = pygame.time.Clock()

while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(black)

    key = pygame.key.get_pressed()
    player.move(key)
    player.show()
    player.laser()

    # pol.rotate(0.3)
    pol.show()

    pygame.display.flip()
    FPS.tick()