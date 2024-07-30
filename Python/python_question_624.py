# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums`, find the length of the longest increasing subsequence such that the difference between any two consecutive elements in the subsequence is less than or equal to a given integer `k`.

Example:
Input: nums = [3, 10, 2, 1, 20], k = 5
Output: 3
Explanation: The longest increasing subsequence satisfying the condition is [3, 10, 20] or [1, 2, 3]. The length is 3. Other increasing subsequences like [1, 2] satisfy the increasing and difference condition.
'''

# Solution
def longest_increasing_subsequence_with_k_difference(nums, k):
    """
    Finds the length of the longest increasing subsequence such that the difference
    between any two consecutive elements is less than or equal to k.

    Args:
        nums: A list of integers.
        k: The maximum allowed difference between consecutive elements.

    Returns:
        The length of the longest increasing subsequence satisfying the condition.
    """
    if not nums:
        return 0

    n = len(nums)
    # dp[i] stores the length of the longest increasing subsequence ending at nums[i].
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            # Check if nums[i] is greater than nums[j] and the difference is less than or equal to k.
            if nums[i] > nums[j] and nums[i] - nums[j] <= k:
                # If it is, update dp[i] to be the maximum of its current value and dp[j] + 1.
                dp[i] = max(dp[i], dp[j] + 1)

    # The maximum value in dp is the length of the longest increasing subsequence.
    return max(dp)

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_k_difference([3, 10, 2, 1, 20], 5) == 3
    assert longest_increasing_subsequence_with_k_difference([1, 2, 3, 4, 5], 1) == 2
    assert longest_increasing_subsequence_with_k_difference([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_k_difference([1, 5, 2, 6, 3, 7, 4, 8], 2) == 4
    assert longest_increasing_subsequence_with_k_difference([1, 2, 3, 4, 5], 0) == 1
    assert longest_increasing_subsequence_with_k_difference([], 5) == 0
    assert longest_increasing_subsequence_with_k_difference([1], 5) == 1
    assert longest_increasing_subsequence_with_k_difference([1, 1, 1, 1, 1], 0) == 1
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()