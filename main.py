import os
import pygame
from players import player
import platform
from moves import knight_moves, king_moves, rook_moves, bishop_moves, queen_moves, pawn_moves

if platform.system() == "Linux":
    os.environ["SDL_VIDEODRIVER"] = "x11"
pygame.init()

WINDOW_SIZE = (560, 560)
screen = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)
pygame.display.set_caption("Chess")

def draw_board(WHITE, ROWS, COLS, SQUARE_SIZE, BROWN):
    screen.fill(WHITE)
    for row in range(ROWS):
        for col in range(COLS):
            if (row + col) % 2 != 0:
                pygame.draw.rect(
                    screen, BROWN,
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
        wp[i] = pygame.transform.smoothscale(original_pcs["P"][i], (siz, siz))
    for i in range(2):
        wr[i] = pygame.transform.smoothscale(original_pcs["R"][i], (siz, siz))
        wb[i] = pygame.transform.smoothscale(original_pcs["B"][i], (siz, siz))
        wn[i] = pygame.transform.smoothscale(original_pcs["N"][i], (siz, siz))
    wq[0] = pygame.transform.smoothscale(original_pcs["Q"][0], (siz, siz))
    wk[0] = pygame.transform.smoothscale(original_pcs["K"][0], (siz, siz))


def blkrsz(siz):
    for i in range(8):
        bp[i] = pygame.transform.smoothscale(original_pcs["p"][i], (siz, siz))
    for i in range(2):
        br[i] = pygame.transform.smoothscale(original_pcs["r"][i], (siz, siz))
        bb[i] = pygame.transform.smoothscale(original_pcs["b"][i], (siz, siz))
        bn[i] = pygame.transform.smoothscale(original_pcs["n"][i], (siz, siz))
    bq[0] = pygame.transform.smoothscale(original_pcs["q"][0], (siz, siz))
    bk[0] = pygame.transform.smoothscale(original_pcs["k"][0], (siz, siz))

def rsz(siz, psc, idx):
    pcs[psc][idx] = pygame.transform.smoothscale(original_pcs[psc][idx], (siz, siz))

def dcrzall():
    for i in range(8):
        wp[i] = pygame.transform.smoothscale(original_pcs["P"][i], (65, 65))
        bp[i] = pygame.transform.smoothscale(original_pcs["p"][i], (65, 65))
    for i in range(2):
        wr[i] = pygame.transform.smoothscale(original_pcs["R"][i], (65, 65))
        wb[i] = pygame.transform.smoothscale(original_pcs["B"][i], (65, 65))
        wn[i] = pygame.transform.smoothscale(original_pcs["N"][i], (65, 65))
        br[i] = pygame.transform.smoothscale(original_pcs["r"][i], (65, 65))
        bb[i] = pygame.transform.smoothscale(original_pcs["b"][i], (65, 65))
        bn[i] = pygame.transform.smoothscale(original_pcs["n"][i], (65, 65))
    wq[0] = pygame.transform.smoothscale(original_pcs["Q"][0], (65, 65))
    wk[0] = pygame.transform.smoothscale(original_pcs["K"][0], (65, 65))
    bq[0] = pygame.transform.smoothscale(original_pcs["q"][0], (65, 65))
    bk[0] = pygame.transform.smoothscale(original_pcs["k"][0], (65, 65))


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
packedsqr = []
def ckcpcn():
    for player_obj in [player1, player2]:
        for p_type, p_data in player_obj.characters.items():
            for idx, piece in enumerate(p_data["detail"]):
                if piece["alive"]:
                    packedsqr.append(piece["position"])

piece_position_map = {}
pcs = {
    "K": wk, "Q": wq, "R": wr, "B": wb, "N": wn, "P": wp,
    "k": bk, "q": bq, "r": br, "b": bb, "n": bn, "p": bp
}
pic = {"K": "king", "Q": "queen", "R": "rook", "B": "bishop", "N": "knight", "P": "pawn"}

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

def get_moves(char, pos, color):
    if char.upper() == 'K':
        return king_moves(pos)
    elif char.upper() == 'Q':
        return queen_moves(pos)
    elif char.upper() == 'R':
        return rook_moves(pos)
    elif char.upper() == 'B':
        return bishop_moves(pos)
    elif char.upper() == 'N':
        return knight_moves(pos)
    elif char.upper() == 'P':
        return pawn_moves(pos, color)
    return []

clock = pygame.time.Clock()
running = True
Selected = None
wt = True

while running:
    for event in pygame.event.get():
        nextmv = None
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            col = mouse_x // square_size
            row = mouse_y // square_size
            file = chr(ord('a') + col)
            rank = str(8 - row)
            square = file + rank

            if Selected is not None:
                ckcpcn()
                nextmv = square if (square not in packedsqr and square in get_moves(Selected[0], player1.characters[pic[Selected[0]]]["detail"][Selected[1]]["position"] if wt else player2.characters[pic[Selected[0]]]["detail"][Selected[1]]["position"], "white" if wt else "black")) else None
            print(nextmv)
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
            rsz(85, Selected[0], Selected[1])
        elif Selected is not None and not wt and Selected[0].islower():
            dcrzall()
            rsz(85, Selected[0], Selected[1])

    

    draw_board((255, 255, 255), 8, 8, 70, (150, 75, 0))
    drawpcs()
    # if Selected is not None:
    #     pygame.draw.circle(screen, (210,249,83), (200,200), 10)
    pygame.display.flip()
    pygame.display.update()

pygame.quit()
