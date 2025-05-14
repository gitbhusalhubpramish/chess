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

piece_position_map = {}
def drawpcs():
    piece_position_map.clear()
    piece_images = {
        'K': wk[0], 'Q': wq[0], 'R': wr[0], 'B': wb[0], 'N': wn[0], 'P': wp[0],
        'k': bk[0], 'q': bq[0], 'r': br[0], 'b': bb[0], 'n': bn[0], 'p': bp[0]
    }
    piece_map = {'king': 'K', 'queen': 'Q', 'rook': 'R', 'bishop': 'B', 'knight': 'N', 'pawn': 'P'}

    for player_obj in [player1, player2]:
        for p_type, p_data in player_obj.characters.items():
            char = piece_map[p_type]
            if player_obj.color == "black":
                char = char.lower()
            for piece in p_data["detail"]:
                if piece["alive"]:
                    pos = piece["position"]
                    col = ord(pos[0]) - ord('a')
                    row = 8 - int(pos[1])
                    x, y = col * square_size, row * square_size
                    screen.blit(piece_images[char], (x, y))
                    piece_position_map[pos] = char


clock = pygame.time.Clock()
running = True
Selected = None
# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            col = mouse_x // square_size
            row = mouse_y // square_size
            file = chr(ord('a') + col)
            rank = str(8 - row)
            square = file + rank

            if square in piece_position_map:
                Selected= f"{piece_position_map[square]}"
            else:
                Selected= None
        print(Selected)
    
    # Clear screen and draw board first
    draw_board((255, 255, 255), 8, 8, 70, (0, 0, 0))
    
    # Draw pieces on top of board
    drawpcs()
    
    # Update display
    pygame.display.flip()
    
    # Update display
    pygame.display.update()

pygame.quit()
