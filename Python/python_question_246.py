# Python Question: Find the Longest Increasing Subsequence with a Constraint
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) such that the difference between any two consecutive elements in the subsequence is at most `k`.

Example:
Input: nums = [1, 3, 2, 4, 5], k = 1
Output: 4
Explanation: The longest increasing subsequence is [1, 2, 3, 4] or [2, 3, 4, 5].  The length is 4.

Input: nums = [1, 5, 2, 4, 3], k = 2
Output: 3
Explanation: The longest increasing subsequence is [1, 2, 3], [1, 2, 4], [1, 3, 4]. The length is 3.

Input: nums = [1, 10, 2, 3, 4, 5], k = 1
Output: 4
Explanation: The longest increasing subsequence is [2, 3, 4, 5]. The length is 4.

Input: nums = [1, 5, 2, 4, 3], k = 0
Output: 1
Explanation: The longest increasing subsequence is [1], [5], [2], [4], or [3]. The length is 1.
'''

# Solution
def solution(nums, k):
    """
    Finds the length of the longest increasing subsequence with a difference constraint.

    Args:
        nums: A list of integers.
        k: The maximum allowed difference between consecutive elements.

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
        # Iterate through the elements before nums[i]
        for j in range(i):
            # Check if nums[i] is greater than nums[j] and their difference is at most k
            if nums[i] > nums[j] and nums[i] - nums[j] <= k:
                # If so, update dp[i] if adding nums[i] to the subsequence ending at nums[j]
                # results in a longer subsequence
                dp[i] = max(dp[i], dp[j] + 1)

    # Return the maximum value in the dp array, which represents the length of the LIS
    return max(dp)

# Test cases
def test_solution():
    assert solution([1, 3, 2, 4, 5], 1) == 4
    assert solution([1, 5, 2, 4, 3], 2) == 3
    assert solution([1, 10, 2, 3, 4, 5], 1) == 4
    assert solution([1, 5, 2, 4, 3], 0) == 1
    assert solution([1, 2, 3, 4, 5], 2) == 5
    assert solution([5, 4, 3, 2, 1], 1) == 1
    assert solution([1, 2, 3, 5, 6, 7], 1) == 3
    assert solution([1, 2, 3, 5, 6, 7], 2) == 5
    assert solution([1, 2, 3, 5, 6, 7], 3) == 6
    assert solution([4, 2, 3, 1, 5], 1) == 2
    assert solution([], 1) == 0
    assert solution([1], 1) == 1
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()