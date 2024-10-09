# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) where the difference between consecutive elements in the subsequence is at most `k`.

Example:
Input: nums = [3, 10, 2, 1, 20], k = 5
Output: 3
Explanation: The longest increasing subsequence with a difference at most 5 is [3, 10, 20] (or [2, 10, 20], or [1, 2, 10] etc.). Length is 3.
Input: nums = [1, 5, 2, 4, 3], k = 1
Output: 2
Explanation: The longest increasing subsequence with a difference at most 1 is [1, 2, 3] (or [2, 3, 4]). Length is 3.
Input: nums = [1, 2, 3, 4, 5], k = 0
Output: 1
Explanation: The longest increasing subsequence with a difference at most 0 is [1], [2], [3], [4] or [5]. Length is 1.
'''

# Solution
def longest_increasing_subsequence_with_k_difference(nums, k):
    """
    Finds the length of the longest increasing subsequence (LIS) where the difference
    between consecutive elements in the subsequence is at most k.

    Args:
        nums: A list of integers.
        k: The maximum allowed difference between consecutive elements in the subsequence.

    Returns:
        The length of the longest increasing subsequence with the specified constraint.
    """

    n = len(nums)
    if n == 0:
        return 0

    # dp[i] stores the length of the longest increasing subsequence ending at nums[i]
    dp = [1] * n  # Initialize each element to 1, as each element itself forms a subsequence of length 1

    # Iterate through the array to build the dp array
    for i in range(1, n):
        for j in range(i):
            # If nums[i] is greater than nums[j] and the difference is at most k,
            # then we can extend the subsequence ending at nums[j] to include nums[i]
            if nums[i] > nums[j] and nums[i] - nums[j] <= k:
                dp[i] = max(dp[i], dp[j] + 1)

    # The maximum value in the dp array is the length of the LIS with the specified constraint
    return max(dp)

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_k_difference([3, 10, 2, 1, 20], 5) == 3
    assert longest_increasing_subsequence_with_k_difference([1, 5, 2, 4, 3], 1) == 2
    assert longest_increasing_subsequence_with_k_difference([1, 2, 3, 4, 5], 0) == 1
    assert longest_increasing_subsequence_with_k_difference([10, 22, 9, 33, 21, 50, 41, 60, 80], 5) == 5
    assert longest_increasing_subsequence_with_k_difference([1, 2, 3, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_k_difference([], 5) == 0
    assert longest_increasing_subsequence_with_k_difference([5], 5) == 1
    assert longest_increasing_subsequence_with_k_difference([1, 1, 1, 1, 1], 0) == 1
    assert longest_increasing_subsequence_with_k_difference([1, 2, 3, 10, 11, 12], 1) == 3
    assert longest_increasing_subsequence_with_k_difference([1, 3, 5, 2, 4, 6], 1) == 2
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()