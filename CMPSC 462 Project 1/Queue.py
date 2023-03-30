# Implements a basic queue class.

class Queue:

    # A constructor that creates an empty list.
    def __init__(self):
        self.items = []

    # Checks to see if the queue is empty and returns a boolean value.
    def isEmpty(self):
        return self.items == []

    # Returns the number of elements in the queue.
    def size(self):
        return len(self.items)

    # Adds an element to the end of the queue.
    def enqueue(self, inputData):
        self.items.append(inputData)

    # Removes an element from the front of the queue and returns it.
    def dequeue(self):
        if self.items == []:
            return 0
        else:
            return self.items.pop(0)

