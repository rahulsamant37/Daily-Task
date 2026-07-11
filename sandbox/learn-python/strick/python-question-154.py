# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) with the following constraint:

For any two consecutive numbers `nums[i]` and `nums[j]` (where `i < j`) in the subsequence, `nums[j] - nums[i] >= k`.

Example:

Input: nums = [1, 5, 2, 4, 3], k = 2
Output: 3

Explanation:
One possible LIS satisfying the condition is [1, 3, 5].  The length is 3.
Another possible LIS satisfying the condition is [1, 4, 5]. The length is 3.
[1, 2, 3] is an increasing subsequence, but it doesn't satisfy the condition (2-1 < 2).
[1, 5] is an increasing subsequence and satisfies the condition (5-1 >= 2).
[2, 4] is an increasing subsequence and satisfies the condition (4-2 >= 2).
[3,5] is an increasing subsequence and satisfies the condition (5-3 >= 2).
'''

# Solution
def longest_increasing_subsequence_with_k_diff(nums, k):
    """
    Finds the length of the longest increasing subsequence (LIS) with a difference of at least k between consecutive elements.

    Args:
        nums: A list of integers.
        k: The minimum difference between consecutive elements in the LIS.

    Returns:
        The length of the longest increasing subsequence with the given constraint.
    """

    if not nums:
        return 0

    n = len(nums)
    # dp[i] stores the length of the LIS ending at nums[i]
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            # Check if nums[i] can extend the LIS ending at nums[j]
            if nums[i] > nums[j] and nums[i] - nums[j] >= k:
                dp[i] = max(dp[i], dp[j] + 1)

    # The maximum value in dp is the length of the longest increasing subsequence
    return max(dp)

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_k_diff([1, 5, 2, 4, 3], 2) == 3
    assert longest_increasing_subsequence_with_k_diff([1, 2, 3, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_k_diff([1, 2, 3, 4, 5], 2) == 3
    assert longest_increasing_subsequence_with_k_diff([1, 2, 3, 4, 5], 3) == 2
    assert longest_increasing_subsequence_with_k_diff([1, 2, 3, 4, 5], 4) == 2
    assert longest_increasing_subsequence_with_k_diff([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_k_diff([5, 4, 3, 2, 1], 2) == 1
    assert longest_increasing_subsequence_with_k_diff([1, 1, 1, 1, 1], 1) == 1
    assert longest_increasing_subsequence_with_k_diff([1, 1, 1, 1, 1], 0) == 1
    assert longest_increasing_subsequence_with_k_diff([], 1) == 0
    assert longest_increasing_subsequence_with_k_diff([10, 22, 9, 33, 21, 50, 41, 60, 80], 5) == 6
    assert longest_increasing_subsequence_with_k_diff([10, 22, 9, 33, 21, 50, 41, 60, 80], 10) == 4
    assert longest_increasing_subsequence_with_k_diff([1, 3, 6, 10, 15], 2) == 5
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()