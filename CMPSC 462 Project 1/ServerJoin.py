# This class acts as a basic server that allows people
# to join and connect. Implements a queue to allow it
# to work correctly.

import Queue


class ServerJoin:

    # A constructor that creates an empty queue.
    def __init__(self):
        self.queue = Queue.Queue()

    # Adds an ID into the queue.
    def joinServer(self, inputID):
        self.queue.enqueue(inputID)
        print("The id " + str(inputID) + " has joined the queue.")

    # The person is connected into the server and is removed from the queue.
    # The ID is also returned.
    def connectedToServer(self):
        tempID = 0
        tempID = self.queue.dequeue()
        print("The id " + str(tempID) + " has connected to the server.")

    # Returns the amount of people that are entered into the queue.
    def queueSize(self):
        print("The queue size is " + str(self.queue.size()) + " people.")


server1 = ServerJoin()
server1.joinServer(15)
server1.joinServer(40)
server1.queueSize()
server1.connectedToServer()
server1.queueSize()
