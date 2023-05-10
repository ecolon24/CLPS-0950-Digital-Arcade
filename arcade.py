import pygame
import sys
from PIL import Image
from io import BytesIO
from os import stat_result
import os.path
import Tetris
import snake
import pong

def main_menu():
    pygame.init()

   
    background_colour = (204,229,255)
    button_light = (170,170,170)
    button_dark = (140,140,140)
    button_dark2 = (153,50,204)
    button_light2 = (186,85,211)
    black = (0,0,0)
    white = (255,255,255)
    arcade_background = pygame.image.load("arcadebackground.jpeg")


    #dimensions of window
    (width, height) = (1200, 800)

    #creating the window
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Digital Aracde')
    screen.blit(arcade_background, (0,0))
    pygame.display.flip()

    #text set up 
    textfont = pygame.font.SysFont('Arial',18)
    quittext = textfont.render('Quit' , True , white)
    tetristext = textfont.render('Tetris' , True , white)
    snaketext = textfont.render('Snake' , True , white)
    pongtext = textfont.render('Pong' , True , white)



    running = True
    while running: 
        mouse = pygame.mouse.get_pos()
    #code for making tetris button lighter when hovered over it 
        if width/2-280 <= mouse[0] <= width/2-140 and height/2-60 <= mouse[1] <= height/2-20:
            pygame.draw.rect(screen,button_light2,[width/2-280,height/2-60,140,40])    
        else:
            pygame.draw.rect(screen,button_dark2,[width/2-280,height/2-60,140,40])
    #code for making snake button lighter when hovered over it 
        if width/2-70 <= mouse[0] <= width/2+70 and height/2-60 <= mouse[1] <= height/2-20:
            pygame.draw.rect(screen,button_light2,[width/2-70,height/2-60,140,40])    
        else:
            pygame.draw.rect(screen,button_dark2,[width/2-70,height/2-60,140,40])
    #code for making space invaders button lighter when hovered over it 
        if width/2+140 <= mouse[0] <= width/2+280 and height/2-60 <= mouse[1] <= height/2-20:
            pygame.draw.rect(screen,button_light2,[width/2+140,height/2-60,140,40])    
        else:
            pygame.draw.rect(screen,button_dark2,[width/2+140,height/2-60,140,40])
    #code for making quit button lighter when hovered over it 
        if width/2-70 <= mouse[0] <= width/2+70 and height/2+20 <= mouse[1] <= height/2+60:
            pygame.draw.rect(screen,button_light2,[width/2-70,height/2+20,140,40])        
        else:
            pygame.draw.rect(screen,button_dark2,[width/2-70,height/2+20,140,40])
      
        screen.blit(quittext , (width/2-20,height/2+30))
        screen.blit(tetristext , (width/2-232,height/2-50))
        screen.blit(snaketext , (width/2-26,height/2-50))
        screen.blit(pongtext , (width/2+190,height/2-50))
        pygame.display.update()  

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
                    Tetris.game() 
            #What happens when the snake button is clicked
                if width/2-70 <= mouse[0] <= width/2+70 and height/2-60 <= mouse[1] <= height/2-20:
                    running = False
                    snake.game()
            #What happens when the space invaders button is clicked
                if width/2+140 <= mouse[0] <= width/2+280 and height/2-60 <= mouse[1] <= height/2-20:
                    running = False
                    pong.game()
                    #space_invaders.space_invaders() 
                  


        
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
	main_menu()
