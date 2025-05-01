
import os
import pygame
from players import player

# Initialize Pygame
pygame.init()

# Set up the display
WINDOW_SIZE = (800, 800)
os.environ['SDL_VIDEODRIVER'] = 'x11'
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Chess")

screen.fill((255, 255, 255))

pygame.quit()
