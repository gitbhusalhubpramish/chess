import os
import pygame
import platform
import itertools
from boad import draw_board, player1, player2, whtrsz, blkrsz, dcrzall, rsz, pcs, pic, piece_map, piece_position_map, square_size, drawpcs, ckcpcn, get_moves, packedsqr, ckcmv, packedmvsqr, filter_blocked_moves
import copy
import chess

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

def validate_moves_no_check(char, pos, moves, color):
    """
    Filters a list of moves for a given piece, returning only those moves that
    do not result in the player's own king being in check.

    Args:
        char (str): The character representing the piece (e.g., 'K', 'q').
        pos (str): The current position of the piece (e.g., 'e2').
        moves (list): A list of potential moves for the piece.
        color (str): The color of the player ('white' or 'black').

    Returns:
        list: A new list containing only the moves that do not put the king in check.
    """
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
    king_pos = player_obj.characters["king"]["detail"][0]["position"]
    enemy_color = "white" if player_obj.color == "black" else "black"
    enemy_player = player1 if enemy_color == "white" else player2

    # First, check if king is in check
    all_enemy_moves = []
    for piece_type, piece_data in enemy_player.characters.items():
        for piece_detail in piece_data["detail"]:
            if piece_detail["alive"]:
                e_char = piece_map[piece_type]
                if enemy_color == "black":
                    e_char = e_char.lower()
                raw = get_moves(e_char, piece_detail["position"], enemy_color)
                all_enemy_moves += filter_blocked_moves(
                    e_char, piece_detail["position"], raw, enemy_color)

    if king_pos not in all_enemy_moves:
        return False

    # Try every possible move of all own pieces
    for piece_type, piece_data in player_obj.characters.items():
        for idx, piece_detail in enumerate(piece_data["detail"]):
            if not piece_detail["alive"]:
                continue

            orig_pos = piece_detail["position"]
            char = piece_map[piece_type]
            if player_obj.color == "black":
                char = char.lower()

            raw_moves = get_moves(char, orig_pos, player_obj.color)
            legal_moves = filter_blocked_moves(char, orig_pos, raw_moves,
                                               player_obj.color)
            legal_moves = validate_moves_no_check(char, orig_pos, legal_moves,
                                                  player_obj.color)

            for move in legal_moves:
                # Simulate the move
                captured = None
                captured_type = None
                captured_idx = None

                # Temporarily capture enemy
                for t, data in enemy_player.characters.items():
                    for i, detail in enumerate(data["detail"]):
                        if detail["alive"] and detail["position"] == move:
                            captured = detail
                            captured_type = t
                            captured_idx = i
                            detail["alive"] = False
                            break

                # Move temporarily
                piece_detail["position"] = move

                # Re-check for king threat
                temp_enemy_moves = []
                king_temp_pos = player_obj.characters["king"]["detail"][0][
                    "position"]
                for t, d in enemy_player.characters.items():
                    for det in d["detail"]:
                        if det["alive"]:
                            ch = piece_map[t]
                            if enemy_color == "black":
                                ch = ch.lower()
                            r = get_moves(ch, det["position"], enemy_color)
                            temp_enemy_moves += filter_blocked_moves(
                                ch, det["position"], r, enemy_color)

                # Restore
                piece_detail["position"] = orig_pos
                if captured:
                    captured["alive"] = True

                if king_temp_pos not in temp_enemy_moves:
                    return False

    # No legal moves found that escape check
    return True


psblmv = []
raw_moves = []
clock = pygame.time.Clock()
running = True
Selected = None
wt = True
nextmv = None

ckcmv()

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
