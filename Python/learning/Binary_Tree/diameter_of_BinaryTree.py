# from Generic_Binary_Tree_Input import predefine_binary_tree_inputs

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