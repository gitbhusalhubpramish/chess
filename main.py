import os
import pygame
from player import player
import platform
from moves import knight_moves, king_moves, rook_moves, bishop_moves, queen_moves, pawn_moves, coord_to_pos, pos_to_coord
import itertools

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
piece_position_map = {}
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
        player1.charactersdata["pawn"][i] = pygame.transform.smoothscale(original_pcs["P"][i], (65, 65)) if player1.characters["pawn"]["detail"][i]["alive"] else None
        player2.charactersdata["pawn"][i] = pygame.transform.smoothscale(original_pcs["p"][i], (65, 65)) if player2.characters["pawn"]["detail"][i]["alive"] else None
    for i in range(2):
        player1.charactersdata["rook"][i] = pygame.transform.smoothscale(original_pcs["R"][i], (65, 65)) if player1.characters["rook"]["detail"][i]["alive"] else None
        player1.charactersdata["bishop"][i] = pygame.transform.smoothscale(original_pcs["B"][i], (65, 65)) if player1.characters["bishop"]["detail"][i]["alive"] else None
        player1.charactersdata["knight"][i] = pygame.transform.smoothscale(original_pcs["N"][i], (65, 65)) if player1.characters["knight"]["detail"][i]["alive"] else None
        player2.charactersdata["rook"][i] = pygame.transform.smoothscale(original_pcs["r"][i], (65, 65)) if player2.characters["rook"]["detail"][i]["alive"] else None
        player2.charactersdata["bishop"][i] = pygame.transform.smoothscale(original_pcs["b"][i], (65, 65)) if player2.characters["bishop"]["detail"][i]["alive"] else None
        player2.charactersdata["knight"][i] = pygame.transform.smoothscale(original_pcs["n"][i], (65, 65)) if player2.characters["knight"]["detail"][i]["alive"] else None
    player1.charactersdata["queen"][0] = pygame.transform.smoothscale(original_pcs["Q"][0], (65, 65)) if player1.characters["queen"]["detail"][0]["alive"] else None
    player1.charactersdata["king"][0] = pygame.transform.smoothscale(original_pcs["K"][0], (65, 65)) if player1.characters["king"]["detail"][0]["alive"] else None
    player2.charactersdata["queen"][0] = pygame.transform.smoothscale(original_pcs["q"][0], (65, 65)) if player2.characters["queen"]["detail"][0]["alive"] else None
    player2.charactersdata["king"][0] = pygame.transform.smoothscale(original_pcs["k"][0], (65, 65)) if player2.characters["king"]["detail"][0]["alive"] else None


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
piece_map = {'king': 'K', 'queen': 'Q', 'rook': 'R', 'bishop': 'B', 'knight': 'N', 'pawn': 'P'}

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
for player_obj in [player1, player2]:
    for piece_type, piece_data in player_obj.characters.items():
        for piece_detail in piece_data["detail"]:
            piece_detail["moves"] = get_moves(piece_type[0].upper(), piece_detail["position"], player_obj.color)


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
# ... (keep all the initial code the same until the game loop)

clock = pygame.time.Clock()
running = True
Selected = None
wt = True
nextmv = None

def is_king_in_check(player_obj):
    """Check if the player's king is in check"""
    king_pos = player_obj.characters["king"]["detail"][0]["position"]
    enemy_color = "white" if player_obj.color == "black" else "black"
    enemy_player = player1 if enemy_color == "white" else player2
    
    for piece_type, piece_data in enemy_player.characters.items():
        for piece_detail in piece_data["detail"]:
            if piece_detail["alive"] and king_pos in piece_detail["moves"]:
                return True
    return False

def filter_moves_for_check(player_obj, piece_type, piece_idx, moves):
    """Filter moves to only allow those that get the king out of check"""
    if not is_king_in_check(player_obj):
        return moves
    
    valid_moves = []
    enemy_player = player1 if player_obj.color == "black" else player2
    
    for move in moves:
        # Save original state
        original_pos = player_obj.characters[piece_type]["detail"][piece_idx]["position"]
        captured_piece = None
        captured_idx = None
        captured_type = None
        
        # Check if there's a piece to capture
        for other_type, other_data in enemy_player.characters.items():
            for other_idx, other_piece in enumerate(other_data["detail"]):
                if other_piece["alive"] and other_piece["position"] == move:
                    captured_piece = other_piece
                    captured_idx = other_idx
                    captured_type = other_type
                    other_piece["alive"] = False
                    break
        
        # Simulate the move
        player_obj.characters[piece_type]["detail"][piece_idx]["position"] = move
        
        # Update enemy moves and check if king is still in check
        ckcpcn()
        for enemy_piece_type, enemy_piece_data in enemy_player.characters.items():
            for enemy_piece_detail in enemy_piece_data["detail"]:
                if enemy_piece_detail["alive"]:
                    enemy_char = piece_map[enemy_piece_type]
                    if enemy_player.color == "black":
                        enemy_char = enemy_char.lower()
                    enemy_raw_moves = get_moves(enemy_char, enemy_piece_detail["position"], enemy_player.color)
                    enemy_piece_detail["moves"] = block_filtered_moves(enemy_char, enemy_piece_detail["position"], enemy_raw_moves, enemy_player.color)
        
        # Check if king is still in check after this move
        king_still_in_check = is_king_in_check(player_obj)
        
        # Restore original state
        player_obj.characters[piece_type]["detail"][piece_idx]["position"] = original_pos
        if captured_piece:
            captured_piece["alive"] = True
        
        # If this move gets the king out of check, it's valid
        if not king_still_in_check:
            valid_moves.append(move)
    
    return valid_moves

def update_all_moves():
    """Update possible moves for all pieces"""
    ckcpcn()  # Update packed squares first
    
    # First pass: calculate raw moves for all pieces
    for player_obj in [player1, player2]:
        for piece_type, piece_data in player_obj.characters.items():
            for piece_detail in piece_data["detail"]:
                if piece_detail["alive"]:
                    char = piece_map[piece_type]
                    if player_obj.color == "black":
                        char = char.lower()
                    raw_moves = get_moves(char, piece_detail["position"], player_obj.color)
                    piece_detail["moves"] = block_filtered_moves(char, piece_detail["position"], raw_moves, player_obj.color)
                else:
                    piece_detail["moves"] = []
    
    # Second pass: filter moves based on check status
    for player_obj in [player1, player2]:
        for piece_type, piece_data in player_obj.characters.items():
            for idx, piece_detail in enumerate(piece_data["detail"]):
                if piece_detail["alive"]:
                    piece_detail["moves"] = filter_moves_for_check(player_obj, piece_type, idx, piece_detail["moves"])

def is_checkmate(player_obj):
    """Check if the player is in checkmate"""
    king_pos = player_obj.characters["king"]["detail"][0]["position"]
    enemy_color = "white" if player_obj.color == "black" else "black"
    enemy_moves = []
    
    # Get all enemy moves
    enemy_player = player1 if enemy_color == "white" else player2
    for piece_type, piece_data in enemy_player.characters.items():
        for piece_detail in piece_data["detail"]:
            if piece_detail["alive"]:
                enemy_moves.extend(piece_detail["moves"])
    
    # If king is not in check, it's not checkmate
    if king_pos not in enemy_moves:
        return False
    
    # Try all possible moves for the player in check
    for piece_type, piece_data in player_obj.characters.items():
        for idx, piece_detail in enumerate(piece_data["detail"]):
            if piece_detail["alive"]:
                original_pos = piece_detail["position"]
                
                # Try each possible move
                for move in piece_detail["moves"]:
                    # Simulate the move
                    captured_piece = None
                    captured_idx = None
                    captured_type = None
                    
                    # Check if there's a piece to capture
                    for other_type, other_data in enemy_player.characters.items():
                        for other_idx, other_piece in enumerate(other_data["detail"]):
                            if other_piece["alive"] and other_piece["position"] == move:
                                captured_piece = other_piece
                                captured_idx = other_idx
                                captured_type = other_type
                                other_piece["alive"] = False
                                break
                    
                    # Move the piece
                    piece_detail["position"] = move
                    
                    # Update all moves and check if king is still in check
                    update_all_moves()
                    ckcmv()
                    
                    new_king_pos = player_obj.characters["king"]["detail"][0]["position"]
                    new_enemy_moves = []
                    for enemy_piece_type, enemy_piece_data in enemy_player.characters.items():
                        for enemy_piece_detail in enemy_piece_data["detail"]:
                            if enemy_piece_detail["alive"]:
                                new_enemy_moves.extend(enemy_piece_detail["moves"])
                    
                    king_still_in_check = new_king_pos in new_enemy_moves
                    
                    # Restore the original state
                    piece_detail["position"] = original_pos
                    if captured_piece:
                        captured_piece["alive"] = True
                    
                    # If this move gets the king out of check, it's not checkmate
                    if not king_still_in_check:
                        update_all_moves()
                        ckcmv()
                        return False
    
    # If no move can get the king out of check, it's checkmate
    update_all_moves()
    ckcmv()
    return True

# Initialize moves for all pieces
update_all_moves()
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

ckcmv()

while running:
    draw_board((255, 255, 255), 8, 8, 70, (150, 75, 0))
    drawpcs()

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

            if Selected and square in Selected[2]:  # Selected[2] contains the moves
                # Move the piece
                moved_char, moved_idx, _ = Selected
                piece_type = pic[moved_char.upper()]

                # Handle capturing
                if square in piece_position_map:
                    captured_char, captured_idx = piece_position_map[square]
                    captured_type = pic[captured_char.upper()]
                    if captured_char.isupper():
                        player1.characters[captured_type]["detail"][captured_idx]["alive"] = False
                    else:
                        player2.characters[captured_type]["detail"][captured_idx]["alive"] = False

                # Update position
                if moved_char.isupper():
                    player1.characters[piece_type]["detail"][moved_idx]["position"] = square
                else:
                    player2.characters[piece_type]["detail"][moved_idx]["position"] = square

                # Switch turn and update all moves
                wt = not wt
                Selected = None
                update_all_moves()
                ckcmv()
                if not player1.characters["king"]["detail"][0]["alive"]:
                    print("Black wins")
                    running = False
                elif not player2.characters["king"]["detail"][0]["alive"]:
                    print("White wins")
                    running = False
                
                # Reset check status
                
                
                if player1.characters['king']['detail'][0]['position'] in list(itertools.chain.from_iterable(packedmvsqr['black'])):
                    print("Check white")
                    player1.characters["king"]["check"] = True
                    if is_checkmate(player1):
                        print("Checkmate! Black wins!")
                        player1.characters["king"]["checkmate"] = True
                        running = False
                elif player2.characters['king']['detail'][0]['position'] in list(itertools.chain.from_iterable(packedmvsqr['white'])):
                    print("Check black")
                    player2.characters["king"]["check"] = True
                    if is_checkmate(player2):
                        print("Checkmate! White wins!")
                        player2.characters["king"]["checkmate"] = True
                        running = False
                else:
                    player1.characters["king"]["check"] = False
                    player2.characters["king"]["check"] = False
                    player1.characters["king"]["checkmate"] = False
                    player2.characters["king"]["checkmate"] = False

            elif square in piece_position_map:
                char, idx = piece_position_map[square]
                # Check if it's the correct player's turn
                if (wt and char.isupper()) or (not wt and char.islower()):
                    piece_type = pic[char.upper()]
                    if char.isupper():
                        moves = player1.characters[piece_type]["detail"][idx]["moves"]
                    else:
                        moves = player2.characters[piece_type]["detail"][idx]["moves"]
                    Selected = (char, idx, moves)
            else:
                Selected = None

    # Highlight possible moves
    if Selected is not None:
        for move in Selected[2]:
            col = ord(move[0]) - ord('a')
            row = 8 - int(move[1])
            center = (col * square_size + square_size // 2, row * square_size + square_size // 2)
            pygame.draw.circle(screen, (210, 249, 83), center, 10)

    # Handle piece resizing based on selection
    if wt and Selected is None:
        whtrsz(75)
        blkrsz(65)
    elif not wt and Selected is None:
        whtrsz(65)
        blkrsz(75)
    elif Selected is not None:
        dcrzall()
        rsz(85, Selected[0], Selected[1])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()