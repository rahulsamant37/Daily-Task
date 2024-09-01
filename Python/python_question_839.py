# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) where the difference between consecutive elements is at most `k`.

Example:
Input: nums = [3, 10, 2, 1, 20], k = 5
Output: 4
Explanation: The longest increasing subsequence with a difference of at most 5 is [3, 2, 1, 20].  Its length is 4.

Input: nums = [1, 3, 5, 2, 4], k = 2
Output: 3
Explanation: The longest increasing subsequence with a difference of at most 2 is [1, 3, 5] or [1, 2, 4]. Its length is 3.

Input: nums = [1, 5, 9, 10, 11], k = 1
Output: 3
Explanation: The longest increasing subsequence with a difference of at most 1 is [9,10,11].
'''

# Solution
def longest_increasing_subsequence_with_k_difference(nums, k):
    """
    Finds the length of the longest increasing subsequence with a difference of at most k.

    Args:
        nums: A list of integers.
        k: An integer representing the maximum allowed difference between consecutive elements.

    Returns:
        The length of the longest increasing subsequence with a difference of at most k.
    """
    if not nums:
        return 0

    n = len(nums)
    # dp[i] stores the length of the longest increasing subsequence ending at nums[i]
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            # Check if nums[i] can be added to the subsequence ending at nums[j]
            if nums[i] > nums[j] and nums[i] - nums[j] <= k:
                dp[i] = max(dp[i], dp[j] + 1)

    # The maximum value in dp is the length of the longest increasing subsequence
    return max(dp)

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_k_difference([3, 10, 2, 1, 20], 5) == 4
    assert longest_increasing_subsequence_with_k_difference([1, 3, 5, 2, 4], 2) == 3
    assert longest_increasing_subsequence_with_k_difference([1, 5, 9, 10, 11], 1) == 3
    assert longest_increasing_subsequence_with_k_difference([1, 2, 3, 4, 5], 0) == 1
    assert longest_increasing_subsequence_with_k_difference([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_k_difference([1, 2, 3, 4, 5], 5) == 5
    assert longest_increasing_subsequence_with_k_difference([], 5) == 0
    assert longest_increasing_subsequence_with_k_difference([1], 5) == 1
    assert longest_increasing_subsequence_with_k_difference([1, 1, 1, 1], 0) == 1
    assert longest_increasing_subsequence_with_k_difference([1, 1, 1, 1], 1) == 1
    assert longest_increasing_subsequence_with_k_difference([1, 2, 4, 8, 16], 3) == 3

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()