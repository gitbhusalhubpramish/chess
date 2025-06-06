class player:
    def __init__(self, color, king, queen, rook, bishop, knight, pawn):
        self.color = color
        self.characters = {
            "king": {
                "check" : False,
                "checkmate" : False,
                "no": 1,
                "detail": [{
                    "alive": True,
                    "position": "e1" if color == "white" else "e8",
                    "moves": []
                }]
            },
            "queen": {
                "no": 1,
                "detail": [{
                    "alive": True,
                    "position": "d1" if color == "white" else "d8",
                    "moves": []
                }]
            },
            "rook": {
                "no": 2,
                "detail": [
                    {
                        "alive": True,
                        "position": "a1" if color == "white" else "a8",
                        "moves": []
                    },
                    {
                        "alive": True,
                        "position": "h1" if color == "white" else "h8",
                        "moves": []
                    }
                ]
            },
            "bishop": {
                "no": 2,
                "detail": [
                    {
                        "alive": True,
                        "position": "c1" if color == "white" else "c8",
                        "moves": []
                    },
                    {
                        "alive": True,
                        "position": "f1" if color == "white" else "f8",
                        "moves": []
                    }
                ]
            },
            "knight": {
                "no": 2,
                "detail": [
                    {
                        "alive": True,
                        "position": "b1" if color == "white" else "b8",
                        "moves": []
                    },
                    {
                        "alive": True,
                        "position": "g1" if color == "white" else "g8",
                        "moves": []
                    }
                ]
            },
            "pawn": {
                "no": 8,
                "detail": [
                    {
                        "alive": True,
                        "position": "a2" if color == "white" else "a7",
                        "moves": []
                    },
                    {
                        "alive": True,
                        "position": "b2" if color == "white" else "b7",
                        "moves": []
                    },
                    {
                        "alive": True,
                        "position": "c2" if color == "white" else "c7",
                        "moves": []
                    },
                    {
                        "alive": True,
                        "position": "d2" if color == "white" else "d7",
                        "moves": []
                    },
                    {
                        "alive": True,
                        "position": "e2" if color == "white" else "e7",
                        "moves": []
                    },
                    {
                        "alive": True,
                        "position": "f2" if color == "white" else "f7",
                        "moves": []
                    },
                    {
                        "alive": True,
                        "position": "g2" if color == "white" else "g7",
                        "moves": []
                    },
                    {
                        "alive": True,
                        "position": "h2" if color == "white" else "h7",
                        "moves": []
                    }
                ]
            }
        }
        self.charactersdata = {
            "king": king,
            "queen": queen,
            "rook": rook,
            "bishop": bishop,
            "knight": knight,
            "pawn": pawn
        }