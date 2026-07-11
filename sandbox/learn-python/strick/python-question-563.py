# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) with the following constraint:

For any two consecutive elements `nums[i]` and `nums[j]` in the subsequence (where `i < j`), `nums[j] - nums[i] >= k`.

Example:
Input: nums = [1, 3, 2, 4, 5], k = 2
Output: 3
Explanation: The longest increasing subsequence satisfying the condition is [1, 3, 5].

Input: nums = [1, 5, 2, 4, 3], k = 3
Output: 2
Explanation: The longest increasing subsequence satisfying the condition is [1, 5] or [1, 4].

Input: nums = [1, 2, 3, 4, 5], k = 1
Output: 1
Explanation: No increasing subsequence can be formed with a difference of at least 1 between consecutive elements. Only single elements satisfy the condition.

'''

# Solution
def longest_increasing_subsequence_with_k(nums, k):
    """
    Finds the length of the longest increasing subsequence with a difference of at least k between consecutive elements.

    Args:
        nums: A list of integers.
        k: The minimum difference between consecutive elements.

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
        # Iterate through all previous elements
        for j in range(i):
            # If nums[i] is greater than nums[j] and the difference is at least k
            if nums[i] > nums[j] and nums[i] - nums[j] >= k:
                # Update dp[i] if we can extend the subsequence ending at nums[j]
                dp[i] = max(dp[i], dp[j] + 1)

    # Return the maximum value in dp, which represents the length of the longest increasing subsequence
    return max(dp)

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_k([1, 3, 2, 4, 5], 2) == 3
    assert longest_increasing_subsequence_with_k([1, 5, 2, 4, 3], 3) == 2
    assert longest_increasing_subsequence_with_k([1, 2, 3, 4, 5], 1) == 1
    assert longest_increasing_subsequence_with_k([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_k([1, 2, 3, 4, 5], 0) == 5
    assert longest_increasing_subsequence_with_k([1, 1, 1, 1, 1], 1) == 1
    assert longest_increasing_subsequence_with_k([], 1) == 0
    assert longest_increasing_subsequence_with_k([1], 1) == 1
    assert longest_increasing_subsequence_with_k([1, 4, 2, 5, 3], 2) == 3
    assert longest_increasing_subsequence_with_k([10, 22, 9, 33, 21, 50, 41, 60, 80], 10) == 5
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()