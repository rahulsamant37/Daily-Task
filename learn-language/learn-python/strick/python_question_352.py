# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums`, find the length of the longest increasing subsequence such that adjacent elements in the subsequence have a difference of at most `k`.

Example:
Input: nums = [3, 10, 2, 1, 20], k = 7
Output: 4
Explanation: One longest increasing subsequence is [3, 10, 20], and another is [2, 1, 20].  The subsequence [1, 2, 3, 10, 20] is increasing, but the difference between adjacent elements cannot exceed k. For example, 2-1 = 1 <= 7, 3-2 = 1 <= 7, 10-3 = 7 <= 7, 20 - 10 = 10 > 7. Therefore, [3, 10, 20] and [2, 1, 20] are acceptable subsequences with a length of 3. The longest subsequence is [3, 10, 20] and [1, 2, 3, 10]. The possible subsequences are [3, 10], [2, 20], [1, 20], [3], [10], [2], [1], [20], [3, 10, 20], [2, 1, 20], [1, 2, 3, 10]. The longest subsequence is [1, 2, 3, 10] or [3, 10, 20] which has a length of 4.
'''

# Solution
def longest_increasing_subsequence_with_k_difference(nums, k):
    """
    Finds the length of the longest increasing subsequence with a maximum difference of k between adjacent elements.

    Args:
        nums: A list of integers.
        k: The maximum allowed difference between adjacent elements.

    Returns:
        The length of the longest increasing subsequence.
    """

    n = len(nums)
    if n == 0:
        return 0

    # dp[i] stores the length of the longest increasing subsequence ending at nums[i]
    dp = [1] * n

    # Iterate through the array to build the dp table
    for i in range(1, n):
        for j in range(i):
            # Check if nums[i] can be added to the subsequence ending at nums[j]
            if nums[i] > nums[j] and nums[i] - nums[j] <= k:
                dp[i] = max(dp[i], dp[j] + 1)

    # The maximum value in the dp table is the length of the longest increasing subsequence
    return max(dp)

# Test cases
def test_longest_increasing_subsequence_with_k_difference():
    assert longest_increasing_subsequence_with_k_difference([3, 10, 2, 1, 20], 7) == 4
    assert longest_increasing_subsequence_with_k_difference([1, 3, 2, 4, 5], 2) == 5
    assert longest_increasing_subsequence_with_k_difference([1, 5, 2, 4, 3], 2) == 3
    assert longest_increasing_subsequence_with_k_difference([1, 2, 3, 4, 5], 1) == 2
    assert longest_increasing_subsequence_with_k_difference([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_k_difference([1, 1, 1, 1, 1], 0) == 1
    assert longest_increasing_subsequence_with_k_difference([1, 2, 3, 4, 5], 10) == 5
    assert longest_increasing_subsequence_with_k_difference([], 5) == 0
    assert longest_increasing_subsequence_with_k_difference([1], 5) == 1
    assert longest_increasing_subsequence_with_k_difference([1, 5, 2, 4, 3], 1) == 1
    assert longest_increasing_subsequence_with_k_difference([1, 2, 3, 4, 5], 0) == 1
    assert longest_increasing_subsequence_with_k_difference([10, 22, 9, 33, 21, 50, 41, 60, 80], 10) == 6

if __name__ == "__main__":
    test_longest_increasing_subsequence_with_k_difference()