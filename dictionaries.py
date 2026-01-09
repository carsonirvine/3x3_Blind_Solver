corner_piece_to_letter = {
    # O Y B
    "OYB": "H",
    "OBY": "H",
    "YBO": "X",
    "YOB": "X",
    "BOY": "S",
    "BYO": "S",

    # O Y G
    "OYG": "G",
    "OGY": "G",
    "YGO": "U",
    "YOG": "U",
    "GOY": "L",
    "GYO": "L",

    # O W B
    "OWB": "E",
    "OBW": "E",
    "WBO": "A",
    "WOB": "A",
    "BOW": "R",
    "BWO": "R",

    # O W G
    "OWG": "F",
    "OGW": "F",
    "WGO": "D",
    "WOG": "D",
    "GOW": "I",
    "GWO": "I",

    # R Y B
    "RYB": "O",
    "RBY": "O",
    "YBR": "W",
    "YRB": "W",
    "BRY": "T",
    "BYR": "T",

    # R Y G
    "RYG": "P",
    "RGY": "P",
    "YGR": "V",
    "YRG": "V",
    "GRY": "K",
    "GYR": "K",

    # R W B
    "RWB": "N",
    "RBW": "N",
    "WBR": "B",
    "WRB": "B",
    "BRW": "Q",
    "BWR": "Q",

    # R W G
    "RWG": "M",
    "RGW": "M",
    "WGR": "C",
    "WRG": "C",
    "GRW": "J",
    "GWR": "J"
}

letter_to_corner_pieces = {
    "H": ["OYB", "OBY"],
    "X": ["YBO", "YOB"],
    "S": ["BOY", "BYO"],

    "G": ["OYG", "OGY"],
    "U": ["YGO", "YOG"],
    "L": ["GOY", "GYO"],

    "E": ["OWB", "OBW"],
    "A": ["WBO", "WOB"],
    "R": ["BOW", "BWO"],

    "F": ["OWG", "OGW"],
    "D": ["WGO", "WOG"],
    "I": ["GOW", "GWO"],

    "O": ["RYB", "RBY"],
    "W": ["YBR", "YRB"],
    "T": ["BRY", "BYR"],

    "P": ["RYG", "RGY"],
    "V": ["YGR", "YRG"],
    "K": ["GRY", "GYR"],

    "N": ["RWB", "RBW"],
    "B": ["WBR", "WRB"],
    "Q": ["BRW", "BWR"],

    "M": ["RWG", "RGW"],
    "C": ["WGR", "WRG"],
    "J": ["GRW", "GWR"]
}

corner_piece_to_position = {
    # Corner at (0,0,0): OYB
    "OYB": (0,0,0), "OBY": (0,0,0), "YOB": (0,0,0), "YBO": (0,0,0), "BOY": (0,0,0), "BYO": (0,0,0),

    # Corner at (0,0,2): OYG
    "OYG": (0,0,2), "OGY": (0,0,2), "YOG": (0,0,2), "YGO": (0,0,2), "GOY": (0,0,2), "GYO": (0,0,2),

    # Corner at (0,2,0): OWB
    "OWB": (0,2,0), "OBW": (0,2,0), "WOB": (0,2,0), "WBO": (0,2,0), "BOW": (0,2,0), "BWO": (0,2,0),

    # Corner at (0,2,2): OWG
    "OWG": (0,2,2), "OGW": (0,2,2), "WOG": (0,2,2), "WGO": (0,2,2), "GOW": (0,2,2), "GWO": (0,2,2),

    # Corner at (2,0,0): RYB
    "RYB": (2,0,0), "RBY": (2,0,0), "YRB": (2,0,0), "YBR": (2,0,0), "BRY": (2,0,0), "BYR": (2,0,0),

    # Corner at (2,0,2): RYG
    "RYG": (2,0,2), "RGY": (2,0,2), "YRG": (2,0,2), "YGR": (2,0,2), "GRY": (2,0,2), "GYR": (2,0,2),

    # Corner at (2,2,0): RWB
    "RWB": (2,2,0), "RBW": (2,2,0), "WRB": (2,2,0), "WBR": (2,2,0), "BRW": (2,2,0), "BWR": (2,2,0),

    # Corner at (2,2,2): RWG
    "RWG": (2,2,2), "RGW": (2,2,2), "WRG": (2,2,2), "WGR": (2,2,2), "GRW": (2,2,2), "GWR": (2,2,2)
}

corner_position_to_desired_piece = {}
for k, v in corner_piece_to_position.items():
    corner_position_to_desired_piece.setdefault(v, []).append(k)
