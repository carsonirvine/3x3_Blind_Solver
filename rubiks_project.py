import sys
#sys.path.append("C:/Users/Carson/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0/LocalCache/local-packages/Python313/site-packages/")

import magiccube
from magiccube import BasicSolver
import random
from scramble import Scramble


piece_locations = [[[[0 for x in range(6)] for i in range(6)] for y in range(6)] for k in range(24)] # creates the 4d array storing each piece location based on its three face colours


moves = ["R","R'","R2","L","L'","L2","U","U'","U2","D","D'","D2","F","F'","F2","B","B'","B2"]

def print_all_pieces():
    for i in range(3):
        for j in range(3):
            for k in range(3):
                print(i,",",j,",",k,": ", cube.get_piece((i,j,k)), "\n")

'''
For piece coordinates, starting with green front and white top (x,y,z)
first digit X reperesents column from front left to right
second digit z represents row from front bottom to top          
third digit y represents layer from back to front

back bottom left is 0,0,0
core is 1,1,1
top front right is 2,2,2

get_piece returns the piece as a string from position x,y,z.
If x is 0 or 2 the first letter will be what is on either the left or right faces
If x is 1 then there will only be maximum two letters because in the core column

If numbers contains only 0s or 2s its a corner.
If contains one 1 its a edge
If it has multiple 1s its a center piece

'''


cube = magiccube.Cube(3,"WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRBRRRBBBRBBBBBYYYYYYYYY")

solver = BasicSolver(cube)

scramble = Scramble(20, moves)
print(scramble.scramble)





print(cube)
print("Finding RB edge: ", cube.find_piece("RB"))
print("Finding BR edge: ", cube.find_piece("BR"))
print("piece 2,1,0: ", cube.get_piece((2,1,0)))
print(cube)
#print(scramble)
#cube.rotate(scramble)
#print(cube)
'''
print("-1,-1,-1",cube.get_piece((-1,-1,-1)),"\n")
print("-1,-1, 0",cube.get_piece((-1,-1,0)),"\n")
print("-1,-1, 1",cube.get_piece((-1,-1,1)),"\n")
print("-1,-1,-1",cube.get_piece((-1,-1,-1)),"\n")
print("-1, 0,-1",cube.get_piece((-1,0,-1)),"\n")
print("-1, 1,-1",cube.get_piece((-1,1,-1)),"\n")
print("0,0,0",cube.get_piece((0,0,0)),"\n")
print("1,1,1",cube.get_piece((1,1,1)),"\n")
'''

#print_all_pieces()

'''
print("ALL PIECES: ", cube.get_all_pieces())
cube.rotate(scramble)
print("ALL PIECES: ", cube.get_all_pieces())
'''

print("Finding RB edge: ", cube.find_piece("RB"))
print("Finding BR edge: ", cube.find_piece("BR"))
print("piece 2,1,0: ", cube.get_piece((1,0,0)))

