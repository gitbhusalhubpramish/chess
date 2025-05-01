
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

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill screen with white color
    screen.fill((255, 255, 255))
    
    # Update display
    pygame.display.flip()

# Quit pygame
pygame.quit()
