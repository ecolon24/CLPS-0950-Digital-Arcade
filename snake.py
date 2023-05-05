import pygame
import sys
import random
pygame.init()

#dimensions of window
(width, height) = (1200, 800)
background_colour = (204,229,255)
button_light = (170,170,170)
button_dark = (140,140,140)
black = (0,0,0)
white = (255,255,255) 
red = (255,0,0)

textfont = pygame.font.SysFont('Arial',18)
bigfont = pygame.font.SysFont('Arial',30)
quittext = textfont.render('Quit' , True , black)

snake_height = 20
snake_length = 20
snake_x = width // 2 - snake_height // 2
snake_y = height // 2 - snake_length // 2
x_move = 0
y_move = 0
snake_colour = (255, 0, 0)

clock = pygame.time.Clock()

#creating the window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Digital Aracde')
screen.fill(background_colour)
pygame.display.flip()



def snake():
    global width, height, snake_x, snake_y, snake_height, snake_length, x_move, y_move
    running = True
    newdirection = []
    direction = []

    #spawning food on a 10/10 grid 
    foodx = round(random.randrange(width/2-320, width/2+320) / 10.0) * 10.0
    foody = round(random.randrange(height/2-320, height/2+320) / 10.0) * 10.0

    while running: 
        mouse = pygame.mouse.get_pos()
        
        #functionality for the quit button in the corner 
        if width-180 <= mouse[0] <= width-40 and height-80 <= mouse[1] <= height-40:
            pygame.draw.rect(screen,button_light,[width-180,height-80,140,40])    
        else:
            pygame.draw.rect(screen,button_dark,[width-180,height-80,140,40])
        screen.blit(quittext , (width-130,height-70))
        
        pygame.display.update() 
        
        
        #if snake hits the edges of the screen, import losescreen
        if snake_x < width/2-350 or snake_x > width/2+350 or snake_y < height/2-350 or snake_y > height/2+350:
            import losescreen


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
            #functionality for the quit button 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if width-180 <= mouse[0] <= width-40 and height-80 <= mouse[1] <= height-40:
                    pygame.quit()
                    sys.exit()
            #makes the snake plan to move in direction of arrow key 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    newdirection = 'left'
                elif event.key == pygame.K_RIGHT:
                    newdirection = 'right'
                elif event.key == pygame.K_UP:
                    newdirection = 'up'
                elif event.key == pygame.K_DOWN:
                    newdirection = 'down'

        #checks to make sure snake is not doubling back on itself
        if newdirection == 'up' and direction != 'down':
            direction = 'up'
        if newdirection == 'down' and direction != 'up':
            direction = 'down'
        if newdirection == 'left' and direction != 'right':
            direction = 'left'
        if newdirection == 'right' and direction != 'left':
            direction = 'right'
        
        #moves snake along arrow key
        if direction == 'left':
            x_move = -snake_height
            y_move = 0
        elif direction == 'right':
            x_move = snake_height
            y_move = 0
        elif direction == 'up':
            x_move = 0
            y_move = -snake_height
        elif direction == 'down':
            x_move = 0
            y_move = snake_height

        #if the head of the snake is on the food, it grows in length
        if snake_x < foodx and foodx < snake_x + snake_height and  snake_y < foody and foody < snake_y+snake_height:
            snake_length += snake_height
       
        #moving the snake
        snake_x += x_move
        snake_y += y_move
        pygame.draw.rect(screen, black, [width/2-350, height/2-350, 700, 700])
        pygame.draw.rect(screen, white, [snake_x, snake_y, snake_height, snake_length])
        pygame.draw.rect(screen, red, [foodx, foody, 10, 10])
        
        #cleaning up border
        pygame.draw.rect(screen, background_colour, [0, 0, width, height/2-1050])
        pygame.draw.rect(screen, background_colour, [0, 0, height, width/2-1050])
        pygame.draw.rect(screen, background_colour, [0, height/2+350, width, height/2])
        pygame.draw.rect(screen, background_colour, [width/2+350, 0, height/2, width])

        #set speed of clock
        clock.tick(5)




snake()

