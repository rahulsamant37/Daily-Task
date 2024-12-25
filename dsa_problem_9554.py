# DSA Problem generated on 2024-12-26

Here is a unique DSA problem in Python with a solution:

**Problem Statement:**

Given a binary tree, write a function to find the longest path from the root to a leaf node such that the path sum is equal to a given target sum. If no such path exists, return -1.

**Problem Example:**

Input:
```
     1
    / \
   2   3
  / \
 4   5

target_sum = 7
```
Output:
```
7 (path: 1 -> 2 -> 4)
```
**Solution Code:**
```python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def longest_path_sum(root, target_sum):
    def dfs(node, current_sum, path_len):
        if not node:
            return 0
        current_sum += node.val
        path_len += 1
        if node.left is None and node.right is None and current_sum == target_sum:
            return path_len
        left_len = dfs(node.left, current_sum, path_len)
        right_len = dfs(node.right, current_sum, path_len)
        return max(left_len, right_len)

    return dfs(root, 0, 0) if dfs(root, 0, 0) > 0 else -1

# Example usage:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(longest_path_sum(root, 7))  # Output: 3
```
**Time Complexity Analysis:**

The time complexity of the solution is O(n), where n is the number of nodes in the binary tree. This is because we are performing a depth-first search (DFS) on the tree, and each node is visited at most twice (once for the left subtree and once for the right subtree).

The space complexity is O(h), where h is the height of the tree, which is the maximum depth of the recursion call stack. This is because we are using recursive function calls to traverse the tree, and the maximum depth of the call stack is equal to the height of the tree.

Note that the time complexity could be improved to O(n/2) if we use an iterative approach instead of recursive function calls, but the recursive solution is easier to understand and implement.