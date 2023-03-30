# Implements a basic stack class.

class Stack():

    # This is the constructor that creates an empty list.
    def __init__(self):
        self.items = []

    # Checks if the stack is empty and returns a boolean value.
    def isEmpty(self):
        return self.items == []

    # Returns the number of elements in the stack.
    def size(self):
        return len(self.items)

    # Adds an element to the end of the stack.
    def push(self, inputData):
        self.items.append(inputData)

    # Removes an element from the end of the stack and returns it.
    def pop(self):
        if len(self.items) == 0:
            return 0
        else:
            return self.items.pop()

    # Checks the end of the stack and returns the element without removing it.
    def peek(self):
        if len(self.items) == 0:
            return 0
        else:
            return self.items[-1]


