# The actual game with all classes needed imported.
# This holds the function needed to solve the game
# as well displays the actions with each move in it.

import Rod
import Stack
import copy
import Blocks


class TOH:

    # Creates a constructor that makes 1 full rod and 2 empty rods.
    # It places them all into a list.
    def __init__(self):
        self.rod1 = Rod.Rod(True)
        self.rod2 = Rod.Rod()
        self.rod3 = Rod.Rod()
        self.towers = [self.rod1, self.rod2, self.rod3]

    # This is the function that solves the game an has a few base cases.
    def solve(self, n=0, startRod=0, extraRod=1, endRod=2):
        # This checks to see if the last tower is complete.
        if self.towers[2].isComplete():
            print(self)
            return
        elif n == 1:  # Checks to see if the block is the last 1 in the rod.
            startRod.blockMove(endRod)
            print(self)
            return
        else:
            # Recalls the function.
            self.solve(n - 1, startRod, endRod, extraRod)
            startRod.blockMove(endRod)  # Moves the block onto the last rod.
            print(self)
            # This works its way back to make sure everything is solved correctly.
            self.solve(n - 1, extraRod, startRod, endRod)

    # Defines a way to print the object by calling it.
    def __str__(self):
        return str(self.towers[0]) + "  " + str(self.towers[1]) + "  " + str(self.towers[2]) + "\n------------------"


towers = TOH()
print(towers)
towers.solve(3, towers.towers[0], towers.towers[1], towers.towers[2])
print(towers)
