import pygame
from player import player
from moves import knight_moves, king_moves, rook_moves, bishop_moves, queen_moves, pawn_moves
WINDOW_SIZE = (560, 560)
screen = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)
def draw_board(WHITE, ROWS, COLS, SQUARE_SIZE, BROWN):
  screen.fill(WHITE)
  for row in range(ROWS):
      for col in range(COLS):
          if (row + col) % 2 != 0:
              pygame.draw.rect(screen, BROWN,
                               (col * SQUARE_SIZE, row * SQUARE_SIZE,
                                SQUARE_SIZE, SQUARE_SIZE))


wk = []
wq = []
wr = []
wb = []
wn = []
wp = []
player1 = player("white", wk, wq, wr, wb, wn, wp)
wk = [
    pygame.image.load("white player/king.png")
    for _ in range(player1.characters["king"]["no"])
]
wq = [
    pygame.image.load("white player/queen.png")
    for _ in range(player1.characters["queen"]["no"])
]
wr = [
    pygame.image.load("white player/rook.png")
    for _ in range(player1.characters["rook"]["no"])
]
wb = [
    pygame.image.load("white player/bishop.png")
    for _ in range(player1.characters["bishop"]["no"])
]
wn = [
    pygame.image.load("white player/knight.png")
    for _ in range(player1.characters["knight"]["no"])
]
wp = [
    pygame.image.load("white player/pawn.png")
    for _ in range(player1.characters["pawn"]["no"])
]
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
bk = [
    pygame.image.load("black player/king.png")
    for _ in range(player2.characters["king"]["no"])
]
bq = [
    pygame.image.load("black player/queen.png")
    for _ in range(player2.characters["queen"]["no"])
]
br = [
    pygame.image.load("black player/rook.png")
    for _ in range(player2.characters["rook"]["no"])
]
bb = [
    pygame.image.load("black player/bishop.png")
    for _ in range(player2.characters["bishop"]["no"])
]
bn = [
    pygame.image.load("black player/knight.png")
    for _ in range(player2.characters["knight"]["no"])
]
bp = [
    pygame.image.load("black player/pawn.png")
    for _ in range(player2.characters["pawn"]["no"])
]

player2.charactersdata["king"] = bk
player2.charactersdata["queen"] = bq
player2.charactersdata["rook"] = br
player2.charactersdata["bishop"] = bb
player2.charactersdata["knight"] = bn
player2.charactersdata["pawn"] = bp

original_pcs = {
    "K": [
        pygame.image.load("white player/king.png")
        for _ in range(player1.characters["king"]["no"])
    ],
    "Q": [
        pygame.image.load("white player/queen.png")
        for _ in range(player1.characters["queen"]["no"])
    ],
    "R": [
        pygame.image.load("white player/rook.png")
        for _ in range(player1.characters["rook"]["no"])
    ],
    "B": [
        pygame.image.load("white player/bishop.png")
        for _ in range(player1.characters["bishop"]["no"])
    ],
    "N": [
        pygame.image.load("white player/knight.png")
        for _ in range(player1.characters["knight"]["no"])
    ],
    "P": [
        pygame.image.load("white player/pawn.png")
        for _ in range(player1.characters["pawn"]["no"])
    ],
    "k": [
        pygame.image.load("black player/king.png")
        for _ in range(player2.characters["king"]["no"])
    ],
    "q": [
        pygame.image.load("black player/queen.png")
        for _ in range(player2.characters["queen"]["no"])
    ],
    "r": [
        pygame.image.load("black player/rook.png")
        for _ in range(player2.characters["rook"]["no"])
    ],
    "b": [
        pygame.image.load("black player/bishop.png")
        for _ in range(player2.characters["bishop"]["no"])
    ],
    "n": [
        pygame.image.load("black player/knight.png")
        for _ in range(player2.characters["knight"]["no"])
    ],
    "p": [
        pygame.image.load("black player/pawn.png")
        for _ in range(player2.characters["pawn"]["no"])
    ]
}


def whtrsz(siz):
    for i in range(8):
        player1.charactersdata["pawn"][i] = pygame.transform.smoothscale(
            original_pcs["P"][i], (siz, siz))
    for i in range(2):
        player1.charactersdata["rook"][i] = pygame.transform.smoothscale(
            original_pcs["R"][i], (siz, siz))
        player1.charactersdata["bishop"][i] = pygame.transform.smoothscale(
            original_pcs["B"][i], (siz, siz))
        player1.charactersdata["knight"][i] = pygame.transform.smoothscale(
            original_pcs["N"][i], (siz, siz))
    player1.charactersdata["queen"][0] = pygame.transform.smoothscale(
        original_pcs["Q"][0], (siz, siz))
    player1.charactersdata["king"][0] = pygame.transform.smoothscale(
        original_pcs["K"][0], (siz, siz))


def blkrsz(siz):
    for i in range(8):
        player2.charactersdata["pawn"][i] = pygame.transform.smoothscale(
            original_pcs["p"][i], (siz, siz))
    for i in range(2):
        player2.charactersdata["rook"][i] = pygame.transform.smoothscale(
            original_pcs["r"][i], (siz, siz))
        player2.charactersdata["bishop"][i] = pygame.transform.smoothscale(
            original_pcs["b"][i], (siz, siz))
        player2.charactersdata["knight"][i] = pygame.transform.smoothscale(
            original_pcs["n"][i], (siz, siz))
    player2.charactersdata["queen"][0] = pygame.transform.smoothscale(
        original_pcs["q"][0], (siz, siz))
    player2.charactersdata["king"][0] = pygame.transform.smoothscale(
        original_pcs["k"][0], (siz, siz))


def rsz(siz, psc, idx):
    pcs[psc][idx] = pygame.transform.smoothscale(original_pcs[psc][idx],
                                                 (siz, siz))


def dcrzall():
    for i in range(8):
        player1.charactersdata["pawn"][i] = pygame.transform.smoothscale(
            original_pcs["P"][i],
            (65,
             65)) if player1.characters["pawn"]["detail"][i]["alive"] else None
        player2.charactersdata["pawn"][i] = pygame.transform.smoothscale(
            original_pcs["p"][i],
            (65,
             65)) if player2.characters["pawn"]["detail"][i]["alive"] else None
    for i in range(2):
        player1.charactersdata["rook"][i] = pygame.transform.smoothscale(
            original_pcs["R"][i],
            (65,
             65)) if player1.characters["rook"]["detail"][i]["alive"] else None
        player1.charactersdata["bishop"][i] = pygame.transform.smoothscale(
            original_pcs["B"][i],
            (65, 65
             )) if player1.characters["bishop"]["detail"][i]["alive"] else None
        player1.charactersdata["knight"][i] = pygame.transform.smoothscale(
            original_pcs["N"][i],
            (65, 65
             )) if player1.characters["knight"]["detail"][i]["alive"] else None
        player2.charactersdata["rook"][i] = pygame.transform.smoothscale(
            original_pcs["r"][i],
            (65,
             65)) if player2.characters["rook"]["detail"][i]["alive"] else None
        player2.charactersdata["bishop"][i] = pygame.transform.smoothscale(
            original_pcs["b"][i],
            (65, 65
             )) if player2.characters["bishop"]["detail"][i]["alive"] else None
        player2.charactersdata["knight"][i] = pygame.transform.smoothscale(
            original_pcs["n"][i],
            (65, 65
             )) if player2.characters["knight"]["detail"][i]["alive"] else None
    player1.charactersdata["queen"][0] = pygame.transform.smoothscale(
        original_pcs["Q"][0],
        (65,
         65)) if player1.characters["queen"]["detail"][0]["alive"] else None
    player1.charactersdata["king"][0] = pygame.transform.smoothscale(
        original_pcs["K"][0],
        (65, 65)) if player1.characters["king"]["detail"][0]["alive"] else None
    player2.charactersdata["queen"][0] = pygame.transform.smoothscale(
        original_pcs["q"][0],
        (65,
         65)) if player2.characters["queen"]["detail"][0]["alive"] else None
    player2.charactersdata["king"][0] = pygame.transform.smoothscale(
        original_pcs["k"][0],
        (65, 65)) if player2.characters["king"]["detail"][0]["alive"] else None
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

pic = {
    "K": "king",
    "Q": "queen",
    "R": "rook",
    "B": "bishop",
    "N": "knight",
    "P": "pawn"
}
piece_map = {
    'king': 'K',
    'queen': 'Q',
    'rook': 'R',
    'bishop': 'B',
    'knight': 'N',
    'pawn': 'P'
}
piece_position_map = {}
square_size = 70
def drawpcs():
    piece_position_map.clear()

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
files = 'abcdefgh'
ranks = '12345678'
chess_positions = {
    f"{files[col]}{ranks[7 - row]}": {
        "x": col * square_size,
        "y": row * square_size
    }
    for row in range(8)
    for col in range(8)
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

packedmv = []
packedmvsqr = {"white": [], "black": []}
def ckcmv():
    packedmv.clear()
    packedmvsqr.clear()
    packedmvsqr["white"] = []
    packedmvsqr["black"] = []
    for player_obj in [player1, player2]:
        for piece_type, piece_data in player_obj.characters.items():
            for piece_detail in piece_data["detail"]:
                packedmv.append(piece_detail["moves"])
                packedmvsqr[player_obj.color].append(piece_detail["moves"])