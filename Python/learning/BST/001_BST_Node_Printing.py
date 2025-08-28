class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def print_bst(self, root):
        if (root is None):
            return
        
        self.print_bst(root.left)
        print(root.data, end=" ") ## Inorder Traversal of my BST
        self.print_bst(root.right)

