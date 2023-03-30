# This class holds block objects and does much of
# the comparing and moving that is envolved within
# the application. The rods will function as a stack.

import Blocks
import Stack
import copy


class Rod:

    # A constructor that ensures that the correct data is input.
    # It is left as none in case an empty rod is to be created.
    def __init__(self, isStart=None):
        if isStart:  # Checks to see if it exists and creates a full rod.
            self.rod = Stack.Stack()
            self.block1 = Blocks.Block(1)
            self.block2 = Blocks.Block(2)
            self.block3 = Blocks.Block(3)
            self.rod.push(self.block3)
            self.rod.push(self.block2)
            self.rod.push(self.block1)
        else:
            self.rod = Stack.Stack()  # Creates an empty rod.

    # Checks to see if the rod is complete and ensures the order is correct.
    # This returns a boolean value.
    def isComplete(self):
        if self.rod.isEmpty():
            return False
        elif self.rod.size() == 3:  # Checks the size of the rod.
            return True
        else:
            return False

    # This moves a block from a rod to another rod.
    # If it is not possible to move the block then it will not move.
    def blockMove(self, inputRod):  # If the rod is empty the block can move.
        if inputRod.rod.isEmpty():
            inputRod.rod.push(self.rod.pop())
        else:
            # Checks that the block is able to move.
            if inputRod.rod.peek() > self.rod.peek():
                inputRod.rod.push(self.rod.pop())

    # Defines a way to call the rod object so it will return a string.
    def __str__(self):
        tempRod = copy.deepcopy(self)
        if tempRod.rod.isEmpty():
            return "\n\n\n====="
        elif tempRod.rod.size() == 1:
            return "\n\n" + str(tempRod.rod.pop()) + "\n" + "====="
        elif tempRod.rod.size() == 2:
            return "\n" + str(tempRod.rod.pop()) + "\n" + str(tempRod.rod.pop()) + "\n" + "====="
        else:
            return "\n" + str(tempRod.rod.pop()) + "\n" + str(tempRod.rod.pop()) + "\n" + str(tempRod.rod.pop()) + "\n" + "====="
