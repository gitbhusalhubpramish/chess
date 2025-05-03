
import os
import pygame
from players import player

# Initialize Pygame with VNC support
os.environ['SDL_VIDEODRIVER'] = 'x11'
pygame.init()

# Set up the display with proper VNC configuration
WINDOW_SIZE = (560, 560)
screen = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)
pygame.display.set_caption("Chess Game")
pygame.display.set_caption("Chess")

def draw_board(WHITE, ROWS, COLS, SQUARE_SIZE, BLACK):
  screen.fill(WHITE)
  for row in range(ROWS):
      for col in range(COLS):
          if (row + col) % 2 != 0:
              pygame.draw.rect(
                  screen, BLACK,
                  (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
              )

# Load chess pieces
player1 = player("white")
wk = pygame.image.load("white player/king.png")
wk = pygame.transform.scale(wk, (100, 100))  # Scale the image
wq = pygame.image.load("white player/queen.png")
wr = pygame.image.load("white player/rook.png")
wb = pygame.image.load("white player/bishop.png")
wn = pygame.image.load("white player/knight.png")
wp = pygame.image.load("white player/pawn.png")
wq = pygame.transform.scale(wq, (100, 100))
wr = pygame.transform.scale(wr, (100, 100))
wb = pygame.transform.scale(wb, (100, 100))
wn = pygame.transform.scale(wn, (100, 100))
wp = pygame.transform.scale(wp, (100, 100))


player2 = player("black")
bk = pygame.image.load("black player/king.png")
bk = pygame.transform.scale(bk, (100, 100))
bq = pygame.image.load("black player/queen.png")
br = pygame.image.load("black player/rook.png")
bb = pygame.image.load("black player/bishop.png")
bn = pygame.image.load("black player/knight.png")
bp = pygame.image.load("black player/pawn.png")
bq = pygame.transform.scale(bq, (100, 100))
br = pygame.transform.scale(br, (100, 100))
bb = pygame.transform.scale(bb, (100, 100))
bn = pygame.transform.scale(bn, (100, 100))
bp = pygame.transform.scale(bp, (100, 100))

def drawpcs():
  screen.blit(wk, (350, 350))
  screen.blit(wq, (250, 350))
  screen.blit(wr, (150, 350))
  screen.blit(wb, (50, 350))
  screen.blit(wn, (450, 350))
  screen.blit(wp, (650, 350))
  screen.blit(bk, (350, 50))
  screen.blit(bq, (250, 50))
  screen.blit(br, (150, 50))
  screen.blit(bb, (50, 50))
  screen.blit(bn, (450, 50))
  screen.blit(bp, (650, 50))

clock = pygame.time.Clock()
running = True

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear screen
    screen.fill((255, 255, 255))
    
    # Draw chess piece (test)
    drawpcs()

  
    # Draw board
    draw_board((255, 255, 255), 8, 8, 70, (0, 0, 0))
    pygame.display.flip()
    
    # Update display
    pygame.display.update()

pygame.quit()
