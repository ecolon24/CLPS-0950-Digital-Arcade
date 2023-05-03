import pygame
import random 

#Global Variables 
screen_width= 800
screen_height= 700 
play_width=300
play_height= 600
block_size= 30

#play area
upper_left_x= (screen_width-play_width)//2
upper_left_y= screen_height - play_height

#Making the shapes of the blocks; accounting for different rotations+positioning
S_shape= [['.....'
           '.....'
           '..00.'
           '.00..'
           '.....'],
           ['.....'
            '..0..'
            '..00.'
            '...0.'
            '.....'
            ]]
print(S_shape)
