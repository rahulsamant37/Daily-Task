class LL:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    def __repr__(self):
        pass
head = LL(0)
node_1 = LL(1)
node_2 = LL(2)
node_3 = LL(3)

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