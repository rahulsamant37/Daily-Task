class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def predefine_binary_tree_inputs():
    # Binary Tree 1
    root1 = BinaryTreeNode(1)
    root1.left = BinaryTreeNode(2)
    root1.right = BinaryTreeNode(3)
    root1.left.left = BinaryTreeNode(4)
    root1.left.right = BinaryTreeNode(5)
    root1.right.left = BinaryTreeNode(6)

    # Binary Tree 2
    root2 = BinaryTreeNode(10)
    root2.left = BinaryTreeNode(20)
    root2.right = BinaryTreeNode(30)
    root2.left.left = BinaryTreeNode(40)
    root2.left.right = BinaryTreeNode(50)
    root2.right.right = BinaryTreeNode(60)

    # Binary Tree 3
    root3 = BinaryTreeNode(100)
    root3.left = BinaryTreeNode(200)
    root3.right = BinaryTreeNode(300)

    root3.left.right = BinaryTreeNode(400)
    root3.left.right.left = BinaryTreeNode(700)       # left-only child
    root3.left.right.left.right = BinaryTreeNode(800) # right-only child

    root3.right.left = BinaryTreeNode(500)
    root3.right.right = BinaryTreeNode(600)
    root3.right.right.right = BinaryTreeNode(900)     # deeper leaf

    return root1, root2, root3

# Returns three predefined binary trees for testing or demonstration purposes.
# Tree 1:

#       1
#     /   \
#    2     3
#  /  \   /
# 4    5 6

# Tree 2:

#      10
#     /  \
#   20    30
#  /  \     \
# 40  50     60

# Tree 3:

#          100
#         /   \
#      200     300
#        \     /   \
#       400  500   600
#      /            \
#    700            900
#      \
#      800

# Returns:
#     tuple: A tuple containing the roots of the three binary trees (root1, root2, root3).