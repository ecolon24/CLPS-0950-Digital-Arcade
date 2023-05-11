import random
import losescreen
import sys
import pygame 
import requests
import io
from pygame import mixer
import tkinter as tk

pygame.init()
pygame.font.init()
pygame.mixer.init()


#Global Variables + Audios
screen_width= 800
screen_height= 700 
play_width=300
play_height= 600
block_size= 30

#creating the music
Tetris_theme_music = 'Tetris Theme Song.mp3'
mixer.music.load(Tetris_theme_music)


#play area 
upper_left_x= (screen_width-play_width)//2
upper_left_y= screen_height - play_height

#Making the shapes of the blocks; accounting for different rotations+positioning
#0 will represent where the block actually is placed, 5X5 setup!
#have a notability file on Ipad that draws out all the different orientations; took some time!
S_shape= [['.....',
           '.....',
           '..00.',
           '.00..',
           '.....'],
           ['.....',
            '..0..',
            '..00.',
            '...0.',
            '.....']]

Z_shape= [['.....',
           '.....',
           '.00..',
           '..00.',
           '.....'],
           ['.....',
            '..0..',
            '.00..',
            '.0...',
            '.....']]

I_shape= [['..0..',
           '..0..',
           '..0..',
           '..0..',
           '.....'],
           ['.....',
            '0000.',
            '.....',
            '.....',
            '.....']]

O_shape=[['.....',
          '.....',
          '.00..',
          '.00..',
          '.....']]

#O_shape only has one configuration because a square when rotated still has the same shape!
J_shape= [['.....',
           '.0...',
           '.000.',
           '.....',
           '.....'],
           ['.....',
            '.....',
            '.000.',
            '...0.',
            '.....'],
            ['.....',
             '..0..',
             '..0..',
             '.00..',
             '.....'],
             ['.....',
              '..00.',
              '..0..',
              '..0..',
              '.....']]

L_shape= [['.....',
           '...0.',
           '.000.',
           '.....',
           '.....'],
           ['.....',
            '..0..',
            '..0..',
            '..00.'],
            ['.....',
             '.....',
             '.000.',
             '.0...',
             '.....'],
             ['.....',
              '.00..',
              '..0..',
              '..0..',
              '.....']]

T_shape= [['.....',
           '..0..',
           '.000.',
           '.....',
           '.....'],
           ['.....',
            '..0..',
            '..00.',
            '..0..',
            '.....'],
            ['.....',
             '..0..',
             '.00..',
             '..0..',
             '.....'],
             ['.....',
              '.....',
              '.000.',
              '..0..',
              '.....']]

#colors 
white= (255,255,255)
red= (255,0,0)
green= (0,255,0)
blue=(0,0,255)
purple= (128,0,128)
yellow= (255,255,0)
cyan= (0,255,255)
orange= (255,165,0)
black=(0,0,0)
grey= (128,128,128)
#Shape Colors! Had to do a bit of research to find these but :) 
#fun fact: Avid tetris fans refer to 'Tetris shapes' as tetriminos!
tetriminos= [S_shape, Z_shape, I_shape, O_shape, J_shape, L_shape, T_shape]
tetrimino_colors= [green, red, cyan,yellow, orange ,blue,purple] #should make colors variables? would be a more "efficient" way to read.  


#function that holds the placement of the pieces!
#new keyword; self! Did a bit of research for it :) 
def game(): 
        
    class Piece(object):
            rows=20
            columns=10
            def __init__(self, column, row, tetrimino):
                self.x= column
                self.y= row
                self.tetrimino = tetrimino
                self.color = tetrimino_colors[tetriminos.index(tetrimino)]
                self.rotation= 0

    def eliminate_full_row(grid, locked_positions):
        # Deleting full rows
        num_eliminated_rows = 0
        for i in range(len(grid)-1, -1, -1):
            row = grid[i]
            if black not in row:
                num_eliminated_rows += 1
                shift= i
                for j in range(len(row)):
                    try:
                        del locked_positions[(j, i)]
                    except:
                        continue

        if num_eliminated_rows > 0:
            for key in sorted(list(locked_positions), key=lambda x: x[1], reverse=True):
                x, y = key
                if y <shift:
                    new_key = (x, y + num_eliminated_rows)
                    locked_positions[new_key] = locked_positions.pop(key)

    #start text
    def instructional_text(text,size,color,surface):
        i_font= pygame.font.SysFont('Fixedsys', size)
        label= i_font.render(text, 1, color)
        surface.blit(label, (upper_left_x+play_width/2 - (label.get_width()/2), upper_left_y + play_height/2 - label.get_height()/2))

    def centered_text(text, size, color, surface):
        font = pygame.font.SysFont('Fixedsys', size)
        label= font.render(text, 1, color)
        surface.blit(label, (upper_left_x+play_width/2 - (label.get_width()/2), upper_left_y + play_height/2 - label.get_height()/2))
        visible=True
        timer_event= pygame.USEREVENT +1
        pygame.time.set_timer(timer_event,500)

        while True: 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    figure_main_movement()
                elif event.type == timer_event:
                    visible = not visible
            surface.fill((0, 0, 0))
        

            if visible:
                surface.blit(label, (upper_left_x+play_width/2 - (label.get_width()/2), upper_left_y + play_height/2 - label.get_height()/2))
            pygame.display.flip()

    def game_over(text,size,color,surface):
        font = pygame.font.SysFont('Fixedsys', size)
        label= font.render(text, 1, color)
        surface.blit(label, (upper_left_x+play_width/2 - (label.get_width()/2), upper_left_y + play_height/2 - label.get_height()/2))


            #creating a list for every row on the grid. 10 blocks width, 20 blocks height!
            #intialize with all black, will fill in with specified colors as the person plays the game.
            #locked_position is for when the user "drops + locks in" their blocks, become static instead of dynamic pieces. keep in mind there is a color change because each tetrimino is a dif color!
    def legit_space (tetriminos,grid):
            #getting every possible position for 10x20 grid, store in tuple!
            all_positions= [[(j, i) for j in range(10) if grid[i][j] == black] for i in range(20)] #can't add in position if there is a tetrimnio--> AKA another color!
            #make list 1D, taking all positions in list+ making 1D, overriding list we had previously! Easier to loops through
            all_positions = [j for sub in all_positions for j in sub]
            #converting tetrimino to positions so we can compare+ check in the tetrimino is a legit space on the grid+not outside it
            format_done= convert_format_of_tetrimino(tetriminos)

            for pos in format_done: 
                if pos not in all_positions:
                    if pos[1] >= 0: #not in valid position if negative value. Think of like a mathematical grid (negative X quadrant)
                        return False
            return True

    def create_grid(locked_positions={}):
            grid = [[black for x in range(10)] for y in range(20)]
            
            #j is the x, i is the y... 
            for i in range (len(grid)):
                for j in range (len(grid[i])):
                    if (j,i) in locked_positions:
                        lp= locked_positions[(j,i)]
                        grid[i][j]= lp
            return grid

    def lost_check(positions):
            for pos in positions:
                x, y = pos
                if y<=0:
                    return True
            return False

        #takes periods/0's in  positions +creates tetriminos
    def convert_format_of_tetrimino(tetrimino):
            positions=[]
            #grabs the specific shape+orientation... sublists in a sense.
            layout= tetrimino.tetrimino[tetrimino.rotation % len(tetrimino.tetrimino)]
            for i, line in enumerate(layout): 
                row=list(line)
                for j, column in enumerate(row): 
                    if column== '0':
                        positions.append((tetrimino.x+j, tetrimino.y+i))
            for i, pos in enumerate(positions): 
                #fixing offset --> move to left/up 
                positions[i] = (pos[0] - 2, pos[1] - 4)
            
            return positions

        #ensures that the pieces being grabbed are in a random order--> User can't predict the pattern + always win the Tetris game! Fixed an intial concern we had :) 
    def grabbing_tetrimino():
            global tetriminos, tetrimino_colors

            return Piece(5, 0, random.choice(tetriminos))


        #the code that actually draws the grid on the screen display! Have to account for different color the the blocks composing the grid
        #needs to be 2D, like a mathematical grid. use rows +columns 
    def drawing_the_gridlines(surface, row, col):
        for i in range(row):
            # drawing vertical lines, y constantly changing w/static x lines
            pygame.draw.line(surface, grey, (upper_left_x, upper_left_y+i*block_size), (upper_left_x+play_width, upper_left_y+i*block_size))
            for j in range(col):
                # drawing horizontal lines, x constantly changing w/static y lines
                pygame.draw.line(surface, grey, (upper_left_x+j*block_size, upper_left_y), (upper_left_x+j*block_size, upper_left_y+play_height))


    def window_draw(surface):
        surface.fill(black)

        # Creating the Tetris label + Drawing it on the Screen!
        Tetris_font = pygame.font.SysFont('Fixedsys', 70)
        title_label_T = Tetris_font.render('T', True, purple)
        title_label_E = Tetris_font.render('E', True, orange)
        title_label_T_2 = Tetris_font.render('T', True, purple)
        title_label_R = Tetris_font.render('R', True, green)
        title_label_I = Tetris_font.render('I', True, cyan)
        title_label_S = Tetris_font.render('S', True, red)
        complete_title = [title_label_T, title_label_E, title_label_T_2, title_label_R, title_label_I, title_label_S]

        offset_x = upper_left_x + play_width / 2 - sum(label.get_width() for label in complete_title) / 2
        offset_y = 30
        for label in complete_title:
            surface.blit(label, (offset_x, offset_y))
            offset_x += label.get_width()

        # Actually drawing the grid now; i = x coordinate, j = y coordinate?
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                pygame.draw.rect(surface, grid[i][j], (upper_left_x+j*block_size, upper_left_y+i*block_size, block_size, block_size), 0) # creates blocks horizontally+vertically
        drawing_the_gridlines(surface, 20, 10)
        pygame.draw.rect(surface, grey, (upper_left_x, upper_left_y, play_width, play_height), 5) # grey rectangle that surrounds the border of the grid!

        pygame.display.update()

    def next_tetrimino_display(tetrimino, surface):
        font = pygame.font.SysFont('Fixedsys', 25)
        label = font.render('Next', True, (255, 255, 255))
        surface.blit(label, (upper_left_x + play_width + 50, upper_left_y + play_height/2 - 80))

        layout = tetrimino.tetrimino[tetrimino.rotation % len(tetrimino.tetrimino)]
        for i, line in enumerate(layout):
            horizont = list(line)
            for j, column in enumerate(horizont):
                if column == '0':
                    color = tetrimino.color
                    pygame.draw.rect(surface, color, (upper_left_x + play_width + 50 + j*block_size, upper_left_y + play_height/2 - 100 + i*block_size, block_size, block_size), 0)
                    block_label = font.render(column, True, pygame.Color(color))
                    surface.blit(block_label, (upper_left_x + play_width + 50 + j*block_size + block_size/2 - block_label.get_width()/2, upper_left_y + play_height/2 - 100 + i*block_size + block_size/2 - block_label.get_height()/2))



    def figure_main_movement():
            mixer.music.play(loops=-1) 
            global grid
            #have to account for "locking" the pieces in place. 
            locked_positions= {}
            grid= create_grid(locked_positions)
            #current piece + piece on deck + possible avenues
            current_tetrimino= grabbing_tetrimino()
            next_tetrimino = grabbing_tetrimino()
            change_tetrimino= False
            running= True
            #fall time for the piece + creating a clock function (time is key in Tetris)
            fall_time= 0 
            clock= pygame.time.Clock()

            while running: 
                fall_speed= 0.29
                grid= create_grid(locked_positions)
                fall_time +=clock.get_rawtime()
                clock.tick() #will run same speed no matter the computer

                if fall_time/1000 >= fall_speed: 
                    fall_time= 0
                    current_tetrimino.y +=1
                    #hitting another piece or bottom of play area. Next piece will be generated!
                    if not (legit_space(current_tetrimino,grid)) and current_tetrimino.y>=1:
                        current_tetrimino.y-=1 
                        change_tetrimino= True
                for event in pygame.event.get():
                    #quitting the game when desired!
                    if event.type == pygame.QUIT:
                        running= False
                        pygame.display.quit()
                        quit()
                    #hardcoding in the keys the user will use to move/rotate the tetrimino. Pretty self explanatory for the most part. 
                    if event.type== pygame.KEYDOWN: #be sure to account for moving tetriminos off the grid; wanna make sure this doesn't happen.
                        if event.key== pygame.K_LEFT:
                            current_tetrimino.x -=1
                            if not (legit_space(current_tetrimino,grid)): 
                                current_tetrimino.x +=1
                        elif event.key== pygame.K_RIGHT:
                            current_tetrimino.x += 1
                            if not (legit_space(current_tetrimino, grid)):
                                current_tetrimino.x -=1
                        #can't move up in Tetris, makes sense to use the up key as a rotation button!
                        elif event.key == pygame.K_UP:
                            current_tetrimino.rotation = current_tetrimino.rotation +1 % len(current_tetrimino.tetrimino)
                            if not (legit_space(current_tetrimino, grid)):
                                current_tetrimino.rotation= current_tetrimino.rotation - 1% len(current_tetrimino.tetrimino)
                        if event.key == pygame.K_DOWN:
                            current_tetrimino.y +=1
                            if not (legit_space(current_tetrimino,grid)):
                                current_tetrimino.y -=1
                        if event.key== pygame.K_SPACE:
                            while legit_space(current_tetrimino, grid):
                                current_tetrimino.y+=1
                            current_tetrimino.y-=1
                            print(convert_format_of_tetrimino(current_tetrimino))                           

                tetrimino_position= convert_format_of_tetrimino(current_tetrimino)

                for i in range (len(tetrimino_position)):
                    x, y= tetrimino_position[i]
                    if y>= 0:
                        grid [y][x] = current_tetrimino.color 
                if change_tetrimino:
                    #structure: gives key of postion + associated color
                    for pos in tetrimino_position: 
                        locked_positions[(pos[0], pos[1])] = current_tetrimino.color
                    current_tetrimino= next_tetrimino
                    next_tetrimino= grabbing_tetrimino()
                    change_tetrimino= False

                    eliminate_full_row(grid, locked_positions)
                
                window_draw(win)
                next_tetrimino_display(next_tetrimino,win)
                pygame.display.update()

                if lost_check(locked_positions): 
                    running= False
                    mixer.music.stop()
            win.fill(black)
            game_over('GAME OVER :(', 60, white, win)
            pygame.display.update()
            pygame.time.delay(3000)

            losescreen.losing()#look into this

    def startup_screen():
            running = True
            while running:
                win.fill(black)
                instructional_text('Welcome to Tetris. The instructions are pretty simple.', 40, white, win)
                pygame.display.update()
                pygame.time.delay(4000)
                win.fill(black)
                instructional_text('Move and rotate tetriminos coming from the top to form complete rows.', 30, white, win)
                pygame.display.update()
                pygame.time.delay(4000)
                win.fill(black)
                instructional_text('The right key moves the tetrimino right.', 35, white, win)
                pygame.display.update()
                pygame.time.delay(4000)
                win.fill(black)
                instructional_text('The left key moves the tetrimino left.', 35, white, win)
                pygame.display.update()
                pygame.time.delay(4000)
                win.fill(black)
                instructional_text('The up key rotates the tetrimino.', 35, white, win)
                pygame.display.update()
                pygame.time.delay(4000)
                win.fill(black)
                instructional_text('The down key moves the tetrimino down the screen.',35, white, win)
                pygame.display.update()
                pygame.time.delay(4000)
                win.fill(black)
                instructional_text('Good luck!',40,white, win)
                pygame.display.update()
                pygame.time.delay(3000)
                win.fill(black)
                centered_text('PRESS TO START', 40, (255,255,255), win)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.KEYDOWN:
                        figure_main_movement()
                                        
            pygame.quit()
        
        
    win = pygame.display.set_mode((screen_width, screen_height))

    startup_screen()

if __name__ == "__main__":
    game()