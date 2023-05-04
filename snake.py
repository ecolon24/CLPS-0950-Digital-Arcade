import pygame
import sys
pygame.init()

#dimensions of window
(width, height) = (1200, 800)
background_colour = (204,229,255)
button_light = (170,170,170)
button_dark = (140,140,140)
black = (0,0,0)

textfont = pygame.font.SysFont('Arial',18)
quittext = textfont.render('Quit' , True , black)

square_size = 50
square_x = width // 2 - square_size // 2
square_y = height // 2 - square_size // 2
square_color = (255, 0, 0)


#creating the window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Digital Aracde')
screen.fill(background_colour)
pygame.display.flip()


def snake():
    running = True
    while running: 
        mouse = pygame.mouse.get_pos()
        if width-180 <= mouse[0] <= width-40 and height-80 <= mouse[1] <= height-40:
            pygame.draw.rect(screen,button_light,[width-180,height-80,140,40])    
        else:
            pygame.draw.rect(screen,button_dark,[width-180,height-80,140,40])
        screen.blit(quittext , (width-130,height-70))
        pygame.display.update() 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if width-280 <= mouse[0] <= width-140 and height-80 <= mouse[1] <= height-40:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    square_x -= 5
                elif event.key == pygame.K_RIGHT:
                    square_x += 5
                elif event.key == pygame.K_UP:
                    square_y -= 5
                elif event.key == pygame.K_DOWN:
                    square_y += 5

        pygame.draw.rect(screen, square_color, (square_x, square_y, square_size, square_size))
        pygame.display.flip()


snake()
