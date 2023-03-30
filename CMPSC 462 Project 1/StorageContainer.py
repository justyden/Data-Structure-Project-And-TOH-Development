# Defines a storage container that can store items.
# The container can be accessed from the end and the front.

import Deque


class StorageContainer:

    # A constructor that creates and empty deque for the items.
    def __init__(self):
        self.storage = Deque.Deque()

    # Returns the amount of items in the container.
    def amountOfItems(self):
        return self.storage.size()

    # Adds an item to the front of the container.
    def addItemFront(self, item):
        self.storage.enqueueStart(item)
        print(str(item) + " has been added to the front of the container.")

    # Adds an item to the end of the container.
    def addItemEnd(self, item):
        self.storage.enqueueEnd(item)
        print(str(item) + " has been added to the end of the container.")

    # Removes an element from the front of the container and returns it.
    def removeItemFront(self):
        tempItem = self.storage.dequeueStart()
        print(tempItem + " has been removed from the front of the container.")
        return tempItem

    # Removes an element from the end of the container and returns it.

    def removeItemEnd(self):
        tempItem = self.storage.dequeueEnd()
        print(tempItem + " has been removed from the end of the container.")
        return tempItem

    # Checks the item at the front of the container and returns it.
    def getItemFront(self):
        if self.storage == []:
            return 0
        else:
            return self.storage.peekFront()

    # Checks the item at the end of the container and returns it.
    def getItemEnd(self):
        if self.storage == []:
            return 0
        else:
            return self.storage.peekEnd()


storage1 = StorageContainer()
storage1.addItemFront("Table")
storage1.addItemFront("Desk")
storage1.addItemFront("Box")
storage1.addItemEnd("Picture")
storage1.addItemEnd("Computer")
print(storage1.getItemEnd())
print(storage1.getItemFront())
storage1.removeItemEnd()
storage1.removeItemFront()
