# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) where the difference between consecutive elements is at most `k`.

Example:
Input: nums = [3, 10, 2, 1, 20], k = 5
Output: 4
Explanation: The longest increasing subsequence with a difference of at most 5 is [3, 2, 1, 20] (or [1, 2, 3, 10] or [2,3,10,20]) which has length 4.  Another valid subsequence is [3, 10, 20] which has length 3. [1, 2, 3, 10,20] is increasing, but not a subsequence of the given input.

Input: nums = [1, 5, 2, 4, 3], k = 1
Output: 3
Explanation: The longest increasing subsequence with a difference of at most 1 is [1, 2, 3] which has length 3.  Another valid subsequence is [1,2,4].
'''

# Solution
def longest_increasing_subsequence_with_k(nums, k):
    """
    Finds the length of the longest increasing subsequence (LIS) where the difference
    between consecutive elements is at most k.

    Args:
        nums: A list of integers.
        k: The maximum difference allowed between consecutive elements in the LIS.

    Returns:
        The length of the longest increasing subsequence with the specified constraint.
    """

    n = len(nums)
    if n == 0:
        return 0

    # dp[i] stores the length of the longest increasing subsequence ending at nums[i]
    dp = [1] * n

    # Iterate through the array to build the dp table
    for i in range(1, n):
        for j in range(i):
            # Check if nums[i] is greater than nums[j] and the difference is at most k
            if nums[i] > nums[j] and nums[i] - nums[j] <= k:
                # Update dp[i] if adding nums[i] to the subsequence ending at nums[j]
                # results in a longer increasing subsequence.
                dp[i] = max(dp[i], dp[j] + 1)

    # The maximum value in the dp table is the length of the longest increasing subsequence
    return max(dp)

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_k([3, 10, 2, 1, 20], 5) == 4
    assert longest_increasing_subsequence_with_k([1, 5, 2, 4, 3], 1) == 3
    assert longest_increasing_subsequence_with_k([1, 2, 3, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_k([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_k([1, 5, 2, 4, 3], 0) == 1
    assert longest_increasing_subsequence_with_k([1, 1, 1, 1, 1], 0) == 1
    assert longest_increasing_subsequence_with_k([], 5) == 0
    assert longest_increasing_subsequence_with_k([1], 5) == 1
    assert longest_increasing_subsequence_with_k([1, 6, 2, 7, 3, 8], 2) == 4
    assert longest_increasing_subsequence_with_k([1, 5, 2, 4, 3, 6, 7, 8, 9, 10], 1) == 3
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()