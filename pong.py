import pygame
import sys
import time
import turtle
import random
from random import randint
from pygame import mixer
import tryagainscreen
import losescreen

def game():
    pygame.init()
    mixer.init()
    theme_music = 'pongbackgroundmusic.mp3'
    mixer.music.load(theme_music) 
    mixer.music.play(loops=-1)  
    def oneplayer():

        (width, height) = (965, 590)
        pygame.display.update()
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('COUNTDOWN')
        pygame.display.update() 
        backgroundinstructions = pygame.image.load("instructions1.png")
        background3 = pygame.image.load("3.png")
        background2 = pygame.image.load("2.png")
        background1 = pygame.image.load("1.png")

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
        mixer.music.stop()

        #speed = 5
        ballx = 3
        bally = 3
        bouncesound = mixer.music.load("boing2.mp3")
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
                #lost screen here

                losescreen2 = "You Lose!"
                textfont2 = pygame.font.SysFont('Arial',40)
                text = textfont2.render(losescreen2, 1, white)
                mixer.music.stop()
                screen.blit(text, (wwidth//2 - text.get_width() // 2, 180 - text.get_height()//2))
                pygame.display.update()
                time.sleep(3)
                losescreen.losing()



        
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
        backgroundinstructions = pygame.image.load("instructions2.png")
        background3 = pygame.image.load("3.png")
        background2 = pygame.image.load("2.png")
        background1 = pygame.image.load("1.png")


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

        def handle_paddle_movement(keys, left_paddle, right_paddle):
            if keys[pygame.K_w] and left_paddle.y - left_paddle.VEL >= 0:
                left_paddle.move(up=True)
            if keys[pygame.K_s] and left_paddle.y + left_paddle.VEL + left_paddle.height <= wheight:
                left_paddle.move(up=False)
            if keys[pygame.K_UP] and right_paddle.y - right_paddle.VEL >= 0:
                right_paddle.move(up=True)
            if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.VEL + right_paddle.height <= wheight:
                right_paddle.move(up=False)


        BALL_VELOCITY = [4,4]
        player1_score = 0
        player2_score = 0
        font = pygame.font.Font("freesansbold.ttf", 50)

        #def endscreen():
        won = False
            

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
            keys = pygame.key.get_pressed()
            handle_paddle_movement(keys, player1, player2)

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
                if player2_score > 5:
                    BALL_VELOCITY = [0,0]
                    won = True
                    winscreen = "Right Player Wins!!"

            elif ball.off_screen_right():
                player1_score += 1
                ball = Ball(wwidth // 2, wheight // 2)
                BALL_VELOCITY = [random.choice([-4, 4]), random.choice([-4, 4])]
                if player1_score >5:
                    BALL_VELOCITY = [0,0]
                    won = True
                    winscreen = "Left Player Wins!!"

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


        
            if won:
                playagain = False
                textfont1 = pygame.font.SysFont('Arial',40)
                text = textfont1.render(winscreen, 1, white)
                screen.blit(text, (wwidth//2 - text.get_width() // 2, 180 - text.get_height()//2))
                pygame.display.update()
                player1.reset()
                player2.reset()
                time.sleep(3)
                tryagainscreen.losing()


            #play again? 
                #playagaintext = textfont.render('Play Again?' , True , black)
                #quittext2 = textfont.render('Quit' , True , black)

                
            #code for making play again button lighter when hovered over it 
                #if width/2-280 <= mouse[0] <= width/2-140 and height/2-60 <= mouse[1] <= height/2-20:
                    #pygame.draw.rect(screen,button_light,[width/2-280,height/2-60,140,40])    
                #else:
                    #pygame.draw.rect(screen,button_dark,[width/2-280,height/2-60,140,40])
            #code for making quit button lighter when hovered over it 
                #if width/2+140 <= mouse[0] <= width/2+280 and height/2-60 <= mouse[1] <= height/2-20:
                    #pygame.draw.rect(screen,button_light,[width/2+140,height/2-60,140,40])    
                #else:
                    #pygame.draw.rect(screen,button_dark,[width/2+140,height/2-60,140,40])


                #screen.blit(playagaintext , (width/2-250,height/2-50))
                #screen.blit(quittext2 , (width/2+170,height/2-50))
                #pygame.display.update()

                #if event.type == pygame.MOUSEBUTTONDOWN:
            #What happens when the oneplayer button is clicked
                    #if width/2-280 <= mouse[0] <= width/2-140 and height/2-60 <= mouse[1] <= height/2-20:
                       # BALL_VELOCITY =[4,4]
                       # player1_score = 0
                       # player2_score = 0
                       # playagain = True
            #What happens when the twoplayer button is clicked
                   # if width/2+140 <= mouse[0] <= width/2+280 and height/2-60 <= mouse[1] <= height/2-20:
                    #    pygame.quit()
                    #    sys.ext()
                
            

    # Update the display
            pygame.display.update()

# Clean up the Pygame window
        pygame.quit()


    
    #single player or two player
    button_light = (170,170,170)
    button_dark = (140,140,140)
    black = (0,0,0)
    background = pygame.image.load("pongbackground.png")


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