# Python Question: Find the Longest Increasing Subsequence with Specific Conditions
'''
Given an array of integers `nums`, find the length of the longest strictly increasing subsequence such that the difference between any two consecutive elements in the subsequence is a multiple of `k`.

Example:
Input: nums = [3, 6, 7, 12, 13, 18], k = 3
Output: 4
Explanation: The longest increasing subsequence is [3, 6, 12, 18].
'''

# Solution
def longest_increasing_subsequence_with_k_difference(nums, k):
    """
    Finds the length of the longest increasing subsequence where the difference
    between consecutive elements is a multiple of k.

    Args:
        nums: A list of integers.
        k: An integer representing the multiple difference.

    Returns:
        The length of the longest increasing subsequence.
    """

    if not nums:
        return 0

    n = len(nums)
    # dp[i] stores the length of the longest increasing subsequence ending at nums[i].
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            # Check if nums[i] > nums[j] and if the difference is a multiple of k.
            if nums[i] > nums[j] and (nums[i] - nums[j]) % k == 0:
                # Update dp[i] if we find a longer subsequence ending at nums[i].
                dp[i] = max(dp[i], dp[j] + 1)

    # Return the maximum value in the dp array, which represents the length of the
    # longest increasing subsequence.
    return max(dp)

# Test cases
def test_longest_increasing_subsequence_with_k_difference():
    assert longest_increasing_subsequence_with_k_difference([3, 6, 7, 12, 13, 18], 3) == 4
    assert longest_increasing_subsequence_with_k_difference([1, 2, 3, 4, 5, 6], 1) == 6
    assert longest_increasing_subsequence_with_k_difference([1, 2, 3, 4, 5, 6], 2) == 3
    assert longest_increasing_subsequence_with_k_difference([1, 2, 3, 4, 5, 6], 3) == 2
    assert longest_increasing_subsequence_with_k_difference([10, 22, 9, 33, 21, 50, 41, 60, 80], 10) == 3
    assert longest_increasing_subsequence_with_k_difference([1, 5, 9, 13, 17], 4) == 5
    assert longest_increasing_subsequence_with_k_difference([1, 2, 3, 4, 5], 6) == 1
    assert longest_increasing_subsequence_with_k_difference([], 5) == 0
    assert longest_increasing_subsequence_with_k_difference([5], 5) == 1
    assert longest_increasing_subsequence_with_k_difference([2, 4, 6, 8, 10], 2) == 5
    assert longest_increasing_subsequence_with_k_difference([2, 4, 6, 8, 10], 3) == 1
    assert longest_increasing_subsequence_with_k_difference([2, 4, 6, 9, 11, 14], 2) == 4
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_increasing_subsequence_with_k_difference()