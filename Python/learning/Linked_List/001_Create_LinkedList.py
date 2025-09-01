from helper import printLL

class LinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None

head = LinkedList(3)

node1 = LinkedList(2)
node2 = LinkedList(1)

head.next = node1
node1.next = node2

printLL(head)