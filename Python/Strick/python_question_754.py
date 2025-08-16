# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) with the following constraint:

For any two consecutive elements `nums[i]` and `nums[j]` in the LIS (where i < j), `nums[j] - nums[i] >= k`.

Example:

Input: nums = [1, 3, 2, 4, 5], k = 2
Output: 3
Explanation: The longest increasing subsequence satisfying the condition is [1, 3, 5] or [1, 4, 5].

Input: nums = [1, 2, 3, 4, 5], k = 3
Output: 2
Explanation: The longest increasing subsequence satisfying the condition is [1, 4], [2, 5] etc.

Input: nums = [5, 4, 3, 2, 1], k = 1
Output: 1
Explanation: Since the array is decreasing, any two consecutive elements will violate the constraint.
'''

# Solution
def longest_increasing_subsequence_with_k_constraint(nums, k):
    """
    Finds the length of the longest increasing subsequence with the given constraint.

    Args:
        nums: A list of integers.
        k: An integer representing the minimum difference between consecutive elements.

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
        for j in range(i):
            # Check if nums[i] can extend the subsequence ending at nums[j]
            if nums[i] > nums[j] and nums[i] - nums[j] >= k:
                dp[i] = max(dp[i], dp[j] + 1)

    # The maximum value in the dp array is the length of the LIS
    return max(dp)

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_k_constraint([1, 3, 2, 4, 5], 2) == 3
    assert longest_increasing_subsequence_with_k_constraint([1, 2, 3, 4, 5], 3) == 2
    assert longest_increasing_subsequence_with_k_constraint([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_k_constraint([1, 5, 2, 4, 3], 2) == 2
    assert longest_increasing_subsequence_with_k_constraint([10, 22, 9, 33, 21, 50, 41, 60, 80], 5) == 5
    assert longest_increasing_subsequence_with_k_constraint([], 5) == 0
    assert longest_increasing_subsequence_with_k_constraint([1], 5) == 1
    assert longest_increasing_subsequence_with_k_constraint([1, 2], 1) == 2
    assert longest_increasing_subsequence_with_k_constraint([1, 2], 2) == 1
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()