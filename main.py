import os
import pygame
import platform
from moves import coord_to_pos, pos_to_coord
import itertools
from boad import draw_board, player1, player2, whtrsz, blkrsz, dcrzall, rsz, pcs, pic, piece_map, piece_position_map, square_size, drawpcs, ckcpcn, get_moves, packedsqr

if platform.system() == "Linux":
    os.environ["SDL_VIDEODRIVER"] = "x11"
pygame.init()

WINDOW_SIZE = (560, 560)
screen = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)
pygame.display.set_caption("Chess")

whtrsz(70)
blkrsz(70)

for player_obj in [player1, player2]:
    for piece_type, piece_data in player_obj.characters.items():
        for piece_detail in piece_data["detail"]:
            piece_detail["moves"] = get_moves(piece_type[0].upper(),
                                              piece_detail["position"],
                                              player_obj.color)

packedmv = []
packedmvsqr = {"white": [], "black": []}


def king_check(col):
    if col == "white":
        return player1.characters["king"]["detail"][0]["position"] in list(
            itertools.chain.from_iterable(packedmvsqr['black']))
    elif col == "black":
        return player2.characters["king"]["detail"][0]["position"] in list(
            itertools.chain.from_iterable(packedmvsqr['white']))


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
    """Validate moves that don't put king in check (without recursion)"""
    if char.upper() == "K":
        return moves  # King moves are handled specially

    valid_moves = []
    piece_type = pic[char.upper()]
    player = player1 if color == "white" else player2

    # Find the piece index
    piece_idx = None
    for i, piece in enumerate(player.characters[piece_type]["detail"]):
        if piece["position"] == pos and piece["alive"]:
            piece_idx = i
            break

    if piece_idx is None:
        return []

    original_pos = player.characters[piece_type]["detail"][piece_idx][
        "position"]

    for move in moves:
        # Temporarily make the move
        player.characters[piece_type]["detail"][piece_idx]["position"] = move

        # Check if king is in check using current state (no recursive update)
        king_pos = player.characters["king"]["detail"][0]["position"]
        in_check = False

        # Check all enemy pieces' current moves (without updating)
        enemy_color = "black" if color == "white" else "white"
        enemy_player = player2 if enemy_color == "black" else player1

        for e_piece_type, e_piece_data in enemy_player.characters.items():
            for e_piece_detail in e_piece_data["detail"]:
                if e_piece_detail["alive"]:
                    e_char = piece_map[e_piece_type]
                    if enemy_color == "black":
                        e_char = e_char.lower()
                    e_moves = get_moves(e_char, e_piece_detail["position"],
                                        enemy_color)
                    e_moves = filter_blocked_moves(e_char,
                                                   e_piece_detail["position"],
                                                   e_moves, enemy_color)
                    if king_pos in e_moves:
                        in_check = True
                        break
            if in_check:
                break

        if not in_check:
            valid_moves.append(move)

        # Undo the move
        player.characters[piece_type]["detail"][piece_idx][
            "position"] = original_pos

    return valid_moves


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


update_all_moves()


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
                    for other_type, other_data in enemy_player.characters.items(
                    ):
                        for other_idx, other_piece in enumerate(
                                other_data["detail"]):
                            if other_piece["alive"] and other_piece[
                                    "position"] == move:
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

                    new_king_pos = player_obj.characters["king"]["detail"][0][
                        "position"]
                    new_enemy_moves = []
                    for enemy_piece_type, enemy_piece_data in enemy_player.characters.items(
                    ):
                        for enemy_piece_detail in enemy_piece_data["detail"]:
                            if enemy_piece_detail["alive"]:
                                new_enemy_moves.extend(
                                    enemy_piece_detail["moves"])

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


while running:
    draw_board((255, 255, 255), 8, 8, 70, (150, 75, 0))
    drawpcs()
    update_all_moves()

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

            if Selected and square in Selected[
                    2]:  # Selected[2] contains the moves
                # Move the piece
                moved_char, moved_idx, _ = Selected
                piece_type = pic[moved_char.upper()]

                # Handle capturing
                if square in piece_position_map:
                    captured_char, captured_idx = piece_position_map[square]
                    captured_type = pic[captured_char.upper()]
                    if captured_char.isupper():
                        player1.characters[captured_type]["detail"][
                            captured_idx]["alive"] = False
                    else:
                        player2.characters[captured_type]["detail"][
                            captured_idx]["alive"] = False

                # Update position
                if moved_char.isupper():
                    player1.characters[piece_type]["detail"][moved_idx][
                        "position"] = square
                else:
                    player2.characters[piece_type]["detail"][moved_idx][
                        "position"] = square

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
                player1.characters["king"]["check"] = False
                player2.characters["king"]["check"] = False
                player1.characters["king"]["checkmate"] = False
                player2.characters["king"]["checkmate"] = False

                if player1.characters['king']['detail'][0]['position'] in list(
                        itertools.chain.from_iterable(packedmvsqr['black'])):
                    print("Check white")
                    player1.characters["king"]["check"] = True
                    if is_checkmate(player1):
                        print("Checkmate! Black wins!")
                        player1.characters["king"]["checkmate"] = True
                        running = False
                elif player2.characters['king']['detail'][0][
                        'position'] in list(
                            itertools.chain.from_iterable(
                                packedmvsqr['white'])):
                    print("Check black")
                    player2.characters["king"]["check"] = True
                    if is_checkmate(player2):
                        print("Checkmate! White wins!")
                        player2.characters["king"]["checkmate"] = True
                        running = False

            elif square in piece_position_map:
                char, idx = piece_position_map[square]
                # Check if it's the correct player's turn
                if (wt and char.isupper()) or (not wt and char.islower()):
                    piece_type = pic[char.upper()]
                    if char.isupper():
                        moves = player1.characters[piece_type]["detail"][idx][
                            "moves"]
                    else:
                        moves = player2.characters[piece_type]["detail"][idx][
                            "moves"]
                    Selected = (char, idx, moves)
            else:
                Selected = None

    # Highlight possible moves
    if Selected is not None:
        for move in Selected[2]:
            col = ord(move[0]) - ord('a')
            row = 8 - int(move[1])
            center = (col * square_size + square_size // 2,
                      row * square_size + square_size // 2)
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
