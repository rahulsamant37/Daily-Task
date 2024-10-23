# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums`, find the length of the longest increasing subsequence where the difference between consecutive elements in the subsequence must be at most `k`.

Example:
Input: nums = [1, 3, 2, 4, 5], k = 1
Output: 4
Explanation: The longest increasing subsequence with a difference of at most 1 is [1, 2, 3, 4] or [2, 3, 4, 5].

Input: nums = [1, 5, 2, 4, 3], k = 2
Output: 3
Explanation: The longest increasing subsequence with a difference of at most 2 is [1, 2, 3] or [2, 4, 5].

Input: nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6], k = 3
Output: 6
Explanation: The longest increasing subsequence with a difference of at most 3 is [1, 2, 3, 4, 5, 6].
'''

# Solution
def solution(nums, k):
    """
    Finds the length of the longest increasing subsequence with a difference of at most k.

    Args:
      nums: A list of integers.
      k: The maximum difference between consecutive elements in the subsequence.

    Returns:
      The length of the longest increasing subsequence.
    """
    n = len(nums)
    if n == 0:
        return 0

    # dp[i] stores the length of the longest increasing subsequence ending at nums[i]
    dp = [1] * n

    # Iterate through the array to build the dp array
    for i in range(1, n):
        # Iterate through all previous elements
        for j in range(i):
            # If nums[i] is greater than nums[j] and the difference is at most k
            if nums[i] > nums[j] and nums[i] - nums[j] <= k:
                # Update dp[i] if we find a longer subsequence
                dp[i] = max(dp[i], dp[j] + 1)

    # The maximum value in the dp array is the length of the longest increasing subsequence
    return max(dp)

# Test cases
def test_solution():
    assert solution([1, 3, 2, 4, 5], 1) == 4
    assert solution([1, 5, 2, 4, 3], 2) == 3
    assert solution([1, 10, 2, 9, 3, 8, 4, 7, 5, 6], 3) == 6
    assert solution([1, 2, 3, 4, 5], 1) == 5
    assert solution([5, 4, 3, 2, 1], 1) == 1
    assert solution([1, 3, 5, 2, 4, 6], 2) == 4
    assert solution([1], 1) == 1
    assert solution([], 1) == 0
    assert solution([1, 2, 4, 8, 16], 1) == 2
    assert solution([1, 2, 4, 8, 16], 3) == 3
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()