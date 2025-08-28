class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def create_predefined_bsts():
    # 1. Balanced BST
    #        10
    #       /  \
    #      5    15
    #     / \   / \
    #    3   7 12 18
    balanced_root = TreeNode(10)
    balanced_root.left = TreeNode(5)
    balanced_root.right = TreeNode(15)
    balanced_root.left.left = TreeNode(3)
    balanced_root.left.right = TreeNode(7)
    balanced_root.right.left = TreeNode(12)
    balanced_root.right.right = TreeNode(18)

    # 2. Right-skewed BST (each node has only right child)
    # 1 -> 2 -> 3 -> 4 -> 5
    right_skewed_root = TreeNode(1)
    current = right_skewed_root
    for i in range(2, 6):
        current.right = TreeNode(i)
        current = current.right

    # 3. Left-skewed BST (each node has only left child)
    # 5 <- 4 <- 3 <- 2 <- 1
    left_skewed_root = TreeNode(5)
    current = left_skewed_root
    for i in range(4, 0, -1):
        current.left = TreeNode(i)
        current = current.left

    return balanced_root, right_skewed_root, left_skewed_root