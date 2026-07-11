from helper import create_predefined_bsts, TreeNode

class SortedListToBSTConverter:
    @staticmethod
    def sortedListToBSTHelper(l1, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        root = TreeNode(l1[mid])
        root.left = SortedListToBSTConverter.sortedListToBSTHelper(l1, start, mid - 1)
        root.right = SortedListToBSTConverter.sortedListToBSTHelper(l1, mid + 1, end)
        return root

    @staticmethod
    def convert(l1):
        return SortedListToBSTConverter.sortedListToBSTHelper(l1, 0, len(l1) - 1)

def inorder_traversal(root):
    if not root:
        return []
    return inorder_traversal(root.left) + [root.data] + inorder_traversal(root.right)

# Example sorted list
sorted_list = [-10, -3, 0, 5, 9]

# Convert to BST
bst_root = SortedListToBSTConverter.convert(sorted_list)

# In-order traversal of BST should match original sorted list
print("In-order Traversal of BST:", inorder_traversal(bst_root))
