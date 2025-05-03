
import os
import pygame
from players import player

# Initialize Pygame
pygame.init()

# Set up the display
WINDOW_SIZE = (800, 800)
os.environ['SDL_VIDEODRIVER'] = 'dummy'
screen = pygame.display.set_mode(WINDOW_SIZE, pygame.HIDDEN)
pygame.display.set_caption("Chess")

# Create virtual display
virtual_surface = pygame.Surface(WINDOW_SIZE)

player1 = player("white")
wk = pygame.image.load("white player/king.png")

player2 = player("black")

running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Fill screen with white color
    virtual_surface.fill((255, 255, 255))

    # Draw to virtual surface first
    screen.blit(virtual_surface, (0, 0))

    # Update display
    pygame.display.flip()

pygame.quit()
