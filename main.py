
import os
import pygame
from players import player

# Initialize Pygame
pygame.init()

# Set up the display
WINDOW_SIZE = (800, 800)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Chess")

# Load chess pieces
player1 = player("white")
wk = pygame.image.load("white player/king.png")
wk = pygame.transform.scale(wk, (100, 100))  # Scale the image

player2 = player("black")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear screen
    screen.fill((255, 255, 255))
    
    # Draw chess piece (test)
    screen.blit(wk, (350, 350))
    
    # Update display
    pygame.display.update()

pygame.quit()
