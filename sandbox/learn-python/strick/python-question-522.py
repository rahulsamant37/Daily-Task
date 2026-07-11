# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums`, find the length of the longest increasing subsequence (LIS) such that the difference between consecutive elements in the subsequence is at most `k`.

Example:
Input: nums = [1, 3, 2, 4, 5], k = 1
Output: 4
Explanation: The longest increasing subsequence with difference at most 1 is [1, 2, 3, 4] or [2,3,4,5] or [1,2,3,4]. Its length is 4.

Input: nums = [1, 5, 2, 4, 3], k = 2
Output: 3
Explanation: The longest increasing subsequence with difference at most 2 is [1, 2, 3] or [2, 4, 5]. Its length is 3.
'''

# Solution
def longest_increasing_subsequence_with_k_difference(nums, k):
    """
    Finds the length of the longest increasing subsequence in nums such that the difference between consecutive elements is at most k.

    Args:
        nums: A list of integers.
        k: The maximum allowed difference between consecutive elements in the subsequence.

    Returns:
        The length of the longest increasing subsequence with the given constraint.
    """

    if not nums:
        return 0

    n = len(nums)
    # dp[i] stores the length of the longest increasing subsequence ending at nums[i]
    dp = [1] * n

    # Iterate through the array
    for i in range(1, n):
        # For each element nums[i], iterate through the elements before it
        for j in range(i):
            # If nums[i] is greater than nums[j] and their difference is at most k
            if nums[i] > nums[j] and nums[i] - nums[j] <= k:
                # Update dp[i] to be the maximum of its current value and dp[j] + 1
                dp[i] = max(dp[i], dp[j] + 1)

    # The maximum value in dp is the length of the longest increasing subsequence
    return max(dp)

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_k_difference([1, 3, 2, 4, 5], 1) == 4
    assert longest_increasing_subsequence_with_k_difference([1, 5, 2, 4, 3], 2) == 3
    assert longest_increasing_subsequence_with_k_difference([1, 2, 3, 4, 5], 0) == 1
    assert longest_increasing_subsequence_with_k_difference([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_k_difference([1, 2, 3, 4, 5], 2) == 3
    assert longest_increasing_subsequence_with_k_difference([], 2) == 0
    assert longest_increasing_subsequence_with_k_difference([1], 2) == 1
    assert longest_increasing_subsequence_with_k_difference([1, 1, 1, 1, 1], 0) == 1
    assert longest_increasing_subsequence_with_k_difference([1, 3, 5, 7, 9], 2) == 3
    assert longest_increasing_subsequence_with_k_difference([10, 22, 9, 33, 21, 50, 41, 60, 80], 10) == 6
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()