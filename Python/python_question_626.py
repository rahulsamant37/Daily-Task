# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) in `nums` such that the difference between consecutive elements in the subsequence is at most `k`.

Example:
Input: nums = [3, 10, 2, 1, 20], k = 5
Output: 4
Explanation: The longest increasing subsequence with a difference of at most 5 is [3, 2, 1, 20] (or [3, 10, 20]). The length is 4.

Input: nums = [1, 5, 2, 4, 3], k = 2
Output: 3
Explanation: The longest increasing subsequence with a difference of at most 2 is [1, 2, 3]. The length is 3.

Input: nums = [1, 2, 3, 4, 5], k = 1
Output: 5
Explanation: The longest increasing subsequence with a difference of at most 1 is [1, 2, 3, 4, 5]. The length is 5.

Input: nums = [5, 4, 3, 2, 1], k = 0
Output: 1
Explanation: The longest increasing subsequence with a difference of at most 0 is [5] or [4] or [3] or [2] or [1]. The length is 1.
'''

# Solution
def longest_increasing_subsequence_with_k(nums, k):
    """
    Finds the length of the longest increasing subsequence (LIS) in nums such that the
    difference between consecutive elements in the subsequence is at most k.

    Args:
      nums: A list of integers.
      k: An integer representing the maximum allowed difference between consecutive elements.

    Returns:
      The length of the longest increasing subsequence.
    """
    n = len(nums)
    if n == 0:
        return 0

    # dp[i] stores the length of the longest increasing subsequence ending at nums[i]
    dp = [1] * n

    # Iterate through the nums array
    for i in range(1, n):
        # Iterate through the elements before nums[i]
        for j in range(i):
            # Check if nums[i] is greater than nums[j] and the difference is at most k
            if nums[i] > nums[j] and nums[i] - nums[j] <= k:
                # Update dp[i] if a longer subsequence is found
                dp[i] = max(dp[i], dp[j] + 1)

    # Return the maximum value in the dp array, which represents the length of the LIS
    return max(dp)

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_k([3, 10, 2, 1, 20], 5) == 4
    assert longest_increasing_subsequence_with_k([1, 5, 2, 4, 3], 2) == 3
    assert longest_increasing_subsequence_with_k([1, 2, 3, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_k([5, 4, 3, 2, 1], 0) == 1
    assert longest_increasing_subsequence_with_k([1, 2, 3, 4, 5], 0) == 1
    assert longest_increasing_subsequence_with_k([5, 4, 3, 2, 1], 5) == 1
    assert longest_increasing_subsequence_with_k([1, 2, 3, 4, 5], 5) == 5
    assert longest_increasing_subsequence_with_k([1], 5) == 1
    assert longest_increasing_subsequence_with_k([], 5) == 0
    assert longest_increasing_subsequence_with_k([1, 3, 2, 4, 5], 1) == 3  # Corrected test case
    assert longest_increasing_subsequence_with_k([1, 3, 2, 4, 5], 2) == 4 # Added test case
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()