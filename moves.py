def pos_to_coord(pos):
  return ord(pos[0]) - ord('a'), int(pos[1]) - 1

def coord_to_pos(x, y):
  if 0 <= x <= 7 and 0 <= y <= 7:
      return chr(ord('a') + x) + str(y + 1)
  return None

def knight_moves(pos):
  x, y = pos_to_coord(pos)
  candidates = [(x+1, y+2), (x+2, y+1), (x+2, y-1), (x+1, y-2),
                (x-1, y-2), (x-2, y-1), (x-2, y+1), (x-1, y+2)]
  return [coord_to_pos(cx, cy) for cx, cy in candidates if coord_to_pos(cx, cy)]

def king_moves(pos):
  x, y = pos_to_coord(pos)
  candidates = [(x+dx, y+dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if dx != 0 or dy != 0]
  return [coord_to_pos(cx, cy) for cx, cy in candidates if coord_to_pos(cx, cy)]

def rook_moves(pos):
  x, y = pos_to_coord(pos)
  moves = []
  for i in range(1, 8):
      for dx, dy in [(i, 0), (-i, 0), (0, i), (0, -i)]:
          m = coord_to_pos(x + dx, y + dy)
          if m: moves.append(m)
  return moves

def bishop_moves(pos):
  x, y = pos_to_coord(pos)
  moves = []
  for i in range(1, 8):
      for dx, dy in [(i, i), (-i, i), (i, -i), (-i, -i)]:
          m = coord_to_pos(x + dx, y + dy)
          if m: moves.append(m)
  return moves

def queen_moves(pos):
  return rook_moves(pos) + bishop_moves(pos)

def pawn_moves(pos, color):
  x, y = pos_to_coord(pos)
  moves = []
  direction = 1 if color == "white" else -1
  forward = coord_to_pos(x, y + direction)
  if forward: moves.append(forward)
  if (color == "white" and y == 1) or (color == "black" and y == 6):
      double = coord_to_pos(x, y + 2 * direction)
      if double: moves.append(double)
  return moves
