import magiccube
import dictionaries as dict

# Finds the corner sequence
def solve_corners(cube):
    # list of answer letters
    return_letters = []
    visited_positions = {}
    solved = False
    corner_turned = False
    # initialize position, piece, and significant side
    starting_position = (0,2,0)
    current_position = starting_position
    significant_pos = "horizontal"


    # while not solved keep looking
    while not solved:
        current_piece = cube.get_piece(current_position)
        return_letters.append(convert_piece_to_letter(current_piece, significant_pos))
        print(f"\nPOSITION: {current_position}, LETTERS: {return_letters}")
        #if current_position in visited_positions:
            #raise RuntimeError("current_position is in visited positions line 21")
        visit(visited_positions, current_position)
        # check if done or unsolved pieces present
        if convert_piece_to_letter(current_piece, significant_pos) in ("A", "R"):
            del return_letters[-1]
            unsolved_piece = find_unsolved_piece(cube, visited_positions)
            if unsolved_piece is None:
                solved = True
                break
            else: 
                current_position = unsolved_piece
                significant_pos = find_significant_pos(current_piece, "horizontal")
        elif return_letters[-1] == "E":
            del return_letters[-1]
            # delete last 'E' letter
            unsolved_piece = find_unsolved_piece(cube, visited_positions)
            if unsolved_piece is None:
                solved = True
                break
            else: 
                current_position = unsolved_piece
                significant_pos = find_significant_pos(current_piece, "horizontal")
        elif return_letters[-1] in ("R", "A"):
            del return_letters[-1]
            corner_turned = True
            unsolved_piece = find_unsolved_piece(cube, visited_positions)
            if unsolved_piece is None:
                solved = True
                break
                raise RuntimeError("Unsolved piece is None on line 31")
            else:
                current_position = unsolved_piece
                significant_pos = find_significant_pos(current_piece, "horizontal")
            solved = False
        # get next piece location, piece, and significant side data
        elif visited_positions[current_position] == 2:
            unsolved_piece = find_unsolved_piece(cube, visited_positions)
            if unsolved_piece is None:
                solved = True
                break
                raise RuntimeError("Unsolved piece is None on line 45")
            else:
                current_position = unsolved_piece
                significant_pos = find_significant_pos(current_piece, "horizontal")
            solved = False
        else:
            current_position = find_next_position(current_piece)
            significant_pos = find_significant_pos(current_piece, significant_pos)

        
    return return_letters


def visit(visited, position):
    if position in visited:
        visited[position] += 1
    else:
        visited[position] = 1


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

def find_unsolved_piece(cube, visited_positions):
    #unsolved_piece_found = False
    unseen_corners = [x for x in dict.corner_position_list if x not in visited_positions]
    for corner in unseen_corners:
        current_position = corner
        current_piece = cube.get_piece(current_position)
        if current_piece is None:
            continue
        desired_position = dict.corner_piece_to_position[str(current_piece)]
        if current_position != desired_position:
            #unsolved_piece_found = True
            unsolved_piece_position = current_position
            return unsolved_piece_position
    return None    