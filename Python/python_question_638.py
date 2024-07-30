# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) with a twist.  The twist is that for any two consecutive elements `nums[i]` and `nums[j]` in the subsequence (where `i < j`), it must hold that `nums[j] - nums[i] >= k`.

Example:
Input: nums = [1, 3, 2, 4, 5], k = 2
Output: 3
Explanation: The longest increasing subsequence with the given condition is [1, 3, 5] or [1, 4, 5].

Input: nums = [10, 22, 9, 33, 21, 50, 41, 60, 80], k = 3
Output: 6
Explanation: One possible longest increasing subsequence is [10, 22, 33, 41, 60, 80].

Input: nums = [1, 2, 3, 4, 5], k = 0
Output: 5
Explanation: The longest increasing subsequence is the entire array [1, 2, 3, 4, 5].

Input: nums = [5, 4, 3, 2, 1], k = 1
Output: 1
Explanation: The longest increasing subsequence can only be of length 1, e.g., [5].
'''

# Solution
def longest_increasing_subsequence_with_twist(nums, k):
    """
    Finds the length of the longest increasing subsequence (LIS) with a twist.
    The twist is that for any two consecutive elements nums[i] and nums[j] in the
    subsequence (where i < j), it must hold that nums[j] - nums[i] >= k.

    Args:
        nums: A list of integers.
        k: An integer representing the minimum difference between consecutive elements.

    Returns:
        The length of the longest increasing subsequence with the twist.
    """

    n = len(nums)
    if n == 0:
        return 0

    # dp[i] stores the length of the longest increasing subsequence ending at nums[i]
    dp = [1] * n

    # Iterate through the array to build the dp table
    for i in range(1, n):
        for j in range(i):
            # Check if nums[i] can extend the subsequence ending at nums[j]
            if nums[i] > nums[j] and nums[i] - nums[j] >= k:
                dp[i] = max(dp[i], dp[j] + 1)

    # The maximum value in the dp table is the length of the LIS
    return max(dp)


# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_twist([1, 3, 2, 4, 5], 2) == 3
    assert longest_increasing_subsequence_with_twist([10, 22, 9, 33, 21, 50, 41, 60, 80], 3) == 6
    assert longest_increasing_subsequence_with_twist([1, 2, 3, 4, 5], 0) == 5
    assert longest_increasing_subsequence_with_twist([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_twist([1, 2, 3, 4, 5], 2) == 3
    assert longest_increasing_subsequence_with_twist([1], 1) == 1
    assert longest_increasing_subsequence_with_twist([], 1) == 0
    assert longest_increasing_subsequence_with_twist([1, 1, 1, 1, 1], 1) == 1
    assert longest_increasing_subsequence_with_twist([1, 1, 1, 1, 1], 0) == 1
    assert longest_increasing_subsequence_with_twist([1, 5, 2, 6, 3, 7, 4, 8], 3) == 4
    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()