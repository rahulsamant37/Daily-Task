# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums`, find the length of the longest increasing subsequence (LIS) such that the difference between consecutive elements in the subsequence is at most `k`.

Example:
Input: nums = [1, 3, 2, 4, 5], k = 1
Output: 4
Explanation: The longest increasing subsequence is [1, 2, 3, 4] or [2, 3, 4, 5].

Input: nums = [1, 5, 2, 4, 3], k = 2
Output: 3
Explanation: The longest increasing subsequence is [1, 2, 3], [1, 2, 4], or [1, 3, 4].

Input: nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6], k = 3
Output: 6
Explanation: The longest increasing subsequence is [1, 2, 3, 4, 5, 6].
'''

# Solution
def longest_increasing_subsequence_with_k_difference(nums, k):
    """
    Finds the length of the longest increasing subsequence with a maximum difference of k.

    Args:
        nums: A list of integers.
        k: The maximum difference between consecutive elements in the subsequence.

    Returns:
        The length of the longest increasing subsequence.
    """

    n = len(nums)
    if n == 0:
        return 0

    # dp[i] stores the length of the longest increasing subsequence ending at nums[i].
    dp = [1] * n

    # Iterate through the array, building up the dp table.
    for i in range(1, n):
        for j in range(i):
            # If nums[i] is greater than nums[j] and the difference is at most k,
            # then we can extend the subsequence ending at nums[j] by including nums[i].
            if nums[i] > nums[j] and nums[i] - nums[j] <= k:
                dp[i] = max(dp[i], dp[j] + 1)

    # The maximum value in the dp table is the length of the longest increasing subsequence.
    return max(dp)

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_k_difference([1, 3, 2, 4, 5], 1) == 4
    assert longest_increasing_subsequence_with_k_difference([1, 5, 2, 4, 3], 2) == 3
    assert longest_increasing_subsequence_with_k_difference([1, 10, 2, 9, 3, 8, 4, 7, 5, 6], 3) == 6
    assert longest_increasing_subsequence_with_k_difference([1, 2, 3, 4, 5], 0) == 1
    assert longest_increasing_subsequence_with_k_difference([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_k_difference([1, 2, 3, 4, 5], 5) == 5
    assert longest_increasing_subsequence_with_k_difference([], 1) == 0
    assert longest_increasing_subsequence_with_k_difference([1], 1) == 1
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()