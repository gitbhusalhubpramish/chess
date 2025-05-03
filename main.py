
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
wk = pygame.transform.scale(wk, (70, 70))  # Scale the image
wq = pygame.image.load("white player/queen.png")
wr = pygame.image.load("white player/rook.png")
wb = pygame.image.load("white player/bishop.png")
wn = pygame.image.load("white player/knight.png")
wp = pygame.image.load("white player/pawn.png")
wq = pygame.transform.scale(wq, (70, 70))
wr = pygame.transform.scale(wr, (70, 70))
wb = pygame.transform.scale(wb, (70, 70))
wn = pygame.transform.scale(wn, (70, 70))
wp = pygame.transform.scale(wp, (70, 70))


player2 = player("black")
bk = pygame.image.load("black player/king.png")
bk = pygame.transform.scale(bk, (70, 70))
bq = pygame.image.load("black player/queen.png")
br = pygame.image.load("black player/rook.png")
bb = pygame.image.load("black player/bishop.png")
bn = pygame.image.load("black player/knight.png")
bp = pygame.image.load("black player/pawn.png")
bq = pygame.transform.scale(bq, (70, 70))
br = pygame.transform.scale(br, (70, 70))
bb = pygame.transform.scale(bb, (70, 70))
bn = pygame.transform.scale(bn, (70, 70))
bp = pygame.transform.scale(bp, (70, 70))

chess_positions = {}

square_size = 70
files = 'abcdefgh'
ranks = '12345678'

for row in range(8):
    for col in range(8):
        square = f"{files[col]}{ranks[7 - row]}"  # a1 at bottom-left
        chess_positions[square] = {
            "x": col * square_size,
            "y": row * square_size
        }


def drawpcs():
    # Draw white pieces (bottom row)
    # screen.blit(wr, (chess_positions[player1.characters.rook.detail[1].position]["x"]), 490))      # a1
    screen.blit(wr, (chess_positions[player1.characters["rook"]["detail"[1]].position]["x"], 490))      # a1
    screen.blit(wn, (70, 490))     # b1
    screen.blit(wb, (140, 490))    # c1
    screen.blit(wq, (210, 490))    # d1
    screen.blit(wk, (280, 490))    # e1
    screen.blit(wb, (350, 490))    # f1
    screen.blit(wn, (420, 490))    # g1
    screen.blit(wr, (490, 490))    # h1

    # Draw black pieces (top row)
    screen.blit(br, (0, 0))        # a8
    screen.blit(bn, (70, 0))       # b8
    screen.blit(bb, (140, 0))      # c8
    screen.blit(bq, (210, 0))      # d8
    screen.blit(bk, (280, 0))      # e8
    screen.blit(bb, (350, 0))      # f8
    screen.blit(bn, (420, 0))      # g8
    screen.blit(br, (490, 0))      # h8

clock = pygame.time.Clock()
running = True

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear screen and draw board first
    draw_board((255, 255, 255), 8, 8, 70, (0, 0, 0))
    
    # Draw pieces on top of board
    drawpcs()
    
    # Update display
    pygame.display.flip()
    
    # Update display
    pygame.display.update()

pygame.quit()
