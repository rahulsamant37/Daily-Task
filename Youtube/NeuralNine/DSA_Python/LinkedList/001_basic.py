class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    def __repr__(self):
        pass
head = Node(1)
node_1 = Node(2)
node_2 = Node(3)
node_3 = Node(4)

head.next = node_1
node_1.next = node_2
node_2.next = node_3

def print_LL(head):
    if head is None:
        print(None)
        return
    print(head.data, end = " -> ")
    print_LL(head.next)
print_LL(head)
print()

class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def __repr__(self):
        pass
    
    ## O(n) Linear Time
    def __contains__(self, val):
        temp = self.head
        while temp:
            if temp.data==val:
                return True
            temp = temp.next
        return False
    
    ## O(n) Linear Time
    def __len__(self):
        temp = self.head
        count=0
        while temp:
            count+=1
            temp = temp.next
        return count
    
    ## O(n) Linear Time
    def append(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = Node(val)
    
    ## O(1) Constant Time
    def prepend(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            newhead = Node(val)
            newhead.next = self.head
            self.head = newhead
    
    ## O(n) Linear Time
    def insert(self, val, index):
        if index == 0:
            self.prepend(val)
        else:
            if self.head is None:
                raise ValueError("Index out of Bounds!")
            else:
                last = self.head
                for _ in range(index-1):
                    if last.next is None:
                        raise ValueError("Index out of Bounds!")
                    last = last.next
                new_node = Node(val)
                new_node.next = last.next
                last.next = new_node
    
    
head = Node(1)
LL = LinkedList(head)

print("Initial list:")
print_LL(LL.head)
print()

LL.append(2)
print("After append(2):")
print_LL(LL.head)
print()

LL.prepend(3)
print("After prepend(3):")
print_LL(LL.head)
print()

LL.insert(3, 2)
print("After insert(3) in 2nd index:")
print_LL(LL.head)
print()

print("Testing if Linked List contain 3 or not:")
print(LL.__contains__(3))
print()

print("Testing if Linked List contain 10 or not:")
print(LL.__contains__(10))
print()

print("Printing the Size of LinkedList:")
print(LL.__len__())
print()