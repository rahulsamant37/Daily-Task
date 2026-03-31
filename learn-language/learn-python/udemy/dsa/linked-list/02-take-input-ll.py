class Node():
    def __init__(self, value):
        self.data = value
        self.next = None

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3
head = node1

def print_LL(head):
    temp = head
    while (temp!=None):
        print(temp.data)
        temp = temp.next
def take_input():
    value = int(input("Enter the first number:- "))
    head = None
    tail = None
    
    while (value!=-1):
        newhead = Node(value)
        if head==None:
            head = newhead
            tail = newhead
        else:
            # temp = head
            # while (temp.next!=None):
            #     temp = temp.next
            tail.next = newhead
            tail = newhead
        value = int(input("Enter your next number:- "))
    return head

new_head = take_input()
print_LL(new_head)