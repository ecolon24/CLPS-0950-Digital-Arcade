import math
import random
import pygame
from os import stat_result
import os.path
import sys

pygame.init()

(width, height) = (800, 600)
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
BG = pygame.transform.scale(pygame.image.load(os.path.join("Downloads","Space Shooter Pics","assets", "background.jpeg")), (width, height))

#setup display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Space Invaders')
screen.blit(BG,(0,0))
#pygame.display.flip()

#making spaceship images C:\\Users\\DELL\\Downloads\\gfg.png
player_image = pygame.image.load(os.path.join("Downloads","Space Shooter Pics", "assets", "green.png"))
player_X = 400
player_Y = 100
player_Xchange = 0

#screen.blit(player_image, (player_X, player_Y))  



#def player(player_X, player_Y):
#    screen.blit(player_image, (player_X, player_Y))  

    

#screen.blit(player_image, (width/2,height/2))

