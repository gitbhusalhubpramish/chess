class player:
  color = ""
  characters = {
    "king": {
      "no":1,
      "position": None
    },
    "queen": {
      "no":1,
      "position": None
    },
    "rook": {
      "no":2,      
      "detail": {        
        "rook1":{
          "alive": True,
          "position": None
        },
        "rook2": {
          "alive": True,
          "position": None
        },
      }  
    },
    "bishop": {
      "no":2,
      "bishop1":{
        "alive": True,
        "position": None
      },
      "bishop2": {
        "alive": True,
        "position": None
      }
    },
    "knight": {
      "no":2,
      "detail":{
        "knight1":{
        "alive": True,
        "position": None
      },
      "knight2":{
        "alive": True,
        "position": None
      }
      }
    },
    "pawn": {
      "no":8,
      "detail":
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
    else:
      self.characters["king"]["position"] = "e8"
      self.characters["queen"]["position"] = "d8"
      self.characters["rook"]["position"] = ["a8", "h8"]
      self.characters["bishop"]["position"] = ["c8", "f8"]
      self.characters["knight"]["position"] = ["b8", "g8"]
      self.characters["pawn"]["position"] = ["a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7"]