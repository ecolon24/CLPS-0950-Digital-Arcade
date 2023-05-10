import pygame
import sys
import time
import turtle
import random
from random import randint
from pygame import mixer


def game():
    pygame.init()
    mixer.init()
    def oneplayer():

        (width, height) = (965, 590)
        pygame.display.update()
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('COUNTDOWN')
        pygame.display.update() 
        backgroundinstructions = pygame.image.load("Documents/Github/CLPS-0950-Digital-Arcade/instructions1.png")
        background3 = pygame.image.load("Documents/Github/CLPS-0950-Digital-Arcade/3.png")
        background2 = pygame.image.load("Documents/Github/CLPS-0950-Digital-Arcade/2.png")
        background1 = pygame.image.load("Documents/Github/CLPS-0950-Digital-Arcade/1.png")

        screen.blit(backgroundinstructions, (0,0))
        pygame.display.update()
        time.sleep(5)

        screen.blit(background3, (0,0))
        pygame.display.update()
        time.sleep(1)
        
        screen.blit(background2, (0,0))
        pygame.display.update()
        time.sleep(1)
       
        screen.blit(background1, (0,0))
        pygame.display.update()
        time.sleep(1)

        #game for one player!
        wwidth, wheight = 700, 500
        screen = pygame.display.set_mode((wwidth, wheight))
        pygame.display.set_caption("Single Player Pong Game")
        black = (0,0,0)
        white = (255,255,255)
        FPS = pygame.time.Clock()

        #speed = 5
        ballx = 3
        bally = 3
        bouncesound = mixer.music.load("Documents/Github/CLPS-0950-Digital-Arcade/boing2.mp3")
        mixer.music.set_volume(0.4)
        score = 0
        game_font = pygame.font.Font("freesansbold.ttf", 20)

        player = pygame.Rect(275,450,100,10)
        ball = pygame.Rect(290,290,10,10)

        def show():
            FPS.tick(60)
            screen.fill(black)
            pygame.draw.rect(screen,white,player)
            pygame.draw.ellipse(screen,white,ball)

        def move():
            if keys[pygame.K_RIGHT]:
                player.x += 5
                if player.x >= 595:
                    player.x = 595
            elif keys[pygame.K_LEFT]:
                player.x -= 5
                if player.x <= 5:
                    player.x = 5


        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            
            ball.x += ballx
            ball.y += bally
            

            
            #ball.direction = 1,1
            #ball.speed = 7

            if ball.top <= 0:
                bally += 1 
            if ball.bottom >= wheight:
                bally -= 1
            if ball.left <= 0:
                ballx += 1
            if ball.right >= wwidth:
                ballx -= 1

            
            if ball.colliderect(player):
                bally += -7
                ballx += 0.1
                score += 1
                mixer.music.play()

            if ball.y >= 475:
                bally = 0
                ballx = 0
                speed = 0

        
            keys = pygame.key.get_pressed()
            show()
            move()

            pt = game_font.render(f"{score}",False,white)
            screen.blit(pt, (350,100))

            pygame.display.update()

 



        

    def twoplayer():
        white = (255,255,255)
        
        #countdown 
        (width, height) = (965, 590)
        pygame.display.update()
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('COUNTDOWN')
        pygame.display.update() 
        backgroundinstructions = pygame.image.load("Documents/Github/CLPS-0950-Digital-Arcade/instructions2.png")
        background3 = pygame.image.load("Documents/Github/CLPS-0950-Digital-Arcade/3.png")
        background2 = pygame.image.load("Documents/Github/CLPS-0950-Digital-Arcade/2.png")
        background1 = pygame.image.load("Documents/Github/CLPS-0950-Digital-Arcade/1.png")


        screen.blit(backgroundinstructions, (0,0))
        pygame.display.update()
        time.sleep(7)

        screen.blit(background3, (0,0))
        pygame.display.update()
        time.sleep(1)
        
        screen.blit(background2, (0,0))
        pygame.display.update()
        time.sleep(1)
       
        screen.blit(background1, (0,0))
        pygame.display.update()
        time.sleep(1)
           

        #actual game for two players! 
        wwidth, wheight = 700, 500
        screen = pygame.display.set_mode((wwidth, wheight))
        pygame.display.set_caption("Two Player Pong Game")

        white = (255, 255, 255)
        purpleblue = (123,104,238)
        black = (0, 0, 0)

        class Ball:
            def __init__(self, x, y):
                self.x = x
                self.y = y
                self.radius = 10
                self.color = (255, 255, 255)

            def move(self):
                self.x += BALL_VELOCITY[0]
                self.y += BALL_VELOCITY[1]

            def draw(self, window):
                pygame.draw.circle(window, self.color, (int(self.x), int(self.y)), self.radius)

            def hit_paddle(self, paddle):
                if (self.x - self.radius <= paddle.x + paddle.width and
                    self.x + self.radius >= paddle.x and
                    self.y + self.radius >= paddle.y and
                    self.y - self.radius <= paddle.y + paddle.height):
                    return True
                else:
                    return False

            def hit_wall(self):
                if self.y - self.radius <= 0 or self.y + self.radius >= wheight:
                    return True
                else:
                    return False

            def off_screen_left(self):
                if self.x + self.radius <= 0:
                    return True
                else:
                    return False

            def off_screen_right(self):
                if self.x - self.radius >= wwidth:
                    return True
                else:
                    return False
                

        class Paddle:
            COLOR = purpleblue
            VEL = 4

            def __init__(self, x, y, width, height):
                self.x = self.original_x = x
                self.y = self.original_y = y
                self.width = width
                self.height = height

            def draw(self, win):
                pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))

            def move(self, up=True):
                if up:
                    self.y -= self.VEL
                else:
                    self.y += self.VEL


            def reset(self):
                self.x = self.original_x
                self.y = self.original_y


        BALL_VELOCITY = [4,4]
        player1_score = 0
        player2_score = 0
        font = pygame.font.Font("freesansbold.ttf", 50)

        player1 = Paddle(10, wheight//2 - 100 //2, 20, 100)
        player2 = Paddle(wwidth - 10 - 20, wheight //2 - 100//2, 20, 100)
        ball = Ball(wwidth//2,wheight//2)

        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        player1.move_up()
                    elif event.key == pygame.K_s:
                        player1.move_down()
                    elif event.key == pygame.K_UP:
                        player2.move_up()
                    elif event.key == pygame.K_DOWN:
                        player2.move_down()

    # Move the ball
            ball.move()

    # Check for collisions
            if ball.hit_paddle(player1) or ball.hit_paddle(player2):
                BALL_VELOCITY[0] *= -1.1
                BALL_VELOCITY[1] *= 1.1
            if ball.hit_wall():
                BALL_VELOCITY[1] *= -1
            if ball.off_screen_left():
                player2_score += 1
                ball = Ball(wwidth // 2, wheight // 2)
                BALL_VELOCITY = [random.choice([-4, 4]), random.choice([-4, 4])]
            elif ball.off_screen_right():
                player1_score += 1
                ball = Ball(wwidth // 2, wheight // 2)
                BALL_VELOCITY = [random.choice([-4, 4]), random.choice([-4, 4])]

    # Draw the objects on the screen
            screen.fill((0, 0, 0))
            player1.draw(screen)
            player2.draw(screen)
            ball.draw(screen)

    # Draw the scores on the screen
            player1_text = font.render(str(player1_score), 1, (255, 255, 255))
            player2_text = font.render(str(player2_score), 1, (255, 255, 255))
            screen.blit(player1_text, (wwidth // 4 - player1_text.get_width() // 2, 10))
            screen.blit(player2_text, (3 * wwidth // 4 - player2_text.get_width() // 2, 10))

    # Update the display
            pygame.display.update()

# Clean up the Pygame window
        pygame.quit()



       # pwidth, pheight = 20, 90
       # ballsize = 6

       # SCORE_FONT = pygame.font.SysFont("comicsans", 50)
       #winscore = 6


        #class player:
            #color = purpleblue
            #speed = 4

            #def __init__(self, x, y, width, height):
                #self.x = self.original_x = x
                #self.y = self.original_y = y
                #self.width = width
                #self.height = height

            #def show(self):
                #pygame.draw.rect(screen, self.color, self.x, self.y, self.width, self.height)

            #def playerup(self, spacing):
                #self.rect.y -= spacing
                #if self.rect.y <0:
                    #self.rect.y =0
            
            #def playerdown(self, spacing):
                #self.rect.y += spacing
                #if self.rect.y > 400:
                    #self.rect.y =400

                

            #def playermove(self, moveup=True):
                #if moveup:
                   # self.y -= self.speed
                #else:
                    #self.y += self.speed

            #def reset(self):
                #self.x = self.original_x
                #self.y = self.original_y


        #class Ball(pygame.sprite.Sprite):
            #MAX_VEL = 5
            #color = white

           #def __init__(self, x, y, radius):
                #self.x = self.original_x = x
                #self.y = self.original_y = y
                #self.radius = radius
                #self.x_vel = self.MAX_VEL
                #self.y_vel = 0

            #def show(self):
 #               pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
#
   #         def move(self):
  #              self.x += self.x_vel
 #               self.y += self.y_vel
#
    #        def reset(self):
   #             self.x = self.original_x
  #              self.y = self.original_y
 #               self.y_vel = 0
#                self.x_vel *= -1


        #def draw(win, paddles, ball, left_score, right_score):
         #   win.fill(black)

          #  left_score_text = SCORE_FONT.render(f"{left_score}", 1, white)
         #   right_score_text = SCORE_FONT.render(f"{right_score}", 1, white)
        #    win.blit(left_score_text, (wwidth//4 - left_score_text.get_width()//2, 20))
       #     win.blit(right_score_text, (wwidth * (3/4) -
       #                                 right_score_text.get_width()//2, 20))

      #      for paddle in paddles:
     #           paddle.draw(win)

    #        for i in range(10, wheight, wheight//20):
           #     if i % 2 == 1:
          #          continue
         #       pygame.draw.rect(win, white, (wwidth//2 - 5, i, 10, wheight//20))

        #    ball.draw(win)
       #     pygame.display.update()


      #  def handle_collision(ball, left_paddle, right_paddle):
       #     if ball.y + ball.radius >= wheight:
      #          ball.y_vel *= -1
     #       elif ball.y - ball.radius <= 0:
    #            ball.y_vel *= -1

   #         if ball.x_vel < 0:
  #              if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.height:
 #                   if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
#                        ball.x_vel *= -1

          #              middle_y = left_paddle.y + left_paddle.height / 2
         #               difference_in_y = middle_y - ball.y
        #                reduction_factor = (left_paddle.height / 2) / ball.MAX_VEL
       #                 y_vel = difference_in_y / reduction_factor
      #                  ball.y_vel = -1 * y_vel

     #       else:
             #   if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.height:
            #        if ball.x + ball.radius >= right_paddle.x:
           #             ball.x_vel *= -1

          #              middle_y = right_paddle.y + right_paddle.height / 2
         #               difference_in_y = middle_y - ball.y
        #                reduction_factor = (right_paddle.height / 2) / ball.MAX_VEL
       #                 y_vel = difference_in_y / reduction_factor
      #                  ball.y_vel = -1 * y_vel


     #   def handle_paddle_movement(keys, left_paddle, right_paddle):
     #       if keys[pygame.K_w] and left_paddle.y - left_paddle.VEL >= 0:
     #           left_paddle.move(up=True)
     #       if keys[pygame.K_s] and left_paddle.y + left_paddle.VEL + left_paddle.height <= wheight:
     #           left_paddle.move(up=False)

    #        if keys[pygame.K_UP] and right_paddle.y - right_paddle.VEL >= 0:
   #             right_paddle.move(up=True)
  #          if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.VEL + right_paddle.height <= wheight:
 #               right_paddle.move(up=False)

    
        #run = True
        #clock = pygame.time.Clock()

        #left_paddle = player(10, wheight//2 - pheight //
                           # 2, pwidth, pheight)
        #right_paddle = player(wwidth - 10 - pwidth, wheight //
                           # 2 - pheight//2, pwidth, pheight)
        #ball = Ball(wwidth // 2, wheight // 2, ballsize)

        #left_score = 0
        #right_score = 0

        #while run:
            #clock.tick(FPS)
            #draw(screen, [left_paddle, right_paddle], ball, left_score, right_score)

            #for event in pygame.event.get():
                #if event.type == pygame.QUIT:
                  #run = False
                  #break

            #keys = pygame.key.get_pressed()
            #handle_paddle_movement(keys, left_paddle, right_paddle)

            #ball.move()
            #handle_collision(ball, left_paddle, right_paddle)

            #if ball.x < 0:
                #right_score += 1
                #ball.reset()
            #elif ball.x > wwidth:
                #left_score += 1
                #ball.reset()

            #won = False
            #if left_score >= winscore:
                #won = True
                #win_text = "Left Wins!"
            #elif right_score >= winscore:
                #won = True
                #win_text = "Right Wins!"

            #if won:
                #text = SCORE_FONT.render(win_text, 1, white)
                #screen.blit(text, (wwidth//2 - text.get_width() //
                               # 2, wheight//2 - text.get_height()//2))
                #pygame.display.update()
                #pygame.time.delay(5000)
                #ball.reset()
                #left_paddle.reset()
                #right_paddle.reset()
                #left_score = 0
               # right_score = 0

        #pygame.quit()

    


    #single player or two player
    button_light = (170,170,170)
    button_dark = (140,140,140)
    black = (0,0,0)
    background = pygame.image.load("Documents/GitHub/CLPS-0950-Digital-Arcade/pongbackground.png")


    #dimensions of window
    (width, height) = (960, 720)

    #creating the window
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Pong Question Screen')
    screen.blit(background, (0,0))
    pygame.display.flip()

    #text set up 
    textfont = pygame.font.SysFont('Arial',16)
    quittext = textfont.render('Quit' , True , black)
    onetext = textfont.render('One Player' , True , black)
    twotext = textfont.render('Two Players' , True , black)



    running = True
    while running: 
        mouse = pygame.mouse.get_pos()
    #code for making one player button lighter when hovered over it 
        if width/2-280 <= mouse[0] <= width/2-140 and height/2-60 <= mouse[1] <= height/2-20:
            pygame.draw.rect(screen,button_light,[width/2-280,height/2-60,140,40])    
        else:
            pygame.draw.rect(screen,button_dark,[width/2-280,height/2-60,140,40])
    #code for making two player button lighter when hovered over it 
        if width/2+140 <= mouse[0] <= width/2+280 and height/2-60 <= mouse[1] <= height/2-20:
            pygame.draw.rect(screen,button_light,[width/2+140,height/2-60,140,40])    
        else:
            pygame.draw.rect(screen,button_dark,[width/2+140,height/2-60,140,40])
    #code for making quit button lighter when hovered over it 
        if width/2-70 <= mouse[0] <= width/2+70 and height/2+20 <= mouse[1] <= height/2+60:
            pygame.draw.rect(screen,button_light,[width/2-70,height/2+20,140,40])        
        else:
            pygame.draw.rect(screen,button_dark,[width/2-70,height/2+20,140,40])
      
        screen.blit(quittext , (width/2-20,height/2+30))
        screen.blit(onetext , (width/2-250,height/2-50))
        screen.blit(twotext , (width/2+170,height/2-50))
        pygame.display.update()  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if width/2-70 <= mouse[0] <= width/2+70 and height/2+20 <= mouse[1] <= height/2+60:
                    pygame.quit()
                    sys.exit()
            #What happens when the oneplayer button is clicked
                if width/2-280 <= mouse[0] <= width/2-140 and height/2-60 <= mouse[1] <= height/2-20:
                    running = False
                    oneplayer()
            #What happens when the twoplayer button is clicked
                if width/2+140 <= mouse[0] <= width/2+280 and height/2-60 <= mouse[1] <= height/2-20:
                    running = False
                    twoplayer()
                    
                  
        
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if width-280 <= mouse[0] <= width-140 and height-80 <= mouse[1] <= height-40:
                    pygame.quit()
                    sys.exit()

        
if __name__ == "__main__":
	game()