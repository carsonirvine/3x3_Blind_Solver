import magiccube
from magiccube import BasicSolver
import random
from scramble import Scramble
import printing

moves = ["R","R'","R2","L","L'","L2","U","U'","U2","D","D'","D2","F","F'","F2","B","B'","B2"]

cube = magiccube.Cube(3,"WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY")

solver = BasicSolver(cube)

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

edge_piece_locations = {
    "OY": "G",
    "YO": "X"
}



scramble = Scramble(20, moves)
print(scramble.scramble)


printing.print_all_pieces(cube)
print(cube)

cube.rotate(scramble.scramble)
print("\nSCRAMBLING\n")
print(cube)
printing.print_all_pieces(cube)




def solve_corners(cube):
    solved = False
    current_x = 2
    current_y = 2
    current_z = 0
    current_position = (current_x, current_y, current_z)
    current_piece = cube.get_piece(current_position)
    significant_pos = "vertical"
    return_letters = ""

    return_letters += (convert_piece_to_letter(current_piece, current_position, significant_pos))

    while not solved:
        '''
        next_position = find_next_position(current_piece)
        next_significant_pos = find_significant_pos(current_piece, significant_pos)
        next_piece = cube.get_piece(next_position)
        '''
        current_position = find_next_position(current_piece)
        significant_pos = find_significant_pos(current_piece, significant_pos)
        current_piece = cube.get_piece(current_position)
        return_letters += (convert_piece_to_letter(current_piece, current_position, significant_pos))
        if return_letters[-1] == "B" or return_letters[-1] == "N" or return_letters[-1] == "Q":
            solved = True
            break
    return return_letters

# significant_pos can be "vertical" for top and bottom, "horizontal" for left and right
# and "through" for front and back
def convert_piece_to_letter(piece, position, significant_pos):
    x_color = str(piece)[0]
    y_color = str(piece)[1]
    z_color = str(piece)[2]

    piece_colors = ""

    if significant_pos == "vertical":
        piece_colors+=y_color
        piece_colors+=x_color
        piece_colors+=z_color
        
    elif significant_pos == "horizontal":
        piece_colors+=x_color
        piece_colors+=y_color
        piece_colors+=z_color
    
    elif significant_pos == "through":
        piece_colors+=z_color
        piece_colors+=x_color
        piece_colors+=y_color

    letter = corner_piece_to_letter[piece_colors]
    return letter

def find_next_position(current_piece):
    home_position = corner_piece_to_position[str(current_piece)]
    return home_position

def find_significant_pos(current_piece, significant_pos):
    next_pos = ""
    color = ""
    if significant_pos == "vertical":
        color = str(current_piece)[1]
    elif significant_pos == "horizontal":
        color = str(current_piece)[0]
    elif significant_pos == "through":
        color = str(current_piece)[2]

    if color == "R" or color == "O":
        next_pos = "horizontal"
    elif color == "W" or color == "Y":
        next_pos = "vertical"
    elif color == "B" or color == "G":
        next_pos = "through"
    return next_pos


corner_sequence = solve_corners(cube)

print(f"\n\nCORNER SEQUENCE\n\n {corner_sequence}")

#piece = cube.get_piece((2,2,2))
#print(piece)