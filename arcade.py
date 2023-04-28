import pygame
import sys

pygame.init()

#I want to get an image for the background of the start screen
# but I'm not sure how to do that
background_colour = (255,255,255)
button_light = (170,170,170)
button_dark = (100,100,100)

#dimensions of window
(width, height) = (1200, 800)

#creating the window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Digital Aracde')
screen.fill(background_colour)
pygame.display.flip()

#text set up 
textfont = pygame.font.SysFont('Arial',18)
quittext = textfont.render('Quit' , True , background_colour)
tetristext = textfont.render('Tetris' , True , background_colour)
snaketext = textfont.render('Snake' , True , background_colour)
spacetext = textfont.render('Space Invaders' , True , background_colour)
  
while True:
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

    #code for making space invaders button lighter when hovered over it 
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
    screen.blit(tetristext , (width/2-232,height/2-50))
    screen.blit(snaketext , (width/2-26,height/2-50))
    screen.blit(spacetext , (width/2+150,height/2-50))
    pygame.display.update()  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if width/2-70 <= mouse[0] <= width/2+70 and height/2+20 <= mouse[1] <= height/2+60:
                pygame.quit()
            #What happens when the tetris button is clicked
            #currently operates same as quit button, as a placeholder
            if width/2-280 <= mouse[0] <= width/2-140 and height/2-60 <= mouse[1] <= height/2-20:
                pygame.quit()
            #What happens when the snake button is clicked
            #currently operates same as quit button, as a placeholder
            if width/2-70 <= mouse[0] <= width/2+70 and height/2-60 <= mouse[1] <= height/2-20:
                pygame.quit()
            #What happens when the space invaders button is clicked
            #currently operates same as quit button, as a placeholder
            if width/2+140 <= mouse[0] <= width/2+280 and height/2-60 <= mouse[1] <= height/2-20:
                pygame.quit()
                  
      
