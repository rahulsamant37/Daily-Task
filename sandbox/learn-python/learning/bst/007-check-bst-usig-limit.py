from helper import create_predefined_bsts, TreeNode

def checkBSTLimit(root, minimum, maximum):
    if root is None:
        return True

    if root.data < minimum or root.data > maximum:
        return False

    return checkBSTLimit(root.left, minimum, root.data - 1) and checkBSTLimit(root.right, root.data + 1, maximum)

root1, root2, root3 = create_predefined_bsts()

print(checkBSTLimit(root1, float("-inf"), float("inf")))
print(checkBSTLimit(root2, float("-inf"), float("inf")))
print(checkBSTLimit(root3, float("-inf"), float("inf")))

# Build the invalid BST
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(6)  # Invalid node (should be >10)
"""
       10
      /  \
     5    15
         /
        6   ← violates BST rule (should be > 10)
"""
# Run the check
print(checkBSTLimit(root, float('-inf'), float('inf')))