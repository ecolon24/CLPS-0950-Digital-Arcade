import pygame
import sys
import random
import losescreen
import winscreen

def game():
    pygame.init()


    #dimensions of window
    (width, height) = (1200, 800)
    background_colour = (204,229,255)
    button_light = (170,170,170)
    button_dark = (140,140,140)
    black = (0,0,0)
    white = (255,255,255)
    red = (255,0,0)

    #initialising variables
    score = 0 
    gamespeed = 5
    difficulty = 1
    snake_height = 20
    snake_length = 20
    special_food_spawn = False
    running = True
    food_spawn = True
    newdirection = []
    direction = []
    snake_score = 2

    #initialising text
    textfont = pygame.font.SysFont('Arial',18)
    quittext = textfont.render('Quit' , True , black)
    diffup = textfont.render('Harder' , True , black)
    diffdown = textfont.render('Easier' , True , black)
    instruc1 = textfont.render('use the arrow keys' , True , black)
    instruc2 = textfont.render('to control the snake!' , True , black)
    instruc3 = textfont.render('try to get to 500!' , True , black)

    
    clock = pygame.time.Clock()


    #creating the window
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Digital Aracde')
    screen.fill(background_colour)
    pygame.display.flip()

    #creating snake dimensions and location
    snake_body = [  [600, 400],
                    [580, 400],
                    [560, 400],
                ]
    snake_position = [width/2, height/2]

    #spawning food on a 20x20 grid
    foodx = round(random.randrange(300, 880) / 20.0) * 20.0
    foody = round(random.randrange(100, 680) / 20.0) * 20.0
    food_spawn = True

    #function for spawning food
    def generate_food():
        while True:
            foodx = round(random.randrange(300, 880) / 20.0) * 20.0
            foody = round(random.randrange(100, 680) / 20.0) * 20.0
                # Check if the generated position is not occupied by the snake's body
            if [foodx, foody] not in snake_body: 
                break  # Exit the while loop once a valid position is found

        return foodx, foody

    foodx, foody = generate_food()
    
    #main game loop
    while running:
       mouse = pygame.mouse.get_pos()
      
       #hover colour changes for the quit button in the corner
       if width-180 <= mouse[0] <= width-40 and height-80 <= mouse[1] <= height-40:
           pygame.draw.rect(screen,button_light,[width-180,height-80,140,40])   
       else:
           pygame.draw.rect(screen,button_dark,[width-180,height-80,140,40])

       #hover colour changes for the difficulty buttons
       if width-180 <= mouse[0] <= width-40 and 80 <= mouse[1] <= 120:
           pygame.draw.rect(screen,button_light,[width-180,80,140,40])   
       else:
           pygame.draw.rect(screen,button_dark,[width-180,80,140,40])

       if width-180 <= mouse[0] <= width-40 and 150 <= mouse[1] <= 190:
           pygame.draw.rect(screen,button_light,[width-180,150,140,40])   
       else:
           pygame.draw.rect(screen,button_dark,[width-180,150,140,40])

    
       #displaying the current score on screen
       screen.blit(quittext , (width-130,height-70))
       score_text = textfont.render('Score: ' + str(score), True, black)
       screen.blit(score_text, (10, 10)) 

       #displaying the current difficulty on screen
       diff_text = textfont.render('Difficulty: ' + str(difficulty), True, black)
       screen.blit(diff_text, (10, 50))
       screen.blit(diffup, (width-140, 90)) 
       screen.blit(diffdown, (width-140, 160))

       pygame.display.update()
      
       
       #if snake hits the edges of the screen, import losescreen
       if snake_position[0] < 300 or snake_position[0]+snake_height > 900 or snake_position[1] < 100 or snake_position[1]+snake_height > 700:
           running = False
           losescreen.losing() 
          

       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               running=False
           elif event.type == pygame.MOUSEBUTTONDOWN:
               #functionality for the quit button
               if width-180 <= mouse[0] <= width-40 and height-80 <= mouse[1] <= height-40:
                   running = False
                   pygame.quit()
                   sys.exit()
               #functionality for the difficulty buttons
               if width-180 <= mouse[0] <= width-40 and 80 <= mouse[1] <= 120:
                   if gamespeed < 24:
                        gamespeed+=1
                        difficulty += 1
               if width-180 <= mouse[0] <= width-40 and 150<= mouse[1] <= 190:
                   if gamespeed > 5:
                        gamespeed-=1
                        difficulty -= 1
                   
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

       #make sure snaks stays consistent length
       snake_body.insert(0, list(snake_position))
       if len(snake_body) > snake_score:  
            snake_body.pop()

       #if the head of the snake is on the food, it grows in length
       if snake_position[0] == foodx and snake_position[1] == foody:
            if special_food_spawn == True:
            # Handle interaction with speical food
                food_spawn = True
                snake_score += 3
                score += 30
                score_text = textfont.render('Score: ' + str(score), True, black)
                foodx, foody = generate_food()
                special_food_spawn = False
            else:
                food_spawn = True
                snake_score += 1
                score += 10
                score_text = textfont.render('Score: ' + str(score), True, black)
                foodx, foody = generate_food()
                    
            if random.random() < 0.1:  # 10% chance of spawning special food
                special_food_spawn = True
    

       else:
            snake_body.pop()
        
       #drawing the game screen
       pygame.draw.rect(screen, black, [300, 100, 600, 600])

       #drawing the snaek
       for pos in snake_body:
        pygame.draw.rect(screen, white,[pos[0], pos[1], snake_height, snake_length])
        
       #self collision mechanics
       if snake_position in snake_body[1:]:
            if (snake_position in snake_body[1:]) and (len(snake_body) > 3):
                running = False
                losescreen.losing()

       #winning screen if the score hits 500
       if snake_score == 500:
           running = False
           winscreen.winning() 
                 
       #cleaning up border
       pygame.draw.rect(screen, background_colour, [0, 0, width, 100])
       pygame.draw.rect(screen, background_colour, [0, 0, 300, height])
       pygame.draw.rect(screen, background_colour, [900, 0, width/2, height])
       pygame.draw.rect(screen, background_colour, [0, 700, width, height/2])

       if food_spawn == True: 
            if special_food_spawn == True:
                pygame.draw.rect(screen, red, [foodx, foody, 20, 20])
            else: 
                pygame.draw.rect(screen, background_colour, [foodx, foody, 20, 20])

       #displaying instructions
       screen.blit(instruc1, (20, 650)) 
       screen.blit(instruc2, (20, 670)) 
       screen.blit(instruc3, (20, 690)) 
            
       #set speed of clock
       clock.tick(gamespeed)

if __name__ == "__main__":
	game()

