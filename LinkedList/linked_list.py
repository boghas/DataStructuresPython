class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self, value):
        self.head = Node(value)
        self.tail = Node(value)
        self.length = 1