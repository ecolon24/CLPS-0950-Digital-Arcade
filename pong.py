import pygame
import sys
def game():
    pygame.init()

    
    button_light = (170,170,170)
    button_dark = (140,140,140)
    background_colour = (204,229,255)
    (width, height) = (1200, 800)
    black = (0,0,0)

        #creating the window
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('One or Two Players Pong')
    screen.fill(background_colour)
    pygame.display.flip()

        #text set up 
    textfont = pygame.font.SysFont('Arial',18)
    onetext = textfont.render('One Player' , True , black)
    twotext = textfont.render('Two Player' , True , black)
    
    running = True
    while running: 
        mouse = pygame.mouse.get_pos()
    #code for making tetris button lighter when hovered over it 
        if width/2-280 <= mouse[0] <= width/2-140 and height/2-60 <= mouse[1] <= height/2-20:
            pygame.draw.rect(screen,button_light,[width/2-280,height/2-60,140,40])    
        else:
            pygame.draw.rect(screen,button_dark,[width/2-280,height/2-60,140,40])
    #code for making snake button lighter when hovered over it 
        if width/2-70 <= mouse[0] <= width/2+70 and height/2-60 <= mouse[1] <= height/2-20:
            pygame.draw.rect(screen,button_light,[width/2-70,height/2-60,140,40])    
        else:
            pygame.draw.rect(screen,button_dark,[width/2-70,height/2-60,140,40])

    screen.blit(onetext , (width/2-20,height/2+30))
    screen.blit(twotext , (width/2-232,height/2-50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if width/2-70 <= mouse[0] <= width/2+70 and height/2+20 <= mouse[1] <= height/2+60:
                pygame.quit()
                sys.exit()
            #What happens when the tetris button is clicked
            if width/2-280 <= mouse[0] <= width/2-140 and height/2-60 <= mouse[1] <= height/2-20:
                running = False
                twoplayer()
            #What happens when the snake button is clicked
            if width/2-70 <= mouse[0] <= width/2+70 and height/2-60 <= mouse[1] <= height/2-20:
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








    def twoplayer():
        wwidth, wheight = 700, 500
        WIN = pygame.display.set_mode((wwidth, wheight))
        pygame.display.set_caption("Pong")

        FPS = 60

        WHITE = (255, 255, 255)
        purpleblue = (123,104,238)
        BLACK = (0, 0, 0)

        PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
        BALL_RADIUS = 7

        SCORE_FONT = pygame.font.SysFont("comicsans", 50)
        WINNING_SCORE = 10


        class Paddle:
            COLOR = purpleblue
            VEL = 4

            def __init__(self, x, y, width, height):
                self.x = self.original_x = x
                self.y = self.original_y = y
                self.width = width
                self.height = height

            def draw(self, win):
                pygame.draw.rect(
                    win, self.COLOR, (self.x, self.y, self.width, self.height))

            def move(self, up=True):
                if up:
                    self.y -= self.VEL
                else:
                    self.y += self.VEL

            def reset(self):
                self.x = self.original_x
                self.y = self.original_y


        class Ball:
            MAX_VEL = 5
            COLOR = WHITE

            def __init__(self, x, y, radius):
                self.x = self.original_x = x
                self.y = self.original_y = y
                self.radius = radius
                self.x_vel = self.MAX_VEL
                self.y_vel = 0

            def draw(self, win):
                pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.radius)

            def move(self):
                self.x += self.x_vel
                self.y += self.y_vel

            def reset(self):
                self.x = self.original_x
                self.y = self.original_y
                self.y_vel = 0
                self.x_vel *= -1


        def draw(win, paddles, ball, left_score, right_score):
            win.fill(BLACK)

            left_score_text = SCORE_FONT.render(f"{left_score}", 1, WHITE)
            right_score_text = SCORE_FONT.render(f"{right_score}", 1, WHITE)
            win.blit(left_score_text, (wwidth//4 - left_score_text.get_width()//2, 20))
            win.blit(right_score_text, (wwidth * (3/4) -
                                        right_score_text.get_width()//2, 20))

            for paddle in paddles:
                paddle.draw(win)

            for i in range(10, wheight, wheight//20):
                if i % 2 == 1:
                    continue
                pygame.draw.rect(win, WHITE, (wwidth//2 - 5, i, 10, wheight//20))

            ball.draw(win)
            pygame.display.update()


        def handle_collision(ball, left_paddle, right_paddle):
            if ball.y + ball.radius >= wheight:
                ball.y_vel *= -1
            elif ball.y - ball.radius <= 0:
                ball.y_vel *= -1

            if ball.x_vel < 0:
                if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.height:
                    if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                        ball.x_vel *= -1

                        middle_y = left_paddle.y + left_paddle.height / 2
                        difference_in_y = middle_y - ball.y
                        reduction_factor = (left_paddle.height / 2) / ball.MAX_VEL
                        y_vel = difference_in_y / reduction_factor
                        ball.y_vel = -1 * y_vel

            else:
                if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.height:
                    if ball.x + ball.radius >= right_paddle.x:
                        ball.x_vel *= -1

                        middle_y = right_paddle.y + right_paddle.height / 2
                        difference_in_y = middle_y - ball.y
                        reduction_factor = (right_paddle.height / 2) / ball.MAX_VEL
                        y_vel = difference_in_y / reduction_factor
                        ball.y_vel = -1 * y_vel


        def handle_paddle_movement(keys, left_paddle, right_paddle):
            if keys[pygame.K_w] and left_paddle.y - left_paddle.VEL >= 0:
                left_paddle.move(up=True)
            if keys[pygame.K_s] and left_paddle.y + left_paddle.VEL + left_paddle.height <= wheight:
                left_paddle.move(up=False)

            if keys[pygame.K_UP] and right_paddle.y - right_paddle.VEL >= 0:
                right_paddle.move(up=True)
            if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.VEL + right_paddle.height <= wheight:
                right_paddle.move(up=False)

    
        run = True
        clock = pygame.time.Clock()

        left_paddle = Paddle(10, wheight//2 - PADDLE_HEIGHT //
                            2, PADDLE_WIDTH, PADDLE_HEIGHT)
        right_paddle = Paddle(wwidth - 10 - PADDLE_WIDTH, wheight //
                            2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
        ball = Ball(wwidth // 2, wheight // 2, BALL_RADIUS)

        left_score = 0
        right_score = 0

        while run:
            clock.tick(FPS)
            draw(WIN, [left_paddle, right_paddle], ball, left_score, right_score)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  run = False
                  break

            keys = pygame.key.get_pressed()
            handle_paddle_movement(keys, left_paddle, right_paddle)

            ball.move()
            handle_collision(ball, left_paddle, right_paddle)

            if ball.x < 0:
                right_score += 1
                ball.reset()
            elif ball.x > wwidth:
                left_score += 1
                ball.reset()

            won = False
            if left_score >= WINNING_SCORE:
                won = True
                win_text = "Left Player Won!"
            elif right_score >= WINNING_SCORE:
                won = True
                win_text = "Right Player Won!"

            if won:
                text = SCORE_FONT.render(win_text, 1, WHITE)
                WIN.blit(text, (wwidth//2 - text.get_width() //
                                2, wheight//2 - text.get_height()//2))
                pygame.display.update()
                pygame.time.delay(5000)
                ball.reset()
                left_paddle.reset()
                right_paddle.reset()
                left_score = 0
                right_score = 0

        pygame.quit()
        
if __name__ == "__main__":
	game()