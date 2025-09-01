class LinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None

def predefine_linked_list_inputs():
    """
    Returns:
    tuple: A tuple containing the heads of the five linked lists (head1, head2, head3).
    """
    
    """
    Linked List 1: Basic list with 5 nodes
    List 1: 1 -> 2 -> 3 -> 4 -> 5 -> None (Basic sequential list)
    """
    head1 = LinkedList(1)
    head1.next = LinkedList(2)
    head1.next.next = LinkedList(3)
    head1.next.next.next = LinkedList(4)
    head1.next.next.next.next = LinkedList(5)

    """
    Linked List 2: List with duplicate values
    List 2: 7 -> 3 -> 7 -> 1 -> 3 -> None (List with duplicates)
    """
    head2 = LinkedList(7)
    head2.next = LinkedList(3)
    head2.next.next = LinkedList(7)
    head2.next.next.next = LinkedList(1)
    head2.next.next.next.next = LinkedList(3)

    """
    Linked List 3: Longer list for complex operations
    List 3: 100 -> 200 -> 150 -> 300 -> 250 -> 400 -> 350 -> None (Longer list for complex operations)
    """
    head3 = LinkedList(100)
    head3.next = LinkedList(200)
    head3.next.next = LinkedList(150)
    head3.next.next.next = LinkedList(300)
    head3.next.next.next.next = LinkedList(250)
    head3.next.next.next.next.next = LinkedList(400)
    head3.next.next.next.next.next.next = LinkedList(350)

    return head1, head2, head3

