class player:
  color = ""
  characters = {
    "king": {
      "no":1,
      "posotion": None
    },
    "queen": {
      "no":1,
      "posotion": None
    },
    "rook": {
      "no":2,
      "posotion": None
    },
    "bishop": {
      "no":2,
      "posotion": None
    },
    "knight": {
      "no":2,
      "posotion": None
    },
    "pawn": {
      "no":8,
      "posotion": None
    }
  }
  def __init__(self, color, name):
    self.color = color
    if color == "white":
      self.characters["king"]["position"] = "e1"
      self.characters["queen"]["position"] = "d1"
      self.characters["rook"]["position"] = ["a1", "h1"]
      self.characters["bishop"]["position"] = ["c1", "f1"]
      self.characters["knight"]["position"] = ["b1", "g1"]
      self.characters["pawn"]["position"] = ["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2"]