# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) where the difference between consecutive elements in the subsequence is exactly `k`.

Example:
Input: nums = [3, 10, 3, 4, 5], k = 1
Output: 3
Explanation: The longest increasing subsequence with a difference of 1 is [3, 4, 5].

Input: nums = [4, 12, 10, 0, 10, 9, 0], k = 0
Output: 2
Explanation: The longest increasing subsequence with a difference of 0 is [0, 0] or [10, 10].

Input: nums = [1, 5, 7, 8, 5, 3, 4, 2, 1], k = 2
Output: 1
Explanation: No increasing subsequence of length greater than 1 exists with a difference of 2.
'''

# Solution
def longest_increasing_subsequence_with_difference(nums, k):
    """
    Finds the length of the longest increasing subsequence with a specific difference.

    Args:
        nums: A list of integers.
        k: The required difference between consecutive elements in the subsequence.

    Returns:
        The length of the longest increasing subsequence with a difference of k.
    """
    if not nums:
        return 0

    # dp[num] stores the length of the longest increasing subsequence ending with num
    dp = {}

    max_len = 0
    for num in nums:
        # If num - k exists in the dp dictionary, it means we can extend a previous subsequence
        if num - k in dp:
            dp[num] = dp[num - k] + 1
        # Otherwise, this is the start of a new subsequence of length 1
        else:
            dp[num] = 1
        
        # Update the maximum length found so far
        max_len = max(max_len, dp[num])

    return max_len

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_difference([3, 10, 3, 4, 5], 1) == 3
    assert longest_increasing_subsequence_with_difference([4, 12, 10, 0, 10, 9, 0], 0) == 2
    assert longest_increasing_subsequence_with_difference([1, 5, 7, 8, 5, 3, 4, 2, 1], 2) == 1
    assert longest_increasing_subsequence_with_difference([1, 2, 3, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_difference([5, 4, 3, 2, 1], -1) == 5
    assert longest_increasing_subsequence_with_difference([1, 1, 1, 1, 1], 0) == 5
    assert longest_increasing_subsequence_with_difference([], 1) == 0
    assert longest_increasing_subsequence_with_difference([1], 1) == 1
    assert longest_increasing_subsequence_with_difference([1, 3, 5, 7, 9], 2) == 5
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()