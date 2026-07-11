from helper import printLL, LinkedList

def takeInput():
    val = int(input("Enter the data for Node(-1 to exit): "))
    if val == -1:
        return None
    head = LinkedList(val)
    head.next = takeInput()
    return head

printLL(takeInput())