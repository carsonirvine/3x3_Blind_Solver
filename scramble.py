import sys
sys.path.append("C:/Users/Carson/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0/LocalCache/local-packages/Python313/site-packages/")

import magiccube
import random

class Scramble:


    def __init__(self, length, moves):
        self.length = length
        self.moves = moves
        self.scramble = self.generate_scramble()
    
    def generate_scramble(self): # generates and returns a scramble
        scramble_string= ""
        move_num = random.randrange(0,17)
        scramble_string = scramble_string + " " + self.moves[move_num]
        for x in range(self.length-1):
            next_move = self.pick_move_num(move_num)
            scramble_string = scramble_string + " " + self.moves[next_move]
            move_num = next_move
        return scramble_string

    def pick_move_num(self, previous_move): # based on last move chooses next move. Cant have two parallel moves in a row
        if previous_move > 11:
            return random.randrange(0,11)
        elif previous_move > 5:
            temp_random = random.randrange(0,1)
            if temp_random == 1:
                return random.randrange(12, 17)
            else:
                return random.randrange(0,5)
        else:
            return random.randrange(6,17)

    