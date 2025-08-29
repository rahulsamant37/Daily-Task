from helper import create_predefined_bsts

def printBSTInRange(root, low, high):
    if root is None:
        return
    
    if (low < root.data):
        printBSTInRange(root.left, low, high)
    
    if (low <= root.data <= high):
        print(root.data, end=" ")
    
    if (high > root.data):
        printBSTInRange(root.right, low, high)

root1, root2, root3 = create_predefined_bsts()

printBSTInRange(root1,0,100)