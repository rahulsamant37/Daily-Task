# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums`, find the length of the longest increasing subsequence (LIS) where the difference between consecutive elements in the subsequence is at most `k`.

Example:
Input: nums = [1, 3, 2, 4, 5], k = 1
Output: 4
Explanation: The longest increasing subsequence with a difference of at most 1 is [1, 2, 3, 4] or [2, 3, 4, 5], with length 4.

Input: nums = [1, 5, 2, 4, 3], k = 2
Output: 3
Explanation: The longest increasing subsequence with a difference of at most 2 is [1, 2, 3] or [2, 4, 3], with length 3.

Input: nums = [1, 5, 2, 4, 3], k = 0
Output: 1
Explanation: The longest increasing subsequence with a difference of at most 0 is [1], [5], [2], [4], or [3], with length 1.
'''

# Solution
def longest_increasing_subsequence_with_difference(nums, k):
    """
    Finds the length of the longest increasing subsequence in nums with a difference of at most k.

    Args:
        nums: A list of integers.
        k: The maximum allowed difference between consecutive elements in the subsequence.

    Returns:
        The length of the longest increasing subsequence.
    """

    n = len(nums)
    if n == 0:
        return 0

    # dp[i] stores the length of the longest increasing subsequence ending at index i
    dp = [1] * n

    # Iterate through the array
    for i in range(1, n):
        # Iterate through the elements before index i
        for j in range(i):
            # Check if nums[i] is greater than nums[j] and the difference is at most k
            if nums[i] > nums[j] and (nums[i] - nums[j]) <= k:
                # Update dp[i] if a longer subsequence is found
                dp[i] = max(dp[i], dp[j] + 1)

    # The maximum value in dp is the length of the longest increasing subsequence
    return max(dp)

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_difference([1, 3, 2, 4, 5], 1) == 4
    assert longest_increasing_subsequence_with_difference([1, 5, 2, 4, 3], 2) == 3
    assert longest_increasing_subsequence_with_difference([1, 5, 2, 4, 3], 0) == 1
    assert longest_increasing_subsequence_with_difference([10, 22, 9, 33, 21, 50, 41, 60, 80], 5) == 6
    assert longest_increasing_subsequence_with_difference([1, 2, 3, 4, 5], 0) == 1
    assert longest_increasing_subsequence_with_difference([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_difference([], 1) == 0
    assert longest_increasing_subsequence_with_difference([1], 1) == 1
    assert longest_increasing_subsequence_with_difference([1, 3, 5, 2, 4], 2) == 3
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()