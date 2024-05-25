# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) where the difference between consecutive elements in the subsequence is at most `k`.

Example:
Input: nums = [3, 10, 2, 1, 20], k = 5
Output: 4
Explanation: The longest increasing subsequence with a difference at most 5 is [3, 2, 1, 20] or [1,2,3,10].  The length is 4.

Input: nums = [1, 3, 5, 2, 4], k = 2
Output: 3
Explanation: The longest increasing subsequence with a difference at most 2 is [1, 2, 4]. The length is 3.

Input: nums = [1, 5, 9, 13, 17], k = 3
Output: 1
Explanation: The longest increasing subsequence with a difference at most 3 is [1], [5], [9], [13], or [17]. The length is 1.
'''

# Solution
def longest_increasing_subsequence_with_k_difference(nums, k):
    """
    Finds the length of the longest increasing subsequence (LIS) where the difference
    between consecutive elements in the subsequence is at most `k`.

    Args:
        nums: A list of integers.
        k: The maximum allowed difference between consecutive elements in the LIS.

    Returns:
        The length of the longest increasing subsequence with a difference at most `k`.
    """

    n = len(nums)
    if n == 0:
        return 0

    # dp[i] stores the length of the longest increasing subsequence ending at nums[i]
    dp = [1] * n  # Initialize with 1, as each element itself is a subsequence of length 1

    # Iterate through the array to build the dp table
    for i in range(1, n):
        # For each element, iterate through the elements before it
        for j in range(i):
            # Check if nums[i] is greater than nums[j] and the difference is at most k
            if nums[i] > nums[j] and nums[i] - nums[j] <= k:
                # If so, update dp[i] to be the maximum of its current value and dp[j] + 1
                dp[i] = max(dp[i], dp[j] + 1)

    # The maximum value in the dp table is the length of the LIS
    return max(dp)

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_k_difference([3, 10, 2, 1, 20], 5) == 4
    assert longest_increasing_subsequence_with_k_difference([1, 3, 5, 2, 4], 2) == 3
    assert longest_increasing_subsequence_with_k_difference([1, 5, 9, 13, 17], 3) == 1
    assert longest_increasing_subsequence_with_k_difference([1, 2, 3, 4, 5], 1) == 2
    assert longest_increasing_subsequence_with_k_difference([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_k_difference([], 5) == 0
    assert longest_increasing_subsequence_with_k_difference([1], 5) == 1
    assert longest_increasing_subsequence_with_k_difference([1, 2, 3, 4, 5], 5) == 5
    assert longest_increasing_subsequence_with_k_difference([10, 20, 30, 40, 50], 10) == 5
    assert longest_increasing_subsequence_with_k_difference([1, 2, 3, 10, 11, 12], 1) == 2
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()