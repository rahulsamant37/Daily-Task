from helper import create_predefined_bsts

def print_bst(root):
    if (root is None):
        return
    
    print_bst(root.left)
    print(root.data, end=" ") ## Inorder Traversal of my BST
    print_bst(root.right)

root1, root2, root3 = create_predefined_bsts()

print_bst(root1)