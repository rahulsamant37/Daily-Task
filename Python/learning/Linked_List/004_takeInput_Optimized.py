from helper import printLL, LinkedList

def takeInputOptimized():
    val = int(input("Enter the data for Node (-1 to exit): "))
    head, tail = None, None
    
    while val!=-1:
        newNode = LinkedList(val)
        
        if head is None:
            head = newNode ## 3(head)-> 
            tail = newNode ## 3(head)-> 
        else:
            tail.next = newNode ## 3(tail)-> 2-> 
            tail = tail.next ## 3-> 2(tail)-> 
        val = int(input("Enter the data for Node (-1 to exit): "))
    return head

printLL(takeInputOptimized())