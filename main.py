import os
import pygame
from players import player
import platform

# Initialize Pygame with VNC support
# Set SDL_VIDEODRIVER to x11 only on Linux
if platform.system() == "Linux":
    os.environ["SDL_VIDEODRIVER"] = "x11"
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
wk = [pygame.image.load("white player/king.png") for _ in range(player1.characters["king"]["no"])]
wk = [pygame.transform.scale(wk, (70, 70)) for wk in wk]
wq = [pygame.image.load("white player/queen.png") for _ in range(player1.characters["queen"]["no"])]
wr = [pygame.image.load("white player/rook.png") for _ in range(player1.characters["rook"]["no"])]
wb = [pygame.image.load("white player/bishop.png") for _ in range(player1.characters["bishop"]["no"])]
wn = [pygame.image.load("white player/knight.png") for _ in range(player1.characters["knight"]["no"])]
wp = [pygame.image.load("white player/pawn.png") for _ in range(player1.characters["pawn"]["no"])]
wq = [pygame.transform.scale(wq, (70, 70)) for wq in wq]
wr = [pygame.transform.scale(wr, (70, 70)) for wr in wr]
wb = [pygame.transform.scale(wb, (70, 70)) for wb in wb]
wn = [pygame.transform.scale(wn, (70, 70)) for wn in wn]
wp = [pygame.transform.scale(wp, (70, 70)) for wp in wp]


player2 = player("black")
bk = [pygame.image.load("black player/king.png") for _ in range(player2.characters["king"]["no"])]
bk = [pygame.transform.scale(bk, (70, 70)) for bk in bk]
bq = [pygame.image.load("black player/queen.png") for _ in range(player2.characters["queen"]["no"])]
br = [pygame.image.load("black player/rook.png") for _ in range(player2.characters["rook"]["no"])]
bb = [pygame.image.load("black player/bishop.png") for _ in range(player2.characters["bishop"]["no"])]
bn = [pygame.image.load("black player/knight.png") for _ in range(player2.characters["knight"]["no"])]
bp = [pygame.image.load("black player/pawn.png") for _ in range(player2.characters["pawn"]["no"])]
bq = [pygame.transform.scale(bq, (70, 70)) for bq in bq]
br = [pygame.transform.scale(br, (70, 70)) for br in br]
bb = [pygame.transform.scale(bb, (70, 70)) for bb in bb]
bn = [pygame.transform.scale(bn, (70, 70)) for bn in bn]
bp = [pygame.transform.scale(bp, (70, 70)) for bp in bp]

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
    # Dictionary mapping piece types to their images
    white_pieces = {"king": wk, "queen": wq, "rook": wr, "bishop": wb, "knight": wn, "pawn": wp}
    black_pieces = {"king": bk, "queen": bq, "rook": br, "bishop": bb, "knight": bn, "pawn": bp}
    
    # Draw pieces for both players
    for player, pieces in [(player1, white_pieces), (player2, black_pieces)]:
        for piece_type, piece_data in player.characters.items():
            for piece in piece_data["detail"]:
                if piece["alive"]:
                    pos = piece["position"]
                    x = chess_positions[pos]["x"]
                    y = chess_positions[pos]["y"]
                    screen.blit(pieces[piece_type], (x, y))

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
