# DSA Problem generated on 2024-11-28

Here's a unique DSA problem in Python:

**Problem Statement:**

Given a 2D matrix of 0s and 1s, find the maximum area of a rectangle that can be formed using the 1s in the matrix. The rectangle should not have any 0s inside it.

**Example:**

Input:
```
matrix = [
    [0, 1, 0, 0],
    [0, 1, 1, 1],
    [1, 1, 1, 0],
    [0, 0, 0, 0]
]
```
Output:
```
4
```
Explanation: The maximum area of a rectangle that can be formed is 2x2, which has an area of 4.

**Solution Code:**
```
def max_rectangle_area(matrix):
    if not matrix:
        return 0

    m, n = len(matrix), len(matrix[0])
    heights = [0] * n
    max_area = 0

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                heights[j] += 1
            else:
                heights[j] = 0

        stack = []
        for k in range(n + 1):
            while stack and (k == n or heights[stack[-1]] >= heights[k]):
                h = heights[stack.pop()]
                w = k if not stack else k - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(k)

    return max_area
```
**Time Complexity Analysis:**

The time complexity of this solution is O(m \* n), where m is the number of rows and n is the number of columns in the matrix.

Here's a breakdown of the time complexity:

* The outer loop iterates m times, where m is the number of rows in the matrix.
* The inner loop iterates n times, where n is the number of columns in the matrix.
* The stack operations (push and pop) take constant time, so they don't affect the overall time complexity.
* The calculation of the maximum area takes constant time, so it doesn't affect the overall time complexity.

Therefore, the overall time complexity is O(m \* n), which is the product of the number of rows and columns in the matrix.

This problem is a variation of the "Largest Rectangle in Histogram" problem, but with a 2D matrix instead of a 1D histogram. The solution uses a stack to keep track of the indices of the columns, and calculates the maximum area of a rectangle that can be formed by considering the heights of the columns.