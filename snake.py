import pygame
import sys

#dimensions of window
(width, height) = (1200, 800)

#creating the window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Digital Aracde')
screen.fill(background_colour)
pygame.display.flip()

