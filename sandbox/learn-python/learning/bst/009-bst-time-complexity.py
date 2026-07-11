"""
Binary Search Tree (BST) Operations Time Complexity:

Operations:
    1. Search
    2. Insert
    3. Delete

Time Complexity (in terms of 'n' nodes and 'h' as the height of the tree):

    - Average Case (Balanced BST):
        Search: O(log n)
        Insert: O(log n)
        Delete: O(log n)

    - Worst Case (Unbalanced BST, e.g., a skewed tree):
        Search: O(n)
        Insert: O(n)
        Delete: O(n)

Notes:
    - The time complexity depends on the height of the tree (h).
    - In a balanced BST (e.g., AVL tree or Red-Black tree), h ≈ log n.
    - In the worst case (unbalanced), h can be as large as n.

"""
