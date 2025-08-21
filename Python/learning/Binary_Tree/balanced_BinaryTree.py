from Generic_Binary_Tree_Input import predefine_binary_tree_inputs

def balanced_or_not(root):
    if root is None:
        return True, 0

    left_balanced, left_height = balanced_or_not(root.left)
    right_balanced, right_height = balanced_or_not(root.right)
    
    balanced = left_balanced and right_balanced and abs(left_height-right_height) <= 1
    height = 1 + max(left_height, right_height)
    return balanced, height

# root1, root2, root3 = predefine_binary_tree_inputs()

# print(balanced_or_not(root1))
# print(balanced_or_not(root3))