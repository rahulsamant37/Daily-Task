# Python Question: Longest Increasing Subsequence with Given Difference
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) where the difference between consecutive elements is exactly `k`.

Example:
Input: nums = [3, 10, 3, 4, 5], k = 1
Output: 3
Explanation: The longest increasing subsequence with a difference of 1 is [3, 4, 5], which has a length of 3.

Input: nums = [1, 5, 7, 8, 5, 3, 4, 2, 1], k = -2
Output: 4
Explanation: The longest increasing subsequence with a difference of -2 is [7, 5, 3, 1], which has a length of 4.
'''

# Solution
def longest_increasing_subsequence_with_difference(nums, k):
    """
    Finds the length of the longest increasing subsequence (LIS) where the difference
    between consecutive elements is exactly k.

    Args:
        nums: A list of integers.
        k: The difference between consecutive elements in the LIS.

    Returns:
        The length of the longest increasing subsequence with difference k.
    """
    # Use a dictionary to store the length of the LIS ending at each number.
    # The key is the number, and the value is the length of the LIS ending at that number.
    dp = {}

    # Iterate over the numbers in the input array.
    for num in nums:
        # If the number - k exists in the dp dictionary, then we can extend the LIS
        # ending at number - k by adding the current number.
        if num - k in dp:
            dp[num] = dp[num - k] + 1
        # Otherwise, the LIS ending at the current number has length 1.
        else:
            dp[num] = 1

    # The length of the longest increasing subsequence is the maximum value in the dp dictionary.
    if not dp:
        return 0
    return max(dp.values())

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_difference([3, 10, 3, 4, 5], 1) == 3
    assert longest_increasing_subsequence_with_difference([1, 5, 7, 8, 5, 3, 4, 2, 1], -2) == 4
    assert longest_increasing_subsequence_with_difference([1, 2, 3, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_difference([5, 4, 3, 2, 1], -1) == 5
    assert longest_increasing_subsequence_with_difference([1, 2, 3, 4, 5], 0) == 1
    assert longest_increasing_subsequence_with_difference([1, 1, 1, 1, 1], 0) == 5
    assert longest_increasing_subsequence_with_difference([], 1) == 0
    assert longest_increasing_subsequence_with_difference([5], 1) == 1
    assert longest_increasing_subsequence_with_difference([1, 3, 5, 7, 9], 2) == 5
    assert longest_increasing_subsequence_with_difference([9, 7, 5, 3, 1], -2) == 5
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()