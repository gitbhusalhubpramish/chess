import os
import pygame
from players import player
import platform
from moves import knight_moves, king_moves, rook_moves, bishop_moves, queen_moves, pawn_moves, coord_to_pos, pos_to_coord

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

wk = []
wq = []
wr = []
wb = []
wn = []
wp = []

player1 = player("white", wk, wq, wr, wb, wn, wp)
wk = [pygame.image.load("white player/king.png") for _ in range(player1.characters["king"]["no"])]
wq = [pygame.image.load("white player/queen.png") for _ in range(player1.characters["queen"]["no"])]
wr = [pygame.image.load("white player/rook.png") for _ in range(player1.characters["rook"]["no"])]
wb = [pygame.image.load("white player/bishop.png") for _ in range(player1.characters["bishop"]["no"])]
wn = [pygame.image.load("white player/knight.png") for _ in range(player1.characters["knight"]["no"])]
wp = [pygame.image.load("white player/pawn.png") for _ in range(player1.characters["pawn"]["no"])]
player1.charactersdata["king"] = wk
player1.charactersdata["queen"] = wq
player1.charactersdata["rook"] = wr
player1.charactersdata["bishop"] = wb
player1.charactersdata["knight"] = wn
player1.charactersdata["pawn"] = wp

bk = []
bq = []
br = []
bb = []
bn = []
bp = []


player2 = player("black", bk, bq, br, bb, bn, bp)
bk = [pygame.image.load("black player/king.png") for _ in range(player2.characters["king"]["no"])]
bq = [pygame.image.load("black player/queen.png") for _ in range(player2.characters["queen"]["no"])]
br = [pygame.image.load("black player/rook.png") for _ in range(player2.characters["rook"]["no"])]
bb = [pygame.image.load("black player/bishop.png") for _ in range(player2.characters["bishop"]["no"])]
bn = [pygame.image.load("black player/knight.png") for _ in range(player2.characters["knight"]["no"])]
bp = [pygame.image.load("black player/pawn.png") for _ in range(player2.characters["pawn"]["no"])]

player2.charactersdata["king"] = bk
player2.charactersdata["queen"] = bq
player2.charactersdata["rook"] = br
player2.charactersdata["bishop"] = bb
player2.charactersdata["knight"] = bn
player2.charactersdata["pawn"] = bp


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
        player1.charactersdata["pawn"][i] = pygame.transform.smoothscale(original_pcs["P"][i], (siz, siz))
    for i in range(2):
        player1.charactersdata["rook"][i] = pygame.transform.smoothscale(original_pcs["R"][i], (siz, siz))
        player1.charactersdata["bishop"][i] = pygame.transform.smoothscale(original_pcs["B"][i], (siz, siz))
        player1.charactersdata["knight"][i] = pygame.transform.smoothscale(original_pcs["N"][i], (siz, siz))
    player1.charactersdata["queen"][0] = pygame.transform.smoothscale(original_pcs["Q"][0], (siz, siz))
    player1.charactersdata["king"][0] = pygame.transform.smoothscale(original_pcs["K"][0], (siz, siz))


def blkrsz(siz):
    for i in range(8):
        player2.charactersdata["pawn"][i] = pygame.transform.smoothscale(original_pcs["p"][i], (siz, siz))
    for i in range(2):
        player2.charactersdata["rook"][i] = pygame.transform.smoothscale(original_pcs["r"][i], (siz, siz))
        player2.charactersdata["bishop"][i] = pygame.transform.smoothscale(original_pcs["b"][i], (siz, siz))
        player2.charactersdata["knight"][i] = pygame.transform.smoothscale(original_pcs["n"][i], (siz, siz))
    player2.charactersdata["queen"][0] = pygame.transform.smoothscale(original_pcs["q"][0], (siz, siz))
    player2.charactersdata["king"][0] = pygame.transform.smoothscale(original_pcs["k"][0], (siz, siz))

def rsz(siz, psc, idx):
    pcs[psc][idx] = pygame.transform.smoothscale(original_pcs[psc][idx], (siz, siz))

def dcrzall():
    for i in range(8):
        player1.charactersdata["pawn"][i] = pygame.transform.smoothscale(original_pcs["P"][i], (65, 65))
        player2.charactersdata["pawn"][i] = pygame.transform.smoothscale(original_pcs["p"][i], (65, 65))
    for i in range(2):
        player1.charactersdata["rook"][i] = pygame.transform.smoothscale(original_pcs["R"][i], (65, 65))
        player1.charactersdata["bishop"][i] = pygame.transform.smoothscale(original_pcs["B"][i], (65, 65))
        player1.charactersdata["knight"][i] = pygame.transform.smoothscale(original_pcs["N"][i], (65, 65))
        player2.charactersdata["rook"][i] = pygame.transform.smoothscale(original_pcs["r"][i], (65, 65))
        player2.charactersdata["bishop"][i] = pygame.transform.smoothscale(original_pcs["b"][i], (65, 65))
        player2.charactersdata["knight"][i] = pygame.transform.smoothscale(original_pcs["n"][i], (65, 65))
    player1.charactersdata["queen"][0] = pygame.transform.smoothscale(original_pcs["Q"][0], (65, 65))
    player1.charactersdata["king"][0] = pygame.transform.smoothscale(original_pcs["K"][0], (65, 65))
    player2.charactersdata["queen"][0] = pygame.transform.smoothscale(original_pcs["q"][0], (65, 65))
    player2.charactersdata["king"][0] = pygame.transform.smoothscale(original_pcs["k"][0], (65, 65))


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
packedsqr = {"white": [], "black": []}
def ckcpcn():
    packedsqr.clear()
    packedsqr["white"] = []
    packedsqr["black"] = []
    for player_obj in [player1]:
        for p_type, p_data in player_obj.characters.items():
            for idx, piece in enumerate(p_data["detail"]):
                if piece["alive"]:
                    packedsqr["white"].append(piece["position"])
    for player_obj in [player2]:
        for p_type, p_data in player_obj.characters.items():
            for idx, piece in enumerate(p_data["detail"]):
                if piece["alive"]:
                    packedsqr["black"].append(piece["position"])



piece_position_map = {}
pcs = {
    "K": player1.charactersdata["king"],
    "Q": player1.charactersdata["queen"],
    "R": player1.charactersdata["rook"],
    "B": player1.charactersdata["bishop"],
    "N": player1.charactersdata["knight"],
    "P": player1.charactersdata["pawn"],
    "k": player2.charactersdata["king"],
    "q": player2.charactersdata["queen"],
    "r": player2.charactersdata["rook"],
    "b": player2.charactersdata["bishop"],
    "n": player2.charactersdata["knight"],
    "p": player2.charactersdata["pawn"]
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
        return pawn_moves(pos, color, packedsqr)
    return []

def block_filtered_moves(char, pos, raw_moves, color):
    enemy_color = "black" if color == "white" else "white"
    own_positions = set(packedsqr[color])
    enemy_positions = set(packedsqr[enemy_color])
    x0, y0 = pos_to_coord(pos)
    valid_moves = []

    for move in raw_moves:
        x1, y1 = pos_to_coord(move)

        dx = x1 - x0
        dy = y1 - y0

        # For non-sliding pieces (knight, king, pawn), skip filtering
        if char.upper() in ["N", "K", "P"]:
            if move not in own_positions:
                valid_moves.append(move)
            continue

        step_x = 0 if dx == 0 else dx // abs(dx)
        step_y = 0 if dy == 0 else dy // abs(dy)

        cx, cy = x0 + step_x, y0 + step_y
        blocked = False

        while (cx, cy) != (x1, y1):
            inter_pos = coord_to_pos(cx, cy)
            if inter_pos in own_positions or inter_pos in enemy_positions:
                blocked = True
                break
            cx += step_x
            cy += step_y

        if not blocked:
            if move not in own_positions:
                valid_moves.append(move)

    return valid_moves


clock = pygame.time.Clock()
running = True
Selected = None
wt = True
psblmv = []
raw_moves = []
nextmv = None
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

            if Selected and square in psblmv:
                nextmv = square
            else:
                if square in piece_position_map:
                    Selected = piece_position_map[square]
                else:
                    Selected = None
                psblmv = []
                raw_moves = []


            print(f"Clicked square: {square}")
            print(f"All pieces: {piece_position_map.keys()}")
            print(f"psblmv {psblmv}\n" if psblmv else "n", end = "")
            print(f"rawmv {raw_moves}\n" if raw_moves else "N", end ="")
    
            # 🟢 Now we compute moves AFTER setting Selected
            if Selected is not None and ((Selected[0].isupper() and wt) or (Selected[0].islower() and not(wt))):
                ckcpcn()
                char = Selected[0]
                idx = Selected[1]
                pos = player1.characters[pic[char]]["detail"][idx]["position"] if wt else player2.characters[pic[char.upper()]]["detail"][idx]["position"]
                raw_moves = get_moves(char, pos, "white" if wt else "black")
                psblmv = block_filtered_moves(char, pos, raw_moves, "white" if wt else "black")

                if Selected and (square not in packedsqr and square in psblmv):
                    nextmv = square
                else:
                    print(f"next move {nextmv} cuz {square} not in {psblmv}")

                # nextmv = square if (square not in packedsqr and square in raw_moves) else None
                print(f" next move {nextmv}")

                print(f"slected {Selected}")
            if square in piece_position_map:
                Selected = piece_position_map[square]
            elif square not in psblmv:
                Selected = None
                psblmv = []  # ← Add this to clear old moves
                raw_moves = []

            print(f"Clicked square: {square}")
            print(f"All pieces: {piece_position_map.keys()}")
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
    if Selected is not None:
        
        
        for i in psblmv:
            col = ord(i[0]) - ord('a')
            row = 8 - int(i[1])
            center = (col * square_size + square_size // 2, row * square_size + square_size // 2)
            pygame.draw.circle(screen, (210, 249, 83), center, 10)

    if nextmv is not None and Selected is not None:
        
        if Selected[0].isupper() and wt:
            player1.characters[pic[Selected[0]]]["detail"][Selected[1]]["position"] = nextmv
        else:
            player2.characters[pic[Selected[0].upper()]]["detail"][Selected[1]]["position"] = nextmv
        Selected = None
        psblmv = []
        nextmv = None
        wt = not wt
    else:
        print(f"selected {Selected}")

    pygame.display.flip()
    pygame.display.update()

pygame.quit()
