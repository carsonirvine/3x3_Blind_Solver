import magiccube
from scramble import Scramble
import dictionaries as dict
import corners
import edges
class Blind_Solver():
    def __init__(self, mode):
        self.mode = mode
    
    def solve(self):
        cube = magiccube.Cube(3,"WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY")

        # generate a scramble object from the move alphabet and  normal length
        scramble = Scramble(20, dict.moves)
        # print the scramble
        print(f"Scramble: {scramble.scramble}")
        # scramble the cube
        cube.rotate(scramble.scramble)
        # print the current state of the cube for reference
        print(cube)

        # calculate the edge sequence
        edge_sequence = edges.solve_edges(cube)
        # calculate the corner sequence
        corner_sequence = corners.solve_corners(cube)
        # Is the parity algorithm required
        parity = False

        # output results
        if self.mode == "edges" or self.mode == "both":
            print(f"EDGE SEQUENCE:\n {edge_sequence}")
            # if odd number of edge and corner moves the parity algorithm is required
            if len(edge_sequence) % 2 != 0:
                parity = True
                print("\nPARITY Ra PERM REQUIRED")
        if self.mode == "corners" or self.mode == "both":
            print(f"\nCORNER SEQUENCE:\n {corner_sequence}")

        # Solves the edges
        if self.mode == "edges" or self.mode == "both":
            for edge in edge_sequence:
                cube.rotate(dict.edge_setup_moves[edge])
                cube.rotate(dict.algorithms["edge_swap"])
                cube.rotate(dict.edge_unsetup_moves[edge])

        # if the parity algorithm is required
        if self.mode == "both":
            if parity:
                cube.rotate(dict.algorithms["parity"])

        # Solves the corners
        if self.mode == "corners" or self.mode == "both":
            for corner in corner_sequence:
                cube.rotate(dict.corner_setup_moves[corner])
                cube.rotate(dict.algorithms["corner_swap"])
                cube.rotate(dict.corner_unsetup_moves[corner])