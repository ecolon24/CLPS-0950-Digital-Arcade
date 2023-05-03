import math
import random
import pygame
from os import stat_result
import os.path
import sys

pygame.init()

(width, height) = (1200, 1000)
fps = 60

#colors for changing later
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
white = (255,255,255)
black = (0,0,0)
yellow = (255,255,0)
aqua = (0,255,255)
fushia = (255,0,255)

#setup display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Space Invaders')
screen.fill(blue)
pygame.display.flip()

