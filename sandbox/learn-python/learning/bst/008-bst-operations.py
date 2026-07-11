from helper import create_predefined_bsts, TreeNode

class BST:
    """
    A class to represent a Binary Search Tree (BST).
    Supports insertion, search, and deletion of nodes.
    """
    def __init__(self):
        self.root = None
    
    def _insert_recursive(self, node, value):
        if node is None:
            return TreeNode(value)
        
        if value < node.data:
            node.left = self._insert_recursive(node.left, value)
        else:
            node.right = self._insert_recursive(node.right, value)
        return node
    
    def _search_recursive(self, node, value):
        if node is None:
            return False
        
        if node.data == value:
            return True
        elif value < node.data:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)
    
    def _min_value_node(self, node):
        """Helper function to find node with the minimum value in a subtree."""
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def _delete_recursive(self, node, value):
        if node is None:
            return None
                
        if value < node.data:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.data:
            node.right = self._delete_recursive(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                 # Node with two children
                successor = self._min_value_node(node.right)
                node.data = successor.data
                node.right = self._delete_recursive(node.right, successor.data)
        return node
    
    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)

    def search(self, value):
        return self._search_recursive(self.root, value)
    
    def delete(self, value):
        return self._delete_recursive(self.root, value)

root1, root2, root3 = create_predefined_bsts()

bst = BST()
bst.root = root1
print(bst.search(18))
print(bst.search(7))
print(bst.search(17))
bst.insert(17)
print("----------## After Inserted New Value ##------------")
print(bst.search(17))
bst.delete(17)
print("----------## After Deleting New Value ##------------")
print(bst.search(17))