import pygame
import sys
import arcade
pygame.init()
from pygame import mixer
mixer.init()

def losing():
    
    losing = 'gameover.wav'
    mixer.music.load(losing) 
    mixer.music.play()  
    (width, height) = (1200, 800)
    background_colour = (204,229,255)
    button_light = (170,170,170)
    button_dark = (140,140,140)
    black = (0,0,0)
    white = (255,255,255) 
    red = (255,0,0)

    #creating the screen
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Digital Aracde')
    screen.fill(background_colour)
    pygame.display.flip()

    #initialising the text
    textfont = pygame.font.SysFont('Arial',18)
    bigfont = pygame.font.SysFont('Arial',30)
    quittext = textfont.render('Quit' , True , black)
    losetext = bigfont.render('You Lost!', True , black)
    mainmenutext = textfont.render('Main Menu' , True , black)


    running = True
    screen.fill(background_colour)
    while running == True:
        mouse = pygame.mouse.get_pos()
        screen.blit(losetext , (width/2-65,height/4))
        
        #hovering over them changes the colours of the buttons
        if width/2-70 <= mouse[0] <= width/2+70 and height/2-60 <= mouse[1] <= height/2-20:
            pygame.draw.rect(screen,button_light,[width/2-70,height/2-60,140,40])    
        else:
            pygame.draw.rect(screen,button_dark,[width/2-70,height/2-60,140,40])
        
        if width/2-70 <= mouse[0] <= width/2+70 and height/2+20 <= mouse[1] <= height/2+60:
            pygame.draw.rect(screen,button_light,[width/2-70,height/2+20,140,40])        
        else:
            pygame.draw.rect(screen,button_dark,[width/2-70,height/2+20,140,40])

        #button functionality 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if width/2-70 <= mouse[0] <= width/2+70 and height/2+20 <= mouse[1] <= height/2+60:
                    pygame.quit()
                    sys.exit()
                if width/2-70 <= mouse[0] <= width/2+70 and height/2-60 <= mouse[1] <= height/2-20:
                    running = False
                    arcade.main_menu()
       
        screen.blit(quittext , (width/2-20,height/2+30))
        screen.blit(mainmenutext , (width/2-42,height/2-50))

        pygame.display.update()


if __name__ == "__main__":
	losing()
