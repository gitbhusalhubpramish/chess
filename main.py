import os
import pygame
from players import player
import platform

if platform.system() == "Linux":
    os.environ["SDL_VIDEODRIVER"] = "x11"
pygame.init()

WINDOW_SIZE = (560, 560)
screen = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)
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
player1 = player("white")
wk = [pygame.image.load("white player/king.png") for _ in range(player1.characters["king"]["no"])]
wq = [pygame.image.load("white player/queen.png") for _ in range(player1.characters["queen"]["no"])]
wr = [pygame.image.load("white player/rook.png") for _ in range(player1.characters["rook"]["no"])]
wb = [pygame.image.load("white player/bishop.png") for _ in range(player1.characters["bishop"]["no"])]
wn = [pygame.image.load("white player/knight.png") for _ in range(player1.characters["knight"]["no"])]
wp = [pygame.image.load("white player/pawn.png") for _ in range(player1.characters["pawn"]["no"])]

player2 = player("black")
bk = [pygame.image.load("black player/king.png") for _ in range(player2.characters["king"]["no"])]
bq = [pygame.image.load("black player/queen.png") for _ in range(player2.characters["queen"]["no"])]
br = [pygame.image.load("black player/rook.png") for _ in range(player2.characters["rook"]["no"])]
bb = [pygame.image.load("black player/bishop.png") for _ in range(player2.characters["bishop"]["no"])]
bn = [pygame.image.load("black player/knight.png") for _ in range(player2.characters["knight"]["no"])]
bp = [pygame.image.load("black player/pawn.png") for _ in range(player2.characters["pawn"]["no"])]

original_pcs = {
    "K": [pygame.image.load("white player/king.png") for _ in range(player1.characters["king"]["no"])],
    "Q": [pygame.image.load("white player/queen.png") for _ in range(player1.characters["queen"]["no"])],
    "R": [pygame.image.load("white player/rook.png") for _ in range(player1.characters["rook"]["no"])],
    "B": [pygame.image.load("white player/bishop.png") for _ in range(player1.characters["bishop"]["no"])],
    "N": [pygame.image.load("white player/knight.png") for _ in range(player1.characters["knight"]["no"])],
    "P": [pygame.image.load("white player/pawn.png") for _ in range(player1.characters["pawn"]["no"])],
    "k": [pygame.image.load("black player/king.png") for _ in range(player2.characters["king"]["no"])],
    "q": [pygame.image.load("black player/queen.png") for _ in range(player2.characters["queen"]["no"])],
    "r": [pygame.image.load("black player/rook.png") for _ in range(player2.characters["rook"]["no"])],
    "b": [pygame.image.load("black player/bishop.png") for _ in range(player2.characters["bishop"]["no"])],
    "n": [pygame.image.load("black player/knight.png") for _ in range(player2.characters["knight"]["no"])],
    "p": [pygame.image.load("black player/pawn.png") for _ in range(player2.characters["pawn"]["no"])]
}

def whtrsz(siz):
    for i in range(8):
        wp[i] = pygame.transform.scale(wp[i], (siz, siz))
    for i in range(2):
        wr[i] = pygame.transform.scale(wr[i], (siz, siz))
        wb[i] = pygame.transform.scale(wb[i], (siz, siz))
        wn[i] = pygame.transform.scale(wn[i], (siz, siz))
    wq[0] = pygame.transform.scale(wq[0], (siz, siz))
    wk[0] = pygame.transform.scale(wk[0], (siz, siz))

def blkrsz(siz):
    for i in range(8):
        bp[i] = pygame.transform.scale(bp[i], (siz, siz))
    for i in range(2):
        br[i] = pygame.transform.scale(br[i], (siz, siz))
        bb[i] = pygame.transform.scale(bb[i], (siz, siz))
        bn[i] = pygame.transform.scale(bn[i], (siz, siz))
    bq[0] = pygame.transform.scale(bq[0], (siz, siz))
    bk[0] = pygame.transform.scale(bk[0], (siz, siz))

def rsz(siz, psc, idx):
    pcs[psc][idx] = pygame.transform.smoothscale(original_pcs[psc][idx], (siz, siz))

def dcrzall():
    for i in range(8):
        wp[i] = pygame.transform.scale(wp[i], (70, 70))
        bp[i] = pygame.transform.scale(bp[i], (70, 70))
    for i in range(2):
        wr[i] = pygame.transform.scale(wr[i], (70, 70))
        wb[i] = pygame.transform.scale(wb[i], (70, 70))
        wn[i] = pygame.transform.scale(wn[i], (70, 70))
        br[i] = pygame.transform.scale(br[i], (70, 70))
        bb[i] = pygame.transform.scale(bb[i], (70, 70))
        bn[i] = pygame.transform.scale(bn[i], (70, 70))
    wq[0] = pygame.transform.scale(wq[0], (70, 70))
    wk[0] = pygame.transform.scale(wk[0], (70, 70))
    bq[0] = pygame.transform.scale(bq[0], (70, 70))
    bk[0] = pygame.transform.scale(bk[0], (70, 70))


whtrsz(70)
blkrsz(70)

square_size = 70
files = 'abcdefgh'
ranks = '12345678'
chess_positions = {
    f"{files[col]}{ranks[7 - row]}": {
        "x": col * square_size,
        "y": row * square_size
    }
    for row in range(8) for col in range(8)
}

piece_position_map = {}
pcs = {
    "K": wk, "Q": wq, "R": wr, "B": wb, "N": wn, "P": wp,
    "k": bk, "q": bq, "r": br, "b": bb, "n": bn, "p": bp
}

def drawpcs():
    piece_position_map.clear()
    piece_map = {'king': 'K', 'queen': 'Q', 'rook': 'R', 'bishop': 'B', 'knight': 'N', 'pawn': 'P'}

    for player_obj in [player1, player2]:
        for p_type, p_data in player_obj.characters.items():
            char = piece_map[p_type]
            if player_obj.color == "black":
                char = char.lower()
            for idx, piece in enumerate(p_data["detail"]):
                if piece["alive"]:
                    pos = piece["position"]
                    col = ord(pos[0]) - ord('a')
                    row = 8 - int(pos[1])
                    x, y = col * square_size, row * square_size
                    screen.blit(pcs[char][idx], (x, y))
                    piece_position_map[pos] = (char, idx)

clock = pygame.time.Clock()
running = True
Selected = None
wt = True

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
                Selected = piece_position_map[square]
            else:
                Selected = None

        if wt and Selected is None:
            whtrsz(75)
            blkrsz(65)
        elif not wt and Selected is None:
            whtrsz(65)
            blkrsz(75)
        elif Selected is not None and wt and Selected[0].isupper():
            dcrzall()
            rsz(90, Selected[0], Selected[1])

    draw_board((255, 255, 255), 8, 8, 70, (0, 0, 0))
    drawpcs()
    pygame.display.flip()
    pygame.display.update()

pygame.quit()
