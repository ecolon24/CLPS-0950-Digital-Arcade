import pygame
import random 
import sys

pygame.init()

#Global Variables 
screen_width= 800
screen_height= 700 
play_width=300
play_height= 600
block_size= 30
background_color_main= (0,0,0)
r= (255,0,0)

#font to use in the game
text_font= pygame.font.SysFont('Fixedsys', 20)
#font for leaving the game if you desire halfway through!
quit_text= text_font.render('Quit', True, r)

#making the window to open Tetris  (works now)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Digital Aracde')
screen.fill(background_color_main)

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
tetrimino_colors= [(0,255,0), (255,0,0), (0,255,255),(255,255,0),(225,165,0),(0,0,255),(128,0,128)] #should make colors variables? would be a more "efficient" way to read.  


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


def convert_format_of_tetrimino(tetriminos):
    pass
def legit_space (tetriminos,grid):
    pass
def lost_check(positions):
    pass

#ensures that the pieces being grabbed are in a random order--> User can't predict the pattern + always win the Tetris game! Fixed an intial concern we had :) 
def grabbing_tetrimino(tetriminos):
    return Piece(5,0, random.choice(tetriminos))

#the code that actually draws the grid on the screen display! Have to account for different color the the blocks composing the grid
#needs to be 2D, like a mathematical grid. use rows +columns 
def drawing_the_gridlines(surface,grid): 

def window_draw (surface,grid): 
    surface.fill= ((0,0,0))#background intially is black. 
    
    #Creating the Tetris label + Drawing it on the Screen!
    pygame.font.init()
    Tetris_font= pygame.font.SysFont('Fixedsys', 40)
    title_label= Tetris_font.render('Tetris', 1, (255,0,0)) #red for now; can I make each letter a dif color? more nostalgic this way!
    surface.blit(title_label, (upper_left_x + (play_width//2)-title_label.get_width), 30) #will center the text in the middle of the X axis, malleable if I were to change the screen size. y is fixed at the top of the screen, so just choose a value + see?

    #Actually drawing the grid now; i = x coordinate, j= y coordinate? 
    for i in range (len(grid)):
        for j in range (len(grid[i])):
            pygame.draw.rect((surface, grid[i][j], upper_left_x+j*block_size, upper_left_y+i*block_size, block_size, block_size)) #creates blocks horizontally+vertically
    pygame.draw.surface(surface, (128,128,128), (upper_left_x, upper_left_y, play_width, play_height),4) #grey rectangle that surrounds the border of the grid!

    drawing_the_grid(surface,grid)
    pygame.display.update()

def figure_main_movement():
    #have to account for "locking" the pieces in place. 
    locked_positions= {}
    grid= create_grid(locked_positions)

    #current piece + piece on deck + possible avenues
    current_tetrimino= grabbing_tetrimino()
    next_tetrimino = grabbing_tetrimino()
    change_tetrimino= False
    run_it=True

    #fall time for the piece + creating a clock function (time is key in Tetris)
    fall_time= 0 
    clock= pygame.time.Clock()

    while run_it: 
        for event in pygame.event.get:
            #quitting the game when desired!
            if event.type == pygame.QUIT:
                sys.exit
            #hardcoding in the keys the user will use to move/rotate the tetrimino. Pretty self explanatory for the most part. 
            if event.type== pygame.KEYDOWN: #be sure to account for moving tetriminos off the grid; wanna make sure this doesn't happen.
                if event.key== pygame.K_LEFT:
                    current_tetrimino.x -=1
                    if not legit_space(current_tetrimino,grid): 
                        current_tetrimino.x +=1
                if event.key== pygame.K_RIGHT:
                    current_tetrimino.x += 1
                    if not legit_space(current_tetrimino, grid):
                        current_tetrimino.x -=1
                #can't move up in Tetris, makes sense to use the up key as a rotation button!
                if event.key == pygame.K_UP:
                    current_tetrimino.rotation +=1
                    if not legit_space(current_tetrimino, grid):
                        current_tetrimino.rotation-=1
                if event.key == pygame.K_DOWN:
                    current_tetrimino.y -=1
                    if not legit_space(current_tetrimino,grid):
                        current_tetrimino.y -=1






