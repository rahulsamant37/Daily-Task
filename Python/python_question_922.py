# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) with the additional constraint:
For any two consecutive elements `nums[i]` and `nums[j]` in the subsequence (where i < j), `nums[j] - nums[i] >= k`.

Example:
Input: nums = [1, 3, 2, 4, 5], k = 2
Output: 3
Explanation: The longest increasing subsequence satisfying the condition is [1, 3, 5] or [1, 4, 5].

Input: nums = [1, 2, 3, 4, 5], k = 3
Output: 2
Explanation: The longest increasing subsequence satisfying the condition is [1, 4] or [2, 5] or [1,5].

Input: nums = [5, 4, 3, 2, 1], k = 1
Output: 1
Explanation: Since the array is decreasing, we can only pick one element at a time.
'''

# Solution
def longest_increasing_subsequence_with_k(nums, k):
    """
    Finds the length of the longest increasing subsequence with a difference constraint.

    Args:
        nums: A list of integers.
        k: The minimum difference between consecutive elements in the subsequence.

    Returns:
        The length of the longest increasing subsequence satisfying the condition.
    """

    n = len(nums)
    if n == 0:
        return 0

    # dp[i] stores the length of the longest increasing subsequence ending at nums[i]
    dp = [1] * n

    # Iterate through the array to build the dp table
    for i in range(1, n):
        # Iterate through all previous elements to check if they can be part of the subsequence
        for j in range(i):
            # Check if nums[i] can extend the subsequence ending at nums[j]
            if nums[i] > nums[j] and nums[i] - nums[j] >= k:
                # If it can, update dp[i] if necessary
                dp[i] = max(dp[i], dp[j] + 1)

    # The maximum value in the dp table is the length of the LIS
    return max(dp)


# Test cases
def test_longest_increasing_subsequence_with_k():
    assert longest_increasing_subsequence_with_k([1, 3, 2, 4, 5], 2) == 3
    assert longest_increasing_subsequence_with_k([1, 2, 3, 4, 5], 3) == 2
    assert longest_increasing_subsequence_with_k([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_k([1, 5, 2, 4, 3], 2) == 2
    assert longest_increasing_subsequence_with_k([1, 2, 3, 4, 5], 0) == 5
    assert longest_increasing_subsequence_with_k([], 1) == 0
    assert longest_increasing_subsequence_with_k([1], 1) == 1
    assert longest_increasing_subsequence_with_k([1, 1, 1, 1, 1], 1) == 1
    assert longest_increasing_subsequence_with_k([1, 4, 2, 5, 3, 6], 2) == 3
    assert longest_increasing_subsequence_with_k([1, 10, 2, 9, 3, 8, 4, 7, 5, 6], 3) == 5

    print("All test cases passed!")


if __name__ == "__main__":
    test_longest_increasing_subsequence_with_k()