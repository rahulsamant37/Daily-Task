from helper import predefine_linked_list_inputs

def lengthOfLL(head):
    temp = head
    count=0
    while temp:
        count+=1
        temp = temp.next
    return count

def lengthOfLLRecursive(head):
    if head is None:
        return 0
    return 1 + lengthOfLLRecursive(head.next)

head1, head2, head3 = predefine_linked_list_inputs()

print(lengthOfLL(head1))
print(lengthOfLL(head2))
print(lengthOfLLRecursive(head3))