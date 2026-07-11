# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) where the difference between consecutive elements in the subsequence must be less than or equal to `k`.

Example:
Input: nums = [3, 10, 2, 1, 20], k = 5
Output: 3
Explanation: One possible LIS is [3, 2, 1] (or [10, 2, 1] or [3, 2, 1] or [2, 1]). Another one is [3, 10, 20] which is an increasing subsequence satisfying the condition |10-3| <= 5 and |20-10| <= 5 and |20-3| > 5. So, only consecutive elements difference must be <= k. Therefore, the longest possible length is 3. Note that the subsequence must be increasing.

Input: nums = [4, 2, 1, 4, 3, 1, 5, 6], k = 1
Output: 4
Explanation: One possible LIS is [1, 1, 5, 6]. Another one is [2, 3, 5, 6].
'''

# Solution
def longest_increasing_subsequence_with_k_difference(nums, k):
    """
    Finds the length of the longest increasing subsequence with a maximum difference of k between consecutive elements.

    Args:
        nums: A list of integers.
        k: The maximum difference allowed between consecutive elements in the subsequence.

    Returns:
        The length of the longest increasing subsequence.
    """

    n = len(nums)
    if n == 0:
        return 0

    # dp[i] stores the length of the longest increasing subsequence ending at nums[i].
    dp = [1] * n

    # Iterate through the array to build the dp table.
    for i in range(1, n):
        for j in range(i):
            # If nums[i] is greater than nums[j] and the difference between them is less than or equal to k,
            # then we can extend the subsequence ending at nums[j] by including nums[i].
            if nums[i] > nums[j] and abs(nums[i] - nums[j]) <= k:
                dp[i] = max(dp[i], dp[j] + 1)

    # The maximum value in the dp table is the length of the longest increasing subsequence.
    return max(dp)

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_k_difference([3, 10, 2, 1, 20], 5) == 3
    assert longest_increasing_subsequence_with_k_difference([4, 2, 1, 4, 3, 1, 5, 6], 1) == 4
    assert longest_increasing_subsequence_with_k_difference([1, 2, 3, 4, 5], 1) == 2
    assert longest_increasing_subsequence_with_k_difference([1, 2, 3, 4, 5], 0) == 1
    assert longest_increasing_subsequence_with_k_difference([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_k_difference([1, 5, 2, 4, 3], 2) == 3
    assert longest_increasing_subsequence_with_k_difference([], 5) == 0
    assert longest_increasing_subsequence_with_k_difference([1], 5) == 1
    assert longest_increasing_subsequence_with_k_difference([1, 2], 1) == 2
    assert longest_increasing_subsequence_with_k_difference([1, 3, 5, 2, 4], 2) == 3
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()