# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) where the difference between consecutive elements in the subsequence is at most `k`.

Example:
Input: nums = [1, 3, 2, 4, 5], k = 1
Output: 4
Explanation: The longest increasing subsequence with a difference of at most 1 is [1, 2, 3, 4] or [2, 3, 4, 5].  Length is 4.

Input: nums = [1, 5, 2, 4, 3], k = 2
Output: 3
Explanation: The longest increasing subsequence with a difference of at most 2 is [1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4], [2, 4], [3,4], [1,5]. Length is 3.

Input: nums = [1, 10, 2, 8, 3, 7, 4, 6, 5], k = 3
Output: 5
Explanation: The longest increasing subsequence with a difference of at most 3 is [1, 2, 3, 4, 5]. Length is 5.
'''

# Solution
def longest_increasing_subsequence_with_k(nums, k):
    """
    Finds the length of the longest increasing subsequence in nums where the difference
    between consecutive elements is at most k.

    Args:
        nums: A list of integers.
        k: The maximum difference allowed between consecutive elements in the subsequence.

    Returns:
        The length of the longest increasing subsequence with the given constraint.
    """

    n = len(nums)
    if n == 0:
        return 0

    # dp[i] stores the length of the longest increasing subsequence ending at nums[i]
    dp = [1] * n

    # Iterate through the array to build the dp table
    for i in range(1, n):
        # For each element, iterate through all previous elements
        for j in range(i):
            # If nums[i] is greater than nums[j] and their difference is at most k,
            # then we can extend the subsequence ending at nums[j]
            if nums[i] > nums[j] and nums[i] - nums[j] <= k:
                dp[i] = max(dp[i], dp[j] + 1)

    # The maximum value in the dp table is the length of the LIS with the given constraint
    return max(dp)

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_k([1, 3, 2, 4, 5], 1) == 4
    assert longest_increasing_subsequence_with_k([1, 5, 2, 4, 3], 2) == 3
    assert longest_increasing_subsequence_with_k([1, 10, 2, 8, 3, 7, 4, 6, 5], 3) == 5
    assert longest_increasing_subsequence_with_k([1, 2, 3, 4, 5], 0) == 1
    assert longest_increasing_subsequence_with_k([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_k([1, 2, 3, 4, 5], 2) == 3
    assert longest_increasing_subsequence_with_k([1, 1, 1, 1, 1], 0) == 1
    assert longest_increasing_subsequence_with_k([], 5) == 0
    assert longest_increasing_subsequence_with_k([1], 5) == 1
    assert longest_increasing_subsequence_with_k([1, 4, 2, 3], 2) == 3
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()