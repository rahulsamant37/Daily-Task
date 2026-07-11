from helper import predefine_linked_list_inputs, printLL, LinkedList

def insert_head(head, value):
    if head is None:
        return None
    newNode = LinkedList(value)
    newNode.next = head
    head = newNode
    return head

def insert_tail(head, value):
    if head is None:
        return None
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = LinkedList(value)
    return head

def insert_inBetween(head, value, k):
    count = 0
    temp = head
    while count<k and temp.next:
        temp = temp.next
        count+=1
    if count!=k:
        temp.next = LinkedList(value)
    else:
        new_node = LinkedList(value)
        new_node.next = temp.next
        temp.next = new_node
    return head

node1, node2, node3 = predefine_linked_list_inputs()

printLL(node1)
node1 = insert_head(node1, 10)
printLL(node1)
insert_tail(node1, 10)
printLL(node1)
insert_inBetween(node1, 10, 2)
printLL(node1)