import magiccube
from magiccube import BasicSolver
import random
from scramble import Scramble
import printing
import dictionaries as dict
import corners

moves = ["R","R'","R2","L","L'","L2","U","U'","U2","D","D'","D2","F","F'","F2","B","B'","B2"]

cube = magiccube.Cube(3,"WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY")

solver = BasicSolver(cube)



edge_piece_locations = {
    "OY": "G",
    "YO": "X"
}



scramble = Scramble(20, moves)
print(f"Scramble: {scramble.scramble}")


#printing.print_all_pieces(cube)
#print(cube)

cube.rotate(scramble.scramble)
#print("\nSCRAMBLING\n")
print(cube)
#printing.print_all_pieces(cube)






corner_sequence = corners.solve_corners(cube)

print(f"\n\nCORNER SEQUENCE\n\n {corner_sequence}")

#piece = cube.get_piece((2,2,2))
#print(piece)