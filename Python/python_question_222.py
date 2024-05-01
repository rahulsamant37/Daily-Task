# Python Question: Maximum Weighted Independent Set in a Path Graph
'''
Given a path graph represented by a list of node weights, find the maximum weight of an independent set of nodes. An independent set is a set of nodes where no two nodes are adjacent.

Input: A list of integers representing the weights of the nodes in the path graph.
Output: An integer representing the maximum weight of an independent set.

Example:
Input: [1, 2, 3, 4, 5]
Output: 9 (Nodes with weights 1, 3, and 5 form the maximum weighted independent set)

Input: [1, 2, 3]
Output: 4 (Nodes with weights 1 and 3 form the maximum weighted independent set)

Input: [5, 5, 10, 100, 10, 5, 5]
Output: 120 (Nodes with weights 5, 10, 100, and 5 form the maximum weighted independent set)
'''

# Solution
def solution(weights):
    """
    Finds the maximum weight of an independent set in a path graph.

    Args:
        weights: A list of integers representing the weights of the nodes.

    Returns:
        An integer representing the maximum weight of an independent set.
    """

    n = len(weights)

    # If the graph is empty, the maximum weight is 0.
    if n == 0:
        return 0

    # If the graph has only one node, the maximum weight is the weight of that node.
    if n == 1:
        return weights[0]

    # dp[i] stores the maximum weight of an independent set considering the first i nodes.
    dp = [0] * n

    # Base cases:
    dp[0] = weights[0]  # The maximum weight considering only the first node is its weight.
    dp[1] = max(weights[0], weights[1])  # The maximum weight considering the first two nodes is the maximum of the two weights.

    # Iterate through the remaining nodes.
    for i in range(2, n):
        # For each node, we have two choices:
        # 1. Include the current node in the independent set. In this case, we cannot include the previous node.
        # 2. Exclude the current node from the independent set.

        # If we include the current node, the maximum weight is the weight of the current node plus the maximum weight considering the first i-2 nodes.
        include_current = weights[i] + dp[i - 2]

        # If we exclude the current node, the maximum weight is the maximum weight considering the first i-1 nodes.
        exclude_current = dp[i - 1]

        # Choose the option that gives us the maximum weight.
        dp[i] = max(include_current, exclude_current)

    # The maximum weight of an independent set is stored in the last element of the dp array.
    return dp[n - 1]

# Test cases
def test_solution():
    assert solution([1, 2, 3, 4, 5]) == 9
    assert solution([1, 2, 3]) == 4
    assert solution([5, 5, 10, 100, 10, 5, 5]) == 120
    assert solution([10, 1, 2, 10, 100]) == 120
    assert solution([1]) == 1
    assert solution([]) == 0
    assert solution([1, 10]) == 10
    assert solution([10, 1]) == 10
    assert solution([4, 8, 5, 10, 20]) == 32
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()