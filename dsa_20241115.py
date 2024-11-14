# DSA Problem for 2024-11-15

Here is a novel DSA problem with a Python solution for 2024-11-15:

**Problem Statement:**

You are given a 2D matrix of integers, where each cell represents the height of a building in a city. A group of buildings is considered a "cluster" if they are horizontally, vertically, or diagonally adjacent to each other. The task is to find the largest cluster of buildings that have a height greater than or equal to a given threshold value `k`.

**Example Input:**

```
matrix = [
    [3, 2, 1, 4, 5],
    [1, 2, 3, 4, 5],
    [5, 6, 7, 8, 9],
    [4, 3, 2, 1, 6],
    [2, 3, 4, 5, 7]
]
k = 4
```

**Example Output:**

The largest cluster of buildings with a height greater than or equal to `k = 4` is:

```
[
    [4, 5],
    [4, 5],
    [5, 6, 7, 8, 9]
]
```

**Optimal Solution:**

We can use a Depth-First Search (DFS) algorithm to solve this problem.

```
def largest_cluster(matrix, k):
    def dfs(i, j):
        if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]) and matrix[i][j] >= k and (i, j) not in visited:
            visited.add((i, j))
            cluster.append((i, j))
            dfs(i-1, j-1)
            dfs(i-1, j)
            dfs(i-1, j+1)
            dfs(i, j-1)
            dfs(i, j+1)
            dfs(i+1, j-1)
            dfs(i+1, j)
            dfs(i+1, j+1)

    visited = set()
    largest = 0
    clusterCoord = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] >= k and (i, j) not in visited:
                cluster = []
                dfs(i, j)
                if len(cluster) > largest:
                    largest = len(cluster)
                    clusterCoord = cluster
    return clusterCoord
```

**Time Complexity Analysis:**

The time complexity of the above solution is O(M*N), where M is the number of rows and N is the number of columns in the matrix. This is because in the worst case, we need to visit every cell in the matrix.

**Space Complexity Analysis:**

The space complexity of the above solution is O(M*N), where M is the number of rows and N is the number of columns in the matrix. This is because we need to store the coordinates of the largest cluster, which can be as large as the size of the matrix.

Note: The above solution assumes that the input matrix is not extremely large, and the DFS algorithm can be optimized further for larger inputs using techniques like iterative DFS or A\* search.