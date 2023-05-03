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

#function that holds the placement of the pieces!
#new keyword; self! Did a bit of research for it :) 
class Piece(object):
    def __init__(self,x,y,tetriminos):
        self.x= x
        self.y= y
        self.tetriminos= tetriminos
        self.color= tetrimino_colors[tetriminos.index(tetriminos)]
        self.rotation= 0
        pass

    #creating a list for every row on the grid. 10 blocks width, 20 blocks height!
    #intialize with all black, will fill in with specified colors as the person plays the game.
    #locked_position is for when the user "drops + locks in" their blocks, become static instead of dynamic pieces. keep in mind there is a color change because each tetrimino is a dif color!
def create_grid(locked_positions={}):
    grid = [[(0,0,0) for x in range(10)] for y in range(20)]
     
     #j is the x, i is the y... 
    for i in range (len(grid)):
        for j in range (len(grid[i])):
            if (j,i) in locked_positions:
                lp= locked_positions[(j,i)]
                grid[i][j]= lp
    return grid
    pass


def convert_format_of_tetrimino(tetriminos):
    pass
def legit_space (tetriminos,grid):
    pass
def lost_check(positions):
    pass
def grabing_tetrimino():
    pass
