# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums`, find the length of the longest increasing subsequence (LIS) such that the difference between consecutive elements in the subsequence is at most `k`.

Example:
Input: nums = [1, 3, 2, 4, 5], k = 1
Output: 4
Explanation: The longest increasing subsequence with a difference of at most 1 is [1, 2, 3, 4] or [2, 3, 4, 5].

Input: nums = [1, 5, 2, 6, 3, 7, 4], k = 2
Output: 4
Explanation: The longest increasing subsequence with a difference of at most 2 is [1, 2, 3, 4], [5,6,7] or [2,3,4].

Input: nums = [1, 2, 3, 4, 5], k = 0
Output: 1
Explanation: The longest increasing subsequence with a difference of at most 0 is [1], [2], [3], [4], or [5].
'''

# Solution
def solution(nums, k):
    """
    Finds the length of the longest increasing subsequence with a difference of at most k.

    Args:
        nums: A list of integers.
        k: The maximum difference allowed between consecutive elements in the subsequence.

    Returns:
        The length of the longest increasing subsequence.
    """

    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n  # dp[i] stores the length of the LIS ending at nums[i]

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j] and nums[i] - nums[j] <= k:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


# Test cases
def test_solution():
    assert solution([1, 3, 2, 4, 5], 1) == 4
    assert solution([1, 5, 2, 6, 3, 7, 4], 2) == 4
    assert solution([1, 2, 3, 4, 5], 0) == 1
    assert solution([5, 4, 3, 2, 1], 1) == 1
    assert solution([1, 1, 1, 1, 1], 0) == 1
    assert solution([1, 2, 3, 4, 5], 1) == 5
    assert solution([], 1) == 0
    assert solution([1], 1) == 1
    assert solution([1, 3, 5, 2, 4, 6], 1) == 3 # Example with overlapping subsequences
    assert solution([10, 22, 9, 33, 21, 50, 41, 60, 80], 5) == 6
    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()