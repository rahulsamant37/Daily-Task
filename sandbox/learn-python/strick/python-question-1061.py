# Python Question: Longest Increasing Subsequence with Limited Difference
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) where the difference between consecutive elements in the subsequence is at most `k`.

Example:
Input: nums = [3, 10, 2, 1, 20], k = 5
Output: 3
Explanation: One possible LIS with a difference at most 5 is [3, 2, 1] or [10, 20]. The length is 2. Another possible LIS is [3, 2, 1], The length is 3.

Input: nums = [1, 5, 3, 7, 2, 9], k = 3
Output: 4
Explanation: One possible LIS with a difference at most 3 is [1, 2, 3, 5]. The length is 4.
'''

# Solution
def longest_increasing_subsequence_with_limited_difference(nums, k):
    """
    Calculates the length of the longest increasing subsequence (LIS) with a limited difference.

    Args:
        nums: A list of integers.
        k: The maximum allowed difference between consecutive elements in the LIS.

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
            # Check if nums[i] can extend the LIS ending at nums[j]
            if nums[i] > nums[j] and nums[i] - nums[j] <= k:
                dp[i] = max(dp[i], dp[j] + 1)

    # The maximum value in the dp table is the length of the LIS
    return max(dp)

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_limited_difference([3, 10, 2, 1, 20], 5) == 3
    assert longest_increasing_subsequence_with_limited_difference([1, 5, 3, 7, 2, 9], 3) == 4
    assert longest_increasing_subsequence_with_limited_difference([1, 2, 3, 4, 5], 1) == 2
    assert longest_increasing_subsequence_with_limited_difference([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_limited_difference([1, 5, 2, 6, 3, 7, 4, 8], 2) == 5
    assert longest_increasing_subsequence_with_limited_difference([], 5) == 0
    assert longest_increasing_subsequence_with_limited_difference([1], 5) == 1
    assert longest_increasing_subsequence_with_limited_difference([1, 2], 0) == 1
    assert longest_increasing_subsequence_with_limited_difference([1, 3, 2, 4, 5], 1) == 3
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()