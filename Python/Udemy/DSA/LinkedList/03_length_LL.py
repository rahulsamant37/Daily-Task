class Node():
    def __init__(self, value):
        self.data = value
        self.next = None

def print_LL(head):
    temp = head
    while(temp!=None):
        print(temp.data)
        temp = temp.next

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3
head = node1
# print_LL(head)

def length(head):
    count = 1
    temp = head
    while(temp.next!=None):
        count+=1
        temp = temp.next
    print(count)
length(head)

def length_rescursion(head):
    count = 1
    temp = head
    if temp.next==None:
        return count
    count +=1
    length_rescursion(temp.next)

length_rescursion()