# A class the acts as the blocks in the TOH game.

class Block:

    # This constructor ensures that the correct data is input.
    def __init__(self, inputData):
        if inputData >= 1 and inputData <= 3:
            self.size = inputData
        else:
            self.size = 1

    # Defines a way to print by just calling the object.
    def __str__(self):
        if self.size == 1:
            return "  *  "
        elif self.size == 2:
            return " * * "
        else:
            return "* * *"

    # Defines a comparison operator for the object.
    def __gt__(self, inputObject):
        if not isinstance(inputObject, Block):
            return None
        else:
            if self.size > inputObject.size:
                return True
            else:
                return False

    # Defines a comparison operator for the object.
    def __lt__(self, inputObject):
        if not isinstance(inputObject, Block):
            return None
        else:
            if self.size < inputObject.size:
                return True
            else:
                return False
