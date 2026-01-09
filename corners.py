import magiccube
import dictionaries as dict

# Finds the corner sequence
def solve_corners(cube):
    solved = False
    parity = False
    # initialize position, piece, and significant side
    current_x = 0
    current_y = 2
    current_z = 0
    current_position = (current_x, current_y, current_z)
    current_piece = cube.get_piece(current_position)
    significant_pos = "horizontal"
    return_letters = []

    return_letters.append(convert_piece_to_letter(current_piece, significant_pos))

    # while not solved keep looking
    while not solved:
        # get next piece location, piece, and significant side data
        current_position = find_next_position(current_piece)
        significant_pos = find_significant_pos(current_piece, significant_pos)
        current_piece = cube.get_piece(current_position)
        return_letters.append(convert_piece_to_letter(current_piece, significant_pos))

        # check if done or unsolved pieces present
        if return_letters[-1] in ("E"):
            solved = True
            print("\nSUCCESS\n")
            # delete last 'E' letter
            del return_letters[-1]
            break
        # unsolved pieces present
        elif return_letters[-1] in ("A", "R"):
            parity = True
            solved = True
            print("UNSOLVED PIECE PRESENT")
            break

    return return_letters

# significant_pos can be "vertical" for top and bottom, "horizontal" for left and right
# and "through" for front and back

# Takes in a piece and side and finds its matching letter
def convert_piece_to_letter(piece, significant_pos):
    # take in piece colors by side
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

    # search dict for matching letter
    letter = dict.corner_piece_to_letter[piece_colors]
    return letter

# returns the position for the next piece
def find_next_position(current_piece):
    home_position = dict.corner_piece_to_position[str(current_piece)]
    return home_position

# checks based on the colour of the piece and significant side
# what the next significant side will be
def find_significant_pos(current_piece, significant_pos):
    next_pos = ""
    color = ""
    # find relevant color
    if significant_pos == "vertical":
        color = str(current_piece)[1]
    elif significant_pos == "horizontal":
        color = str(current_piece)[0]
    elif significant_pos == "through":
        color = str(current_piece)[2]

    # find side from color
    if color == "R" or color == "O":
        next_pos = "horizontal"
    elif color == "W" or color == "Y":
        next_pos = "vertical"
    elif color == "B" or color == "G":
        next_pos = "through"
    return next_pos

# finds next position to check through each corner
def next_corner_position(current_position):
    x,y,z = current_position
    if current_position[2] == 0:
        z = 2
    elif current_position[1] == 0 and current_position[2] == 2:
        y = 2
        z = 0
    elif current_position[0] == 0 and current_position[1] == 2 and current_position[2] == 2: 
        x = 2
        y = 0
        z = 0
    else:
        x = 2
        y = 2
        z = 2
    return (x,y,z)
