from helper import predefine_binary_tree_inputs

def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

def diameterOfBinaryTree(root):
    if (root is None):
        return 0
    
    leftHeight = height(root.left)
    rightHeight = height(root.right)
    
    leftDiameter = diameterOfBinaryTree(root.left)
    rightDiameter = diameterOfBinaryTree(root.right)
    return max(leftDiameter,rightDiameter, leftHeight+rightHeight)

# root1, root2, root3 = predefine_binary_tree_inputs()

# print(height(root3))
# print(diameterOfBinaryTree(root3))

## optimize this

def diameterOfBinaryTreeOptimized(root):
    if (root is None):
        return 0,0 ## Height, Diameter
    
    left_height, left_diameter = diameterOfBinaryTreeOptimized(root.left)
    right_height, right_diameter = diameterOfBinaryTreeOptimized(root.right)
    
    current_height = 1 + max(left_height, right_height)
    diameter_through_root = left_height + right_height
    current_diameter = max(diameter_through_root, left_diameter, right_diameter)

    return current_height, current_diameter


# root1, root2, root3 = predefine_binary_tree_inputs()

# print(height(root3))
# print(diameterOfBinaryTreeOptimized(root3))
    