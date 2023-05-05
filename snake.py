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

foodx = round(random.randrange(0, 700 - snake_height) / 10.0) * 10.0
foody = round(random.randrange(0, 700 - snake_height) / 10.0) * 10.0

#creating the window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Digital Aracde')
screen.fill(background_colour)
pygame.display.flip()



def snake():
    global width, height, snake_x, snake_y, snake_height, snake_length, x_move, y_move, foodx, foody
    running = True
    while running: 
        mouse = pygame.mouse.get_pos()
        
        if width-180 <= mouse[0] <= width-40 and height-80 <= mouse[1] <= height-40:
            pygame.draw.rect(screen,button_light,[width-180,height-80,140,40])    
        else:
            pygame.draw.rect(screen,button_dark,[width-180,height-80,140,40])
        screen.blit(quittext , (width-130,height-70))
        
        pygame.display.update() 
        
        if snake_x < width/2-350 or snake_x > width/2+350 or snake_y < height/2-350 or snake_y > height/2+350:
            import losescreen

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if width-180 <= mouse[0] <= width-40 and height-80 <= mouse[1] <= height-40:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_move = -10
                    y_move = 0
                elif event.key == pygame.K_RIGHT:
                    x_move = 10
                    y_move = 0
                elif event.key == pygame.K_UP:
                    x_move = 0
                    y_move = -10
                elif event.key == pygame.K_DOWN:
                    x_move = 0
                    y_move = 10
                elif event.key == pygame.K_1:
                    snake_length += 5
       
        snake_x += x_move
        snake_y += y_move
        pygame.draw.rect(screen, black, [width/2-350, height/2-350, 700, 700])
        pygame.draw.rect(screen, white, [snake_x, snake_y, 20, 20])
        
        #cleaning up border
        pygame.draw.rect(screen, background_colour, [0, 0, width, height/2-1050])
        pygame.draw.rect(screen, background_colour, [0, 0, height, width/2-1050])
        pygame.draw.rect(screen, background_colour, [0, height/2+350, width, height/2])
        pygame.draw.rect(screen, background_colour, [width/2+350, 0, height/2, width])

        #set speed of clock
        clock.tick(30)




snake()

