from helper import printLL, LinkedList

def takeInputOptimized():
    """
    Benefits of Head–Tail (Iterative) Approach
    | Aspect        | Recursive Version       | Iterative Head–Tail Version |
    | ------------- | ----------------------- | --------------------------- |
    | Stack usage   | `O(n)`                  | `O(1)`                      |
    | Risk of crash | Yes (stack overflow)    | No                          |
    | Performance   | Slower (function calls) | Faster                      |
    | Scalability   | Limited                 | Better for large input      |
    """
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