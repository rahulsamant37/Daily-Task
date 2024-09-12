# Python Question: Longest Increasing Subsequence with Limited Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence (LIS) where the difference between any two consecutive elements in the subsequence is at most `diff`.

Example:
Input: nums = [1, 3, 2, 4, 5], diff = 1
Output: 4
Explanation: One possible LIS is [1, 2, 3, 4].  Another is [2,3,4,5]. The length is 4.

Input: nums = [1, 5, 2, 6, 3, 7], diff = 2
Output: 4
Explanation: One possible LIS is [1, 2, 3, 5]. Another is [5, 6, 7]. The length is 3. [1,2,3] or [5,6,7]. [1, 2, 3, 5] is not a valid subsequence since 5-3 > 2. A valid LIS with length 4 is [1, 2, 3, 4] if we had 4 in the input. An LIS of length 4 in the input is [1, 2, 3, 5] is *not* valid because 5-3>2.  The longest valid LIS is [5, 6, 7] or [1,2,3] or [2,3,5]
'''

# Solution
def longest_increasing_subsequence_with_limited_difference(nums, diff):
    """
    Finds the length of the longest increasing subsequence with limited difference.

    Args:
        nums: A list of integers.
        diff: The maximum allowed difference between consecutive elements in the subsequence.

    Returns:
        The length of the longest increasing subsequence with limited difference.
    """
    n = len(nums)
    if n == 0:
        return 0

    # dp[i] stores the length of the longest increasing subsequence ending at nums[i]
    dp = [1] * n

    # Iterate through the array
    for i in range(1, n):
        # Iterate through the elements before nums[i]
        for j in range(i):
            # If nums[i] is greater than nums[j] and the difference is within the limit
            if nums[i] > nums[j] and nums[i] - nums[j] <= diff:
                # Update the length of the LIS ending at nums[i]
                dp[i] = max(dp[i], dp[j] + 1)

    # Return the maximum length among all LIS
    return max(dp)

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_limited_difference([1, 3, 2, 4, 5], 1) == 4
    assert longest_increasing_subsequence_with_limited_difference([1, 5, 2, 6, 3, 7], 2) == 3
    assert longest_increasing_subsequence_with_limited_difference([1, 2, 3, 4, 5], 0) == 1
    assert longest_increasing_subsequence_with_limited_difference([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_limited_difference([1, 1, 1, 1, 1], 0) == 1
    assert longest_increasing_subsequence_with_limited_difference([1, 2, 4, 6, 8], 2) == 3
    assert longest_increasing_subsequence_with_limited_difference([10, 22, 9, 33, 21, 50, 41, 60, 80], 5) == 5
    assert longest_increasing_subsequence_with_limited_difference([], 5) == 0
    assert longest_increasing_subsequence_with_limited_difference([1], 5) == 1
    assert longest_increasing_subsequence_with_limited_difference([1,3,5], 2) == 2

if __name__ == "__main__":
    test_solution()