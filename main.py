import os
import pygame
import platform
import itertools
from boad import draw_board, player1, player2, whtrsz, blkrsz, dcrzall, rsz, pic, piece_position_map, square_size, drawpcs, ckcpcn, get_moves, ckcmv, packedmvsqr, update_all_moves, is_checkmate, chgpwn, packedmvpic
import time

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

psblmv = []
raw_moves = []
clock = pygame.time.Clock()
running = True
Selected = None
wt = True
nextmv = None

ckcmv()
mt = 0

while running:
    draw_board((255, 255, 255), 8, 8, 70, (150, 75, 0))
    drawpcs()
    update_all_moves()
    chgpwn(player1)
    chgpwn(player2)
    if player1.characters["king"]["checkmate"]:
        print("Checkmate! Black wins!")
        mt += 1
    elif player2.characters["king"]["checkmate"]:
        print("Checkmate! White wins!")
        mt += 1
    if mt == 2:
        time.sleep(10)
        running = False

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
                current_player_obj = player1 if moved_char.isupper(
                ) else player2
                is_castling = current_player_obj.castling
                if piece_type == "king":
                    start_king_pos = current_player_obj.characters["king"][
                        "detail"][moved_idx]["position"]
                    if abs(ord(square[0]) - ord(start_king_pos[0])
                           ) == 2:  # King moved two squares horizontally
                        is_castling = True
                        if square[0] == 'g':  # Kingside castling
                            rook_original_pos = "h1" if current_player_obj.color == "white" else "h8"
                            rook_target_pos = "f1" if current_player_obj.color == "white" else "f8"
                            rook_idx = 1  # Index for the h1 rook
                        elif square[0] == 'c':  # Queenside castling
                            rook_original_pos = "a1" if current_player_obj.color == "white" else "a8"
                            rook_target_pos = "d1" if current_player_obj.color == "white" else "d8"
                            rook_idx = 0  # Index for the a1 rook

                        # Move the rook
                        if current_player_obj.characters["rook"]["detail"][
                                rook_idx][
                                    "alive"]:  # Ensure rook is still alive
                            current_player_obj.characters["rook"]["detail"][
                                rook_idx]["position"] = rook_target_pos
                            current_player_obj.characters["rook"]["detail"][
                                rook_idx]["moved"] = True
                            print(
                                f"Castling! {current_player_obj.color} rook moved to {rook_target_pos}"
                            )
                        current_player_obj.characters[piece_type]["detail"][
                            moved_idx]["position"] = square
                        if piece_type in [
                                "rook", "king"
                        ]:  # Set moved for both king and rook after castling
                            current_player_obj.characters[piece_type][
                                "detail"][moved_idx]["moved"] = True

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
                    if piece_type in ["rook", "king"]:
                        player1.characters[piece_type]["detail"][moved_idx][
                            "moved"] = True
                else:
                    player2.characters[piece_type]["detail"][moved_idx][
                        "position"] = square
                    if piece_type in ["rook", "king"]:
                        player1.characters[piece_type]["detail"][moved_idx][
                            "moved"] = True

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
                    print(f"Check white valid move {packedmvpic['white']}")
                    player1.characters["king"]["check"] = True
                    if is_checkmate(player1):
                        print("Checkmate! Black wins!")
                        player1.characters["king"]["checkmate"] = True
                elif player2.characters['king']['detail'][0][
                        'position'] in list(
                            itertools.chain.from_iterable(
                                packedmvsqr['white'])):
                    print(f"Check black valid move {packedmvpic['black']}")
                    player2.characters["king"]["check"] = True
                    if is_checkmate(player2):
                        print("Checkmate! White wins!")
                        player2.characters["king"]["checkmate"] = True

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
        rsz(player1 if Selected[0].isupper() else player2,
            pic[Selected[0].upper()], Selected[1], 85)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
