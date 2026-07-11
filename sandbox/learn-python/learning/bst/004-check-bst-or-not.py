from helper import create_predefined_bsts

def find_max(node):
    if node is None:
        return float('-inf')  # Return smallest possible value for comparison
    left_max = find_max(node.left)
    right_max = find_max(node.right)
    return max(left_max, right_max, node.data)

def find_min(node):
    if node is None:
        return float('inf')  # Return largest possible value for comparison
    left_min = find_min(node.left)
    right_min = find_min(node.right)
    return min(left_min, right_min, node.data)

def check_bst_or_not(root):
    if (root is None):
        return True ## Base Condition : Empty Tree is a BST
    
    left_max = find_max(root.left)
    right_min = find_min(root.right)
    
    left_BST = check_bst_or_not(root.left)
    right_BST = check_bst_or_not(root.right)
    
    return left_BST and right_BST and (left_max < root.data) and (right_min > root.data)

root1, root2, root3 = create_predefined_bsts()
print(check_bst_or_not(root1))
    