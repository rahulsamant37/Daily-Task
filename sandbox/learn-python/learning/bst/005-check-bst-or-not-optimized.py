from helper import create_predefined_bsts

def is_bst_optimized(node):
    # Helper function returns a tuple:
    # (is_bst, min_value, max_value)
    def helper(n):
        if n is None:
            return True, float('inf'), float('-inf')  # Empty tree is BST
        
        left_is_bst, left_min, left_max = helper(n.left)
        right_is_bst, right_min, right_max = helper(n.right)
        
        # Current node is BST if:
        # - left and right subtrees are BSTs
        # - max value in left < current node
        # - min value in right > current node
        current_is_bst = (
            left_is_bst and 
            right_is_bst and 
            left_max < n.data < right_min
        )
        
        # Update min and max for current subtree
        current_min = min(left_min, n.data)
        current_max = max(right_max, n.data)
        
        return current_is_bst, current_min, current_max

    result, _, _ = helper(node)
    return result

root1, root2, root3 = create_predefined_bsts()
print(is_bst_optimized(root1))