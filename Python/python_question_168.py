# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) where the difference between consecutive elements in the subsequence is exactly `k`.

Example:
Input: nums = [3, 10, 3, 6, 7, 8], k = 3
Output: 3
Explanation: The longest increasing subsequence with a difference of 3 is [3, 6, 9], which has length 3.  Note that 3, 6, 7 is not a valid subsequence because 7-6 != 3. In the given array, the subsequence [3, 6, 9] can be found with 3 at index 0, 6 at index 3, and 9 (not in the array, but implied in the subsequence).  Another valid subsequence is [3, 6] which has length 2.  The subsequence [7] has length 1. The longest is thus [3,6,9] or length 3.

Input: nums = [1, 5, 9, 2, 6, 10], k = 4
Output: 3
Explanation: The longest increasing subsequence with a difference of 4 is [1, 5, 9], which has length 3.
'''

# Solution
def longest_increasing_subsequence_with_difference(nums, k):
    """
    Finds the length of the longest increasing subsequence (LIS) where the difference
    between consecutive elements in the subsequence is exactly `k`.

    Args:
        nums: A list of integers.
        k: The required difference between consecutive elements.

    Returns:
        The length of the longest increasing subsequence with difference `k`.
    """

    # dp[num] stores the length of the longest increasing subsequence ending at num
    # with the required difference k.
    dp = {}

    max_len = 0  # Initialize the maximum length to 0

    for num in nums:
        # If num - k is in dp, it means we can extend a subsequence ending at num - k.
        if num - k in dp:
            dp[num] = dp[num - k] + 1  # Extend the subsequence by adding num
        else:
            dp[num] = 1  # Start a new subsequence with num

        max_len = max(max_len, dp[num])  # Update the maximum length

    return max_len  # Return the maximum length

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_difference([3, 10, 3, 6, 7, 8], 3) == 3
    assert longest_increasing_subsequence_with_difference([1, 5, 9, 2, 6, 10], 4) == 3
    assert longest_increasing_subsequence_with_difference([1, 2, 3, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_difference([1, 2, 3, 4, 5], 2) == 3
    assert longest_increasing_subsequence_with_difference([1, 2, 3, 4, 5], 3) == 2
    assert longest_increasing_subsequence_with_difference([1, 2, 3, 4, 5], 4) == 1
    assert longest_increasing_subsequence_with_difference([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_difference([5, 4, 3, 2, 1], -1) == 5
    assert longest_increasing_subsequence_with_difference([1, 1, 1, 1, 1], 0) == 5
    assert longest_increasing_subsequence_with_difference([1, 1, 1, 1, 1], 1) == 1
    assert longest_increasing_subsequence_with_difference([], 1) == 0
    assert longest_increasing_subsequence_with_difference([5], 2) == 1
    assert longest_increasing_subsequence_with_difference([1,4,7,10], 3) == 4
    assert longest_increasing_subsequence_with_difference([1,4,7,10,2,5,8,11], 3) == 4
    assert longest_increasing_subsequence_with_difference([0,2,4,6,8,10], 2) == 6
    assert longest_increasing_subsequence_with_difference([10,8,6,4,2,0], -2) == 6
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()