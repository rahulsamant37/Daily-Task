class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Helper function to create a linked list from a list
def create_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function to print linked list
def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Test
head = create_linked_list([1, 2, 6, 3, 4, 5, 6])
print_linked_list(head)  # Output: 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6 -> None