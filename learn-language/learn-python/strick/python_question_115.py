# Python Question: Longest Increasing Subsequence with Maximum Sum
'''
Given an array of integers, find the longest increasing subsequence (LIS) such that the sum of its elements is maximized. Return the maximum sum.

Example:
Input: [1, 101, 2, 3, 100, 4, 5]
Output: 106
Explanation: The LIS with the maximum sum is [1, 2, 3, 100] with a sum of 106. Another LIS is [1, 2, 3, 4, 5] with sum 15. [1, 101] is an increasing subsequence but is not the longest with max sum.

Input: [10, 5, 4, 3]
Output: 10
Explanation: The LIS with maximum sum is [10] with sum 10.

Input: [1, 3, 2, 4, 5]
Output: 15
Explanation: The LIS with maximum sum is [1, 3, 4, 5] with sum 13. The LIS [1, 2, 4, 5] is also valid and has sum 12. But [1,3,4,5] has the longest increasing subsequence and max sum.
'''

# Solution
def solution(arr):
    """
    Finds the longest increasing subsequence with the maximum sum in an array.

    Args:
        arr: A list of integers.

    Returns:
        The maximum sum of the longest increasing subsequence.
    """

    n = len(arr)
    # Initialize a DP table to store the maximum sum of LIS ending at each index.
    dp = [0] * n
    # Initialize the DP table with the values of the array itself.
    # This is because a single element is an increasing subsequence of length 1.
    for i in range(n):
        dp[i] = arr[i]

    # Iterate through the array to build the DP table.
    for i in range(1, n):
        for j in range(i):
            # If the current element is greater than the previous element,
            # it can be added to the LIS ending at the previous element.
            if arr[i] > arr[j]:
                # Update the maximum sum of LIS ending at the current element.
                dp[i] = max(dp[i], dp[j] + arr[i])

    # The maximum value in the DP table is the maximum sum of the LIS.
    return max(dp) if n > 0 else 0
    

# Test cases
def test_solution():
    assert solution([1, 101, 2, 3, 100, 4, 5]) == 106
    assert solution([10, 5, 4, 3]) == 10
    assert solution([1, 3, 2, 4, 5]) == 15
    assert solution([1, 5, 2, 3, 4]) == 15
    assert solution([1, 2, 3, 4, 5]) == 15
    assert solution([5, 4, 3, 2, 1]) == 5
    assert solution([]) == 0
    assert solution([1]) == 1
    assert solution([1,2]) == 3
    assert solution([2,1]) == 2
    assert solution([4, 2, 3, 6, 10, 1, 12]) == 32
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()