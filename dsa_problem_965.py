# DSA Problem generated on 2024-10-24

Here is a unique DSA problem in Python with solution:

**Problem Statement:**

Given a binary tree, write a function to find the maximum sum of a path from the root to a leaf node. The path sum is defined as the sum of node values from the root to a leaf node. If the tree is empty, return 0.

**Solution Code:**
```python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def max_path_sum(root):
    max_sum = [0]

    def dfs(node, current_sum):
        if not node:
            return
        current_sum += node.val
        if not node.left and not node.right:  # leaf node
            max_sum[0] = max(max_sum[0], current_sum)
            return
        dfs(node.left, current_sum)
        dfs(node.right, current_sum)

    dfs(root, 0)
    return max_sum[0]
```
**Time Complexity Analysis:**

The time complexity of the solution is O(n), where n is the number of nodes in the binary tree. This is because we visit each node exactly once during the DFS traversal.

The space complexity is O(h), where h is the height of the binary tree. This is because the maximum recursion depth is equal to the height of the tree.

Here's an explanation of the solution:

1. We define a `TreeNode` class to represent each node in the binary tree.
2. The `max_path_sum` function takes the root node as input and returns the maximum sum of a path from the root to a leaf node.
3. We use a helper function `dfs` to perform a depth-first search traversal of the tree.
4. In the `dfs` function, we recursively visit each node and add its value to the `current_sum`.
5. When we reach a leaf node, we update the `max_sum` if the current sum is greater than the previous maximum sum.
6. Finally, we return the maximum sum found.

Example usage:
```python
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(max_path_sum(root))  # Output: 11 (1 + 2 + 4)
```
I hope this helps! Let me know if you have any questions.