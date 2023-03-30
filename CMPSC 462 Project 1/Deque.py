# Implements a basic deque.

class Deque:

    # A constructor that creates an empty list.
    def __init__(self):
        self.items = []

    # Checks if the deque is empty and returns a boolean value.
    def isEmpty(self):
        return self.items == []

    # Return the amount of elements in the deque.
    def size(self):
        return len(self.items)

    # Adds an element to the front of the deque.
    def enqueueStart(self, inputData):
        self.items.insert(0, inputData)

    # Adds an element to the end of the deque.
    def enqueueEnd(self, inputData):
        self.items.append(inputData)

    # Removes an element from the front of the deque and returns it.
    def dequeueStart(self):
        if self.items == []:
            return 0
        else:
            return self.items.pop(0)

    # Removes an element from the end of the deque and returns it.
    def dequeueEnd(self):
        if self.items == []:
            return 0
        else:
            return self.items.pop()

    # Gets the element at the front and returns it.
    def peekFront(self):
        if self.items == []:
            return 0
        else:
            return self.items[0]

    # Gets the element at the end and returns it.
    def peekEnd(self):
        if self.items == []:
            return 0
        else:
            return self.items[self.size() - 1]

