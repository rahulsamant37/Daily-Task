# Python Question: Longest Increasing Subsequence with Limited Differences
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) where the difference between consecutive elements in the subsequence is at most `k`.

Example:
Input: nums = [3, 10, 2, 1, 20], k = 5
Output: 3
Explanation: One of the longest increasing subsequences is [3, 10, 20] (length 3). Another is [2, 1, 20].  The subsequence [1, 20] is not valid because 20-1 > 5.  A valid LIS with length 3 would be [3, 2, 1].

Input: nums = [1, 5, 2, 4, 3], k = 1
Output: 3
Explanation: The longest increasing subsequence with difference at most k is [1, 2, 3].

Input: nums = [4, 2, 1, 4, 3, 4, 5, 8, 15], k = 3
Output: 5
Explanation: The longest increasing subsequence with difference at most k is [1, 4, 5, 8, 15].
'''

# Solution
def longest_increasing_subsequence_with_limited_differences(nums, k):
    """
    Finds the length of the longest increasing subsequence (LIS) where the difference
    between consecutive elements in the subsequence is at most `k`.

    Args:
        nums: A list of integers.
        k: An integer representing the maximum difference between consecutive elements.

    Returns:
        The length of the longest increasing subsequence.
    """

    n = len(nums)
    if n == 0:
        return 0

    # dp[i] stores the length of the longest increasing subsequence ending at nums[i]
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            # Check if nums[i] can extend the subsequence ending at nums[j]
            if nums[i] > nums[j] and nums[i] - nums[j] <= k:
                dp[i] = max(dp[i], dp[j] + 1)

    # The maximum value in dp is the length of the LIS
    return max(dp)

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_limited_differences([3, 10, 2, 1, 20], 5) == 3
    assert longest_increasing_subsequence_with_limited_differences([1, 5, 2, 4, 3], 1) == 3
    assert longest_increasing_subsequence_with_limited_differences([4, 2, 1, 4, 3, 4, 5, 8, 15], 3) == 5
    assert longest_increasing_subsequence_with_limited_differences([1, 2, 3, 4, 5], 0) == 1
    assert longest_increasing_subsequence_with_limited_differences([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_limited_differences([], 5) == 0
    assert longest_increasing_subsequence_with_limited_differences([1], 5) == 1
    assert longest_increasing_subsequence_with_limited_differences([1, 3, 5, 2, 4], 2) == 3
    assert longest_increasing_subsequence_with_limited_differences([10, 22, 9, 33, 21, 50, 41, 60, 80], 10) == 6
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()