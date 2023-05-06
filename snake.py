import pygame
import sys
import random
#import losescreen
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


snake_body = [  [600, 400],
               [580, 400],
               [560, 400],
               [540, 400],
               [520, 400]
           ]

snake_position = [width/2, height/2]

#spawning food on a 20x20 grid
foodx = round(random.randrange(width/2-320, width/2+320) / 20.0) * 20.0
foody = round(random.randrange(height/2-320, height/2+320) / 20.0) * 20.0
food_position = [foodx, foody]
food_spawn = True




def game():
   global width, height, snake_height, snake_length, x_move, y_move, foodx, foody
   running = True
   food_spawn = True
   newdirection = []
   direction = []



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
       if snake_position[0] < 300 or snake_position[0]+snake_height > 900 or snake_position[1] < 100 or snake_position[1]+snake_height > 700:
           running = False
           #losescreen.losescreen() 
          

       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               running=False
           #functionality for the quit button
           elif event.type == pygame.MOUSEBUTTONDOWN:
               if width-180 <= mouse[0] <= width-40 and height-80 <= mouse[1] <= height-40:
                   running = False
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
           snake_position[0] -= 20
       elif direction == 'right':
           snake_position[0] += 20
       elif direction == 'up':
           snake_position[1] -= 20
       elif direction == 'down':
           snake_position[1] += 20


       snake_body.insert(0, list(snake_position))
       for i in range(1, len(snake_body)):
            snake_body[i] = list(snake_body[i - 1])

       #if the head of the snake is on the food, it grows in length
       if snake_position[0] == foodx and snake_position[1] == foody:
            food_spawn = True
            foodx = round(random.randrange(width/2-320, width/2+320) / 20.0) * 20.0
            foody = round(random.randrange(height/2-320, height/2+320) / 20.0) * 20.0
       else:
            snake_body.pop()


       pygame.draw.rect(screen, black, [300, 100, 600, 600])

       for pos in snake_body:
        pygame.draw.rect(screen, white,[pos[0], pos[1], snake_height, snake_length])

       if food_spawn == True:
            pygame.draw.rect(screen, red, [foodx, foody, 20, 20])
            
      
       #cleaning up border
       pygame.draw.rect(screen, background_colour, [0, 0, width, 100])
       pygame.draw.rect(screen, background_colour, [0, 0, 300, height])
       pygame.draw.rect(screen, background_colour, [900, 0, width/2, height])
       pygame.draw.rect(screen, red, [0, 700, width, height/2])


       #set speed of clock
       clock.tick(5)






game()
