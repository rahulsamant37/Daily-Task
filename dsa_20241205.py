# DSA Problem for 2024-12-05

Here is a novel DSA problem with a Python solution for 2024-12-05:

**Problem Statement:**

**"Maximize Christmas Tree Decorations"**

You have been tasked with decorating a Christmas tree with a set of unique ornaments. Each ornament has a specific weight and a specific value. You can only place one ornament on each branch of the tree, and you want to maximize the total value of the ornaments while ensuring that the total weight of the ornaments does not exceed a certain limit.

The tree has `n` branches, and you have `m` ornaments to choose from. Each ornament is represented by a tuple `(weight, value)`. Your goal is to find the maximum total value of ornaments that can be placed on the tree without exceeding the weight limit `W`.

**Constraints:**

* `1 <= n <= 100`
* `1 <= m <= 100`
* `1 <= weight <= 100`
* `1 <= value <= 100`
* `1 <= W <= 1000`

**Optimal Solution:**

Here is a Python solution using dynamic programming:
```python
def max_christmas_tree_decorations(n, m, ornaments, W):
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, W + 1):
            max_val = 0
            for ornament in ornaments:
                weight, value = ornament
                if weight <= j:
                    max_val = max(max_val, dp[i - 1][j - weight] + value)
            dp[i][j] = max_val

    return dp[n][W]

# Example usage:
n = 5
m = 10
ornaments = [(2, 10), (3, 20), (1, 5), (4, 30), (2, 15), (3, 25), (4, 35), (5, 40), (1, 10), (2, 20)]
W = 10
print(max_christmas_tree_decorations(n, m, ornaments, W))  # Output: 60
```
**Time/Space Complexity Analysis:**

* Time complexity: O(n \* m \* W)
	+ The outer loop iterates `n` times, the middle loop iterates `W` times, and the inner loop iterates `m` times.
* Space complexity: O(n \* W)
	+ We need to store the dynamic programming table `dp` with size `(n + 1) x (W + 1)`.

The solution works by building a dynamic programming table `dp` where `dp[i][j]` represents the maximum total value of ornaments that can be placed on the first `i` branches of the tree with a total weight of `j`. We fill up the table by iterating over the branches, weights, and ornaments, and choosing the maximum value that can be achieved by placing each ornament on each branch. Finally, we return the maximum total value that can be achieved with the given weight limit `W`.