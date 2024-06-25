# Python Question: Longest Increasing Subsequence with Limited Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence (LIS) such that the difference between consecutive elements in the subsequence is at most `diff`.

Example:
Input: nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], diff = 2
Output: 4
Explanation: One possible LIS is [1, 1, 2, 3], where the differences are 0, 1, 1, which are all <= 2. Another is [3, 4, 5, 6]. The length is 4.
'''

# Solution
def longest_increasing_subsequence_with_limited_difference(nums, diff):
    """
    Finds the length of the longest increasing subsequence with a limited difference.

    Args:
        nums: A list of integers.
        diff: The maximum allowed difference between consecutive elements in the subsequence.

    Returns:
        The length of the longest increasing subsequence.
    """
    n = len(nums)
    if n == 0:
        return 0

    # dp[i] stores the length of the LIS ending at nums[i]
    dp = [1] * n

    # Iterate through the array
    for i in range(1, n):
        # Iterate through all previous elements
        for j in range(i):
            # If nums[i] is greater than nums[j] and the difference is within the limit
            if nums[i] > nums[j] and nums[i] - nums[j] <= diff:
                # Update dp[i] if we can extend the LIS ending at nums[j]
                dp[i] = max(dp[i], dp[j] + 1)

    # Return the maximum value in the dp array
    return max(dp)

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_limited_difference([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 2) == 4
    assert longest_increasing_subsequence_with_limited_difference([1, 2, 3, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_limited_difference([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_limited_difference([1, 5, 2, 4, 3], 2) == 3
    assert longest_increasing_subsequence_with_limited_difference([], 2) == 0
    assert longest_increasing_subsequence_with_limited_difference([1], 2) == 1
    assert longest_increasing_subsequence_with_limited_difference([1, 1, 1, 1, 1], 0) == 1
    assert longest_increasing_subsequence_with_limited_difference([1, 3, 2, 4, 5], 1) == 3
    assert longest_increasing_subsequence_with_limited_difference([1, 3, 2, 4, 5], 2) == 4
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()