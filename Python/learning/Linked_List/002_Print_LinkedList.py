from helper import predefine_linked_list_inputs

def printLL(head):
    if head is None:
        print("None")
        return
    print(head.data, end="-> ")
    printLL(head.next)

head1, head2, head3 = predefine_linked_list_inputs()
print("--------------## First LinkedList ##----------------", end="\n")
printLL(head1)
print("--------------## Second LinkedList ##----------------", end="\n")
printLL(head2)
print("--------------## Third LinkedList ##----------------", end="\n")
printLL(head3)
