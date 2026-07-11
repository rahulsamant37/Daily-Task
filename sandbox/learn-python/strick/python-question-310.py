# Python Question: Longest Increasing Subsequence with Constraints
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest strictly increasing subsequence (LIS) such that the difference between consecutive elements in the subsequence is at most `k`.

Example:
Input: nums = [3, 10, 2, 1, 20], k = 7
Output: 4
Explanation: The longest increasing subsequence with a difference of at most 7 is [3, 10, 20], which has length 3.
Another possible longest increasing subsequence is [1, 2, 3, 10] which has length 4.

Input: nums = [4, 2, 1, 4, 3, 4, 5, 8, 15], k = 3
Output: 5
Explanation: The longest increasing subsequence with a difference of at most 3 is [1, 3, 4, 5, 8], which has length 5.

Input: nums = [1, 2, 3, 4, 5], k = 1
Output: 5
Explanation: The longest increasing subsequence with a difference of at most 1 is [1, 2, 3, 4, 5], which has length 5.
'''

# Solution
def longest_increasing_subsequence_with_constraints(nums, k):
    """
    Finds the length of the longest strictly increasing subsequence with a constraint on the difference between consecutive elements.

    Args:
        nums: A list of integers.
        k: The maximum allowed difference between consecutive elements.

    Returns:
        The length of the longest increasing subsequence with the constraint.
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
                # Update dp[i] if a longer subsequence is found
                dp[i] = max(dp[i], dp[j] + 1)

    # The maximum value in the dp table is the length of the longest increasing subsequence
    return max(dp)

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_constraints([3, 10, 2, 1, 20], 7) == 4
    assert longest_increasing_subsequence_with_constraints([4, 2, 1, 4, 3, 4, 5, 8, 15], 3) == 5
    assert longest_increasing_subsequence_with_constraints([1, 2, 3, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_constraints([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_constraints([1, 5, 2, 4, 3], 2) == 3
    assert longest_increasing_subsequence_with_constraints([], 5) == 0
    assert longest_increasing_subsequence_with_constraints([1], 5) == 1
    assert longest_increasing_subsequence_with_constraints([1, 2, 3, 4, 5], 0) == 1
    assert longest_increasing_subsequence_with_constraints([1, 3, 5, 7, 9], 2) == 1
    assert longest_increasing_subsequence_with_constraints([1, 2, 5, 6, 7, 9], 1) == 3

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()