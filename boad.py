import pygame
from player import player
from moves import knight_moves, king_moves, rook_moves, bishop_moves, queen_moves, pawn_moves, coord_to_pos, pos_to_coord
import itertools

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
    # This might need to be more dynamic if multiple queens are promoted
    if len(player1.charactersdata["queen"]) > 0: # Check if queen exists before accessing
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
    # This might need to be more dynamic if multiple queens are promoted
    if len(player2.charactersdata["queen"]) > 0: # Check if queen exists before accessing
        player2.charactersdata["queen"][0] = pygame.transform.smoothscale(
            original_pcs["q"][0], (siz, siz))
    player2.charactersdata["king"][0] = pygame.transform.smoothscale(
        original_pcs["k"][0], (siz, siz))

def rsz(player_obj, piece_type_str, idx, new_size):
    """
    Resizes a specific piece and updates its corresponding image in player.charactersdata.
    Requires player_obj (player1 or player2), piece_type_str (e.g., "queen"),
    index of the piece in its detail list, and the new size.
    """
    if player_obj.color == "white":
        char_key = piece_map[piece_type_str]
    else:
        char_key = piece_map[piece_type_str].lower()

    if idx < len(original_pcs[char_key]):
        # Update the image in player_obj.charactersdata directly
        # This assumes original_pcs has the unscaled image for this index.
        player_obj.charactersdata[piece_type_str][idx] = pygame.transform.smoothscale(
            original_pcs[char_key][idx], (new_size, new_size)
        )
        # Note: You would still need to call drawpcs() afterwards for the change to show on screen.
    else:
        print(f"Error: Cannot resize piece. Index {idx} for {piece_type_str} not found in original_pcs or characterdata.")

def dcrzall():
    for player_obj in [player1, player2]: # Renamed 'i' to 'player_obj' for clarity
        for piece_type in player_obj.charactersdata: # Renamed 'j' to 'piece_type'
            char_key = piece_map[piece_type] if player_obj.color == "white" else piece_map[piece_type].lower()

            # We need to ensure that original_pcs[char_key] has an image for every
            # piece listed in player_obj.characters[piece_type]["detail"].
            # If a new piece (promoted pawn) exists in "detail" but not yet in original_pcs,
            # load its image and append it to original_pcs.

            # Loop through the 'detail' list to find out how many pieces of this type exist
            for k in range(len(player_obj.characters[piece_type]["detail"])):
                # If this 'k' index is beyond what original_pcs[char_key] currently holds,
                # it means a new piece has been added (promoted pawn) and needs its image loaded.
                if k >= len(original_pcs[char_key]):
                    if player_obj.color == "white":
                        image_path = f"white player/{piece_type}.png"
                    else:
                        image_path = f"black player/{piece_type}.png"

                    new_img = pygame.image.load(image_path)
                    original_pcs[char_key].append(new_img) # Add the new image to original_pcs

            # Now that original_pcs is guaranteed to have all necessary images,
            # we can create the scaled images for player_obj.charactersdata.
            newly_scaled_images_list = []
            for k in range(len(player_obj.characters[piece_type]["detail"])):
                scaled_img = pygame.transform.smoothscale(original_pcs[char_key][k], (65, 65))
                newly_scaled_images_list.append(scaled_img)

            # Update player_obj.charactersdata[piece_type] with the new list of scaled images
            player_obj.charactersdata[piece_type] = newly_scaled_images_list


# Global pcs dictionary (will be re-initialized in drawpcs)
pcs = {} # Initialize empty, it will be filled in drawpcs

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

    # IMPORTANT: Refresh the pcs dictionary with the latest characterdata
    # This is the crucial step to ensure 'pcs' always points to the most
    # up-to-date lists of resized images, including promoted ones.
    global pcs
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


    for player_obj in [player1, player2]:
        for p_type, p_data in player_obj.characters.items():
            char = piece_map[p_type]
            if player_obj.color == "black":
                char = char.lower()

            # Iterate using the 'detail' list, which is the source of truth for piece count
            for idx, piece in enumerate(p_data["detail"]):
                if piece["alive"]:
                    pos = piece["position"]
                    col = ord(pos[0]) - ord('a')
                    row = 8 - int(pos[1])
                    x, y = col * square_size, row * square_size

                    # Ensure that pcs[char] has enough elements.
                    # With the re-assignment of pcs inside drawpcs, this check
                    # should now pass correctly.
                    if idx < len(pcs[char]):
                        screen.blit(pcs[char][idx], (x, y))
                        piece_position_map[pos] = (char, idx)
                    else:
                        print(f"Warning: Index {idx} out of range for pcs[{char}]. This piece might not have been correctly resized/loaded.")
                        # This 'else' block should ideally not be hit with the current fixes.
                        # If it is, there's still a synchronization issue between
                        # player.characters[type]["detail"] and player.charactersdata[type]
                        # or pcs.

                        # As a fallback, you could try to load and blit it here,
                        # but it's better to ensure dcrzall and pcs refresh correctly.


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


def is_square_empty(square):
    """Checks if a given square is empty."""
    return square not in piece_position_map

def is_square_attacked(square, attacking_color):
    """
    Checks if a given square is attacked by any piece of the attacking_color.
    This function will simulate moves of all pieces of `attacking_color`
    to see if any of them can reach `square`.
    """
    opponent_player_obj = player1 if attacking_color == "white" else player2

    # Iterate through all opponent pieces
    for piece_type, piece_data in opponent_player_obj.characters.items():
        for piece_detail in piece_data["detail"]:
            if piece_detail["alive"]:
                current_pos = piece_detail["position"]

                # Get the character representation (e.g., 'R' for Rook)
                char_key = piece_map[piece_type]
                if opponent_player_obj.color == "black":
                    char_key = char_key.lower()

                # Get the raw moves for this attacking piece
                raw_moves_of_attacker = get_moves_for_attack_check(char_key, current_pos, attacking_color)

                # Filter blocked moves for sliding pieces.
                # For `is_square_attacked`, we need to check if the *path* is clear to the target square,
                # even if there's a piece *on* the target square.
                # The `filter_blocked_moves` you already have should work for this.
                filtered_moves_of_attacker = filter_blocked_moves(char_key, current_pos, raw_moves_of_attacker, attacking_color)

                if square in filtered_moves_of_attacker:
                    return True
    return False

# A helper function similar to get_moves but specifically for attack checks.
# This prevents circular dependency if `get_moves` itself calls `is_square_attacked`
# and needs to know about raw moves.
def get_moves_for_attack_check(char, pos, color):
    """Returns raw moves for a piece, to be used specifically for attack checks (no castling, no check validation)."""
    if char.upper() == 'K':
        return king_moves(pos) # Standard king moves, no castling here
    elif char.upper() == 'Q':
        return queen_moves(pos)
    elif char.upper() == 'R':
        return rook_moves(pos)
    elif char.upper() == 'B':
        return bishop_moves(pos)
    elif char.upper() == 'N':
        return knight_moves(pos)
    elif char.upper() == 'P':
        # Pawn attacks are diagonal. For attack checks, we only care about these.
        x, y = pos_to_coord(pos)
        moves = []
        direction = 1 if color == "white" else -1
        for dx in [-1, 1]:
            diag = coord_to_pos(x + dx, y + direction)
            if diag:
                moves.append(diag)
        return moves
    return []


def get_moves(char, pos, color):
    # Retrieve the base moves
    moves = []
    if char.upper() == 'K':
        moves = king_moves(pos) # Gets standard King moves
    elif char.upper() == 'Q':
        moves = queen_moves(pos)
    elif char.upper() == 'R':
        moves = rook_moves(pos)
    elif char.upper() == 'B':
        moves = bishop_moves(pos)
    elif char.upper() == 'N':
        moves = knight_moves(pos)
    elif char.upper() == 'P':
        moves = pawn_moves(pos, color, packedsqr) # Your existing pawn moves
    # --- Castling Logic ---
    if char.upper() == 'K': # Only for the King
        current_player_obj = player1 if color == "white" else player2
        opponent_color = "black" if color == "white" else "white"

        king_detail = current_player_obj.characters["king"]["detail"][0] # Assuming only one king

        # Check if king has moved or is in check
        if not king_detail["moved"] and not current_player_obj.characters["king"]["check"]:
            # Kingside Castling (0-0)
            if color == "white":
                rook_h_pos = "h1"
                king_path_squares = ["f1", "g1"] # Squares king moves through/to
                empty_squares = ["f1", "g1"] # Squares that must be empty
                target_king_pos = "g1"
                rook_idx = 1 # Index of the h1 rook
            else: # Black
                rook_h_pos = "h8"
                king_path_squares = ["f8", "g8"]
                empty_squares = ["f8", "g8"]
                target_king_pos = "g8"
                rook_idx = 1 # Index of the h8 rook

            rook_h_detail = current_player_obj.characters["rook"]["detail"][rook_idx]

            # Check if kingside rook exists, hasn't moved, and is at its original position
            if rook_h_detail["alive"] and not rook_h_detail["moved"] and \
               rook_h_detail["position"] == rook_h_pos:

                path_clear = True
                for s in empty_squares:
                    if not is_square_empty(s):
                        path_clear = False
                        break

                # Check if king's current square or path squares are attacked
                king_safe = not is_square_attacked(pos, opponent_color) and \
                            not is_square_attacked(king_path_squares[0], opponent_color) and \
                            not is_square_attacked(king_path_squares[1], opponent_color)

                if path_clear and king_safe:
                    moves.append(target_king_pos)

            # Queenside Castling (0-0-0)
            if color == "white":
                rook_a_pos = "a1"
                king_path_squares = ["d1", "c1"] # Squares king moves through/to
                empty_squares = ["b1", "c1", "d1"] # Squares that must be empty
                target_king_pos = "c1"
                rook_idx = 0 # Index of the a1 rook
            else: # Black
                rook_a_pos = "a8"
                king_path_squares = ["d8", "c8"]
                empty_squares = ["b8", "c8", "d8"]
                target_king_pos = "c8"
                rook_idx = 0 # Index of the a8 rook

            rook_a_detail = current_player_obj.characters["rook"]["detail"][rook_idx]

            # Check if queenside rook exists, hasn't moved, and is at its original position
            if rook_a_detail["alive"] and not rook_a_detail["moved"] and \
               rook_a_detail["position"] == rook_a_pos:

                path_clear = True
                for s in empty_squares:
                    if not is_square_empty(s):
                        path_clear = False
                        break

                # Check if king's current square or path squares are attacked
                king_safe = not is_square_attacked(pos, opponent_color) and \
                            not is_square_attacked(king_path_squares[0], opponent_color) and \
                            not is_square_attacked(king_path_squares[1], opponent_color)

                if path_clear and king_safe:
                    moves.append(target_king_pos)

    return moves



packedmv = []
packedmvsqr = {"white": [], "black": []}
packedmvpic = {"white": [], "black": []}


def ckcmv():
    packedmv.clear()
    packedmvsqr.clear()
    packedmvpic.clear()
    packedmvsqr["white"] = []
    packedmvsqr["black"] = []
    packedmvpic["white"] = []
    packedmvpic["black"] = []
    for player_obj in [player1, player2]:
        for piece_type, piece_data in player_obj.characters.items():
            for piece_detail in piece_data["detail"]:
                if piece_detail["alive"]:
                    packedmv.append(piece_detail["moves"])
                    packedmvsqr[player_obj.color].append(piece_detail["moves"])
                    packedmvpic[player_obj.color].append({piece_type : piece_detail["moves"]})

def filter_blocked_moves(char, pos, raw_moves, color):
    """Filter moves blocked by other pieces (without check validation)"""
    enemy_color = "black" if color == "white" else "white"
    own_positions = set(packedsqr[color])
    enemy_positions = set(packedsqr[enemy_color])
    x0, y0 = pos_to_coord(pos)
    valid_moves = []

    for move in raw_moves:
        x1, y1 = pos_to_coord(move)
        dx = x1 - x0
        dy = y1 - y0

        # For non-sliding pieces (knight, king), skip path checking
        if char.upper() in ["N", "K"]:
            if move not in own_positions:
                valid_moves.append(move)
            continue

        # For pawns (special movement rules)
        if char.upper() == "P":
            # Handle pawn captures differently
            if abs(dx) == 1 and abs(dy) == 1:  # Diagonal capture
                if move in enemy_positions:
                    valid_moves.append(move)
            else:  # Forward movement
                step_y = dy // abs(dy) if dy != 0 else 0
                blocked = False
                cy = y0 + step_y
                while cy != y1:
                    current_pos = coord_to_pos(x0, cy)
                    if current_pos in own_positions or current_pos in enemy_positions:
                        blocked = True
                        break
                    cy += step_y
                if not blocked and move not in own_positions and move not in enemy_positions:
                    valid_moves.append(move)
            continue

        # For sliding pieces (queen, rook, bishop)
        step_x = 0 if dx == 0 else dx // abs(dx)
        step_y = 0 if dy == 0 else dy // abs(dy)
        blocked = False
        cx, cy = x0 + step_x, y0 + step_y

        while (cx, cy) != (x1, y1):
            current_pos = coord_to_pos(cx, cy)
            if current_pos in own_positions or current_pos in enemy_positions:
                blocked = True
                break
            cx += step_x
            cy += step_y

        if not blocked:
            if move not in own_positions:
                valid_moves.append(move)

    return valid_moves

def validate_moves_no_check(char, pos, moves, color):
    safe_moves = []

    # Determine the current player and enemy player objects
    current_player = player1 if color == "white" else player2
    enemy_player = player1 if color == "black" else player2

    # Find the index of the piece being moved
    piece_type = pic[char.upper()]
    piece_idx = -1
    for idx, detail in enumerate(current_player.characters[piece_type]["detail"]):
        if detail["position"] == pos and detail["alive"] and (piece_map[piece_type] == char.upper() if color == "white" else piece_map[piece_type].lower() == char.lower()):
            piece_idx = idx
            break

    if piece_idx == -1:
        return [] # Should not happen if `pos` is a valid piece position

    original_pos = current_player.characters[piece_type]["detail"][piece_idx]["position"]

    for move in moves:
        # Simulate the move

        # 1. Store original state of board and piece
        original_king_pos = current_player.characters["king"]["detail"][0]["position"]

        captured_piece_info = None

        # Check if the move is a capture
        for t, data in enemy_player.characters.items():
            for i, detail in enumerate(data["detail"]):
                if detail["alive"] and detail["position"] == move:
                    captured_piece_info = (t, i, detail["alive"])
                    detail["alive"] = False # Temporarily "capture" the piece
                    break
            if captured_piece_info:
                break

        # Move the current piece to the new position
        current_player.characters[piece_type]["detail"][piece_idx]["position"] = move

        # 2. Update packed squares with the simulated move
        ckcpcn()  

        # 3. Get all moves of the enemy pieces after the simulated move
        temp_enemy_attacking_moves = []
        for e_piece_type, e_piece_data in enemy_player.characters.items():
            for e_piece_detail in e_piece_data["detail"]:
                if e_piece_detail["alive"]:
                    e_char = piece_map[e_piece_type]
                    if enemy_player.color == "black":
                        e_char = e_char.lower()

                    # Get raw moves for enemy piece
                    raw_enemy_moves = get_moves(e_char, e_piece_detail["position"], enemy_player.color)

                    # Filter blocked moves for enemy piece (this is crucial for accurate check detection)
                    filtered_enemy_moves = filter_blocked_moves(e_char, e_piece_detail["position"], raw_enemy_moves, enemy_player.color)
                    temp_enemy_attacking_moves.extend(filtered_enemy_moves)

        # 4. Check if the king is in check after the simulated move
        king_current_pos_after_move = current_player.characters["king"]["detail"][0]["position"]

        if king_current_pos_after_move not in temp_enemy_attacking_moves:
            safe_moves.append(move)

        # 5. Revert the simulated move to restore the board state
        current_player.characters[piece_type]["detail"][piece_idx]["position"] = original_pos
        if captured_piece_info:
            captured_type, captured_idx, original_alive_status = captured_piece_info
            enemy_player.characters[captured_type]["detail"][captured_idx]["alive"] = original_alive_status

        # Restore packed squares to original state
        ckcpcn()  

    return safe_moves

def update_all_moves():
    """Update possible moves for all pieces without recursion"""
    ckcpcn()  # Update packed squares first

    # First pass: calculate all raw moves without check validation
    for player_obj in [player1, player2]:
        for piece_type, piece_data in player_obj.characters.items():
            for piece_detail in piece_data["detail"]:
                if piece_detail["alive"]:
                    char = piece_map[piece_type]
                    if player_obj.color == "black":
                        char = char.lower()
                    raw_moves = get_moves(char, piece_detail["position"],
                                          player_obj.color)
                    piece_detail["moves"] = raw_moves

    # Second pass: filter moves that are blocked by other pieces
    for player_obj in [player1, player2]:
        for piece_type, piece_data in player_obj.characters.items():
            for piece_detail in piece_data["detail"]:
                if piece_detail["alive"]:
                    char = piece_map[piece_type]
                    if player_obj.color == "black":
                        char = char.lower()
                    piece_detail["moves"] = filter_blocked_moves(
                        char, piece_detail["position"], piece_detail["moves"],
                        player_obj.color)

    # Third pass: validate moves that don't put king in check
    for player_obj in [player1, player2]:
        for piece_type, piece_data in player_obj.characters.items():
            for piece_detail in piece_data["detail"]:
                if piece_detail["alive"]:
                    char = piece_map[piece_type]
                    if player_obj.color == "black":
                        char = char.lower()
                    piece_detail["moves"] = validate_moves_no_check(
                        char, piece_detail["position"], piece_detail["moves"],
                        player_obj.color)

def is_checkmate(player_obj):
    if player_obj.color == "white":
        return True if not list(itertools.chain.from_iterable(packedmvsqr["white"])) else False
    else:
        return True if not list(itertools.chain.from_iterable(packedmvsqr["black"])) else False

def chgpwn(player_obj):
    for piece_detail in player_obj.characters["pawn"]["detail"]:
        if piece_detail["alive"]:
            if player_obj.color == "white" and piece_detail["position"][1] == '8':
                pice = input("choose a piece to promote to (Q, R, B, N): ")
                while pice not in ["Q", "R", "B", "N"]:
                    pice = input("Invalid piece! choose a piece to promote to (Q, R, B, N): ")
                piece_detail["alive"] = False

                new_piece_type = ""
                new_piece_char = ""
                if pice == "Q":
                    new_piece_type = "queen"
                    new_piece_char = "Q" # Uppercase for white pieces
                elif pice == "R":
                    new_piece_type = "rook"
                    new_piece_char = "R"
                elif pice == "B":
                    new_piece_type = "bishop"
                    new_piece_char = "B"
                elif pice == "N":
                    new_piece_type = "knight"
                    new_piece_char = "N"

                player_obj.characters[new_piece_type]["detail"].append({
                    "alive": True,
                    "position": piece_detail["position"],
                    "moves": []
                })
                player_obj.characters[new_piece_type]["no"] += 1

                # Load the new piece image and add it to original_pcs
                new_img = pygame.image.load(f"white player/{new_piece_type}.png")
                original_pcs[new_piece_char].append(new_img)


            elif player_obj.color == "black" and piece_detail["position"][1] == '1':
                pice = input("choose a piece to promote to (q, r, b, n): ")
                while pice not in ["q", "r", "b", "n"]:
                    pice = input("Invalid piece! choose a piece to promote to (q, r, b, n): ")
                piece_detail["alive"] = False

                new_piece_type = ""
                new_piece_char = ""
                if pice == "q":
                    new_piece_type = "queen"
                    new_piece_char = "q" # Lowercase for black pieces
                elif pice == "r":
                    new_piece_type = "rook"
                    new_piece_char = "r"
                elif pice == "b":
                    new_piece_type = "bishop"
                    new_piece_char = "b"
                elif pice == "n":
                    new_piece_type = "knight"
                    new_piece_char = "n"

                player_obj.characters[new_piece_type]["detail"].append({
                    "alive": True,
                    "position": piece_detail["position"],
                    "moves": []
                })
                player_obj.characters[new_piece_type]["no"] += 1

                # Load the new piece image and add it to original_pcs
                new_img = pygame.image.load(f"black player/{new_piece_type}.png")
                original_pcs[new_piece_char].append(new_img)