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
#0 will represent where the block actually is placed, 5X5 setup!
#have a notability file on Ipad that draws out all the different orientations; took some time!
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

Z_shape= [['.....'
           '.....'
           '.00..'
           '..00.'
           '.....'],
           ['.....'
            '..0..'
            '.00..'
            '.0...'
            '.....']]
I_shape= [['..0..'
           '..0..'
           '..0..'
           '..0..'
           '.....'],
           ['.....'
            '0000.'
            '.....'
            '.....'
            '.....']]
O_shape=[['.....'
          '.....'
          '.00..'
          '.00..'
          '.....']]
#O_shape only has one configuration because a square when rotated still has the same shape!
J_shape= [['.....'
           '.0...'
           '.000.'
           '.....'
           '.....'],
           ['.....'
            '.....'
            '.000.'
            '...0.'
            '.....'],
            ['.....'
             '..0..'
             '..0..'
             '.00..'
             '.....'],
             ['.....'
              '..00.'
              '..0..'
              '..0..'
              '.....']]

L_shape= [['.....'
           '...0.'
           '.000.'
           '.....'
           '.....'],
           ['.....'
            '..0..'
            '..0..'
            '..00.'],
            ['.....'
             '.....'
             '.000.'
             '.0...'
             '.....'],
             ['.....'
              '.00..'
              '..0..'
              '..0..'
              '.....']]
T_shape= [['.....'
           '..0..'
           '.000.'
           '.....'
           '.....'],
           ['.....'
            '..0..'
            '..00.'
            '..0..'
            '.....'],
            ['.....'
             '..0..'
             '.00..'
             '..0..'
             '.....'],
             ['.....'
              '.....'
              '.000.'
              '..0..'
              '.....']]

#Shape Colors! Had to do a bit of research to find these but :) 
#fun fact: Avid tetris fans refer to 'Tetris shapes' as tetriminos!
tetriminos= [S_shape, Z_shape, I_shape, O_shape, J_shape, L_shape, T_shape]
tetrimino_colors= [(0,255,0), (255,0,0), (0,255,255),(255,255,0),(225,165,0),(0,0,255),(128,0,128)]
print(tetriminos)
