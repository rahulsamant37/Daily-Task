# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums`, find the length of the longest strictly increasing subsequence such that the difference between consecutive elements in the subsequence is at most `k`.

Example:
Input: nums = [1, 3, 2, 4, 5], k = 1
Output: 4
Explanation: The longest increasing subsequence with a difference of at most 1 is [1, 2, 3, 4] or [2, 3, 4, 5].  The length is 4.

Input: nums = [1, 5, 2, 6, 3, 7, 4, 8], k = 2
Output: 4
Explanation: One possible longest increasing subsequence is [1, 2, 3, 4].  Another is [5,6,7,8]. The length is 4.

Input: nums = [1, 2, 3, 4, 5], k = 0
Output: 1
Explanation: Only single elements can be part of the subsequence since the difference must be 0.
'''

# Solution
def longest_increasing_subsequence_with_k_diff(nums, k):
    """
    Finds the length of the longest increasing subsequence with a difference of at most k.

    Args:
        nums: A list of integers.
        k: The maximum allowed difference between consecutive elements in the subsequence.

    Returns:
        The length of the longest increasing subsequence.
    """
    n = len(nums)
    if n == 0:
        return 0

    # dp[i] stores the length of the longest increasing subsequence ending at nums[i]
    dp = [1] * n

    # Iterate through the array
    for i in range(1, n):
        # For each element, iterate through the elements before it
        for j in range(i):
            # If nums[i] is greater than nums[j] and the difference is at most k
            if nums[i] > nums[j] and nums[i] - nums[j] <= k:
                # Update dp[i] if adding nums[i] to the subsequence ending at nums[j] gives a longer subsequence
                dp[i] = max(dp[i], dp[j] + 1)

    # The maximum value in dp is the length of the longest increasing subsequence
    return max(dp)

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_k_diff([1, 3, 2, 4, 5], 1) == 4
    assert longest_increasing_subsequence_with_k_diff([1, 5, 2, 6, 3, 7, 4, 8], 2) == 4
    assert longest_increasing_subsequence_with_k_diff([1, 2, 3, 4, 5], 0) == 1
    assert longest_increasing_subsequence_with_k_diff([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_k_diff([1, 2, 3, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_k_diff([1, 5, 2, 6, 3, 7, 4, 8], 1) == 2
    assert longest_increasing_subsequence_with_k_diff([], 1) == 0
    assert longest_increasing_subsequence_with_k_diff([1], 1) == 1
    assert longest_increasing_subsequence_with_k_diff([1, 3, 5, 7, 9], 2) == 3
    assert longest_increasing_subsequence_with_k_diff([10, 20, 30, 40, 50], 5) == 1
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()