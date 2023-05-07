import math
import random
import pygame
from os import stat_result
import os.path
import sys

def game():
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
    #BG = pygame.transform.scale(pygame.image.load(os.path.join("Downloads","Space Shooter Pics","assets", "background.jpeg")), (width, height))
    BG = pygame.image.load("/Users/EvelynKrall/Downloads/Space Shooter Pics/assets/background.jpeg")

    #setup display
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Space Invaders')
    #screen.blit(BG,(0,0))
    #pygame.display.flip()

    #making spaceship images C:\\Users\\DELL\\Downloads\\gfg.png
    #player_image = pygame.image.load(os.path.join("Downloads","Space Shooter Pics", "assets", "green.png"))
    player_rocket = pygame.image.load("player.png")
    x = 400
    y = 100
    xChange = 0
    
    monster_rocket = []

    #screen.blit(player_image, (player_X, player_Y))  
    running = True

    while running:
       screen.blit(BG, (0,0))



    #def player(player_X, player_Y):
    #    screen.blit(player_image, (player_X, player_Y))  

    

    #screen.blit(player_image, (width/2,height/2))

