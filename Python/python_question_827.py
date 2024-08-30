# Python Question: Find the Longest Increasing Subsequence with Maximum Sum
'''
Given an array of integers, find the longest increasing subsequence (LIS) such that the sum of its elements is maximum.

Example:
Input: arr = [1, 101, 2, 3, 100, 4, 5]
Output: 106 (The LIS is [1, 2, 3, 100], and its sum is 106)

Input: arr = [10, 5, 4, 3]
Output: 10 (The LIS is [10], and its sum is 10)
'''

# Solution
def longest_increasing_subsequence_with_maximum_sum(arr):
    """
    Finds the longest increasing subsequence (LIS) with the maximum sum.

    Args:
        arr: A list of integers.

    Returns:
        The maximum sum of the LIS.
    """

    n = len(arr)

    # lis[i] stores the maximum sum of an increasing subsequence ending at arr[i]
    lis = [0] * n

    # Initialize lis values for all indexes
    for i in range(n):
        lis[i] = arr[i]

    # Compute optimized LIS values in bottom up manner
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + arr[i]:
                lis[i] = lis[j] + arr[i]

    # Return the maximum of all LIS values
    maximum = 0
    for i in range(n):
        if maximum < lis[i]:
            maximum = lis[i]

    return maximum


# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_maximum_sum([1, 101, 2, 3, 100, 4, 5]) == 106
    assert longest_increasing_subsequence_with_maximum_sum([10, 5, 4, 3]) == 10
    assert longest_increasing_subsequence_with_maximum_sum([3, 4, 5, 10]) == 22
    assert longest_increasing_subsequence_with_maximum_sum([1, 2, 3, 4, 5]) == 15
    assert longest_increasing_subsequence_with_maximum_sum([5, 4, 3, 2, 1]) == 5
    assert longest_increasing_subsequence_with_maximum_sum([]) == 0
    assert longest_increasing_subsequence_with_maximum_sum([1]) == 1
    assert longest_increasing_subsequence_with_maximum_sum([1, 1, 1, 1]) == 1
    assert longest_increasing_subsequence_with_maximum_sum([1, 2, 1, 5]) == 8 # 1+2+5
    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()