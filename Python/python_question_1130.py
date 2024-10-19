# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) with the following condition:

For any two consecutive elements `nums[i]` and `nums[j]` in the subsequence (where i < j), `nums[j] - nums[i] >= k`.

Example:
Input: nums = [1, 3, 2, 4, 5], k = 2
Output: 3
Explanation: The longest increasing subsequence satisfying the condition is [1, 3, 5] or [1, 4, 5].

Input: nums = [1, 2, 3, 4, 5], k = 1
Output: 5
Explanation: The longest increasing subsequence is [1, 2, 3, 4, 5].

Input: nums = [5, 4, 3, 2, 1], k = 1
Output: 1
Explanation: The longest increasing subsequence is [5], [4], [3], [2], or [1].

Input: nums = [10, 22, 9, 33, 21, 50, 41, 60, 80], k = 5
Output: 5
Explanation: One possible LIS is [10, 22, 33, 41, 50, 60, 80], and with k = 5, we can have [10, 22, 33, 50, 60, 80] which is of length 6. One possible LIS is [10, 22, 33, 50, 60, 80].
Another possible LIS is [10, 33, 50, 60, 80] which is of length 5.
'''

# Solution
def longest_increasing_subsequence_with_k(nums, k):
    """
    Finds the length of the longest increasing subsequence (LIS) with the condition that
    for any two consecutive elements nums[i] and nums[j] in the subsequence (where i < j),
    nums[j] - nums[i] >= k.

    Args:
        nums: A list of integers.
        k: An integer representing the minimum difference between consecutive elements in the subsequence.

    Returns:
        The length of the longest increasing subsequence satisfying the condition.
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
            # If nums[i] can extend the subsequence ending at nums[j]
            if nums[i] > nums[j] and nums[i] - nums[j] >= k:
                # Update dp[i] if extending the subsequence results in a longer subsequence
                dp[i] = max(dp[i], dp[j] + 1)

    # Return the maximum value in the dp array, which represents the length of the LIS
    return max(dp)

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_k([1, 3, 2, 4, 5], 2) == 3
    assert longest_increasing_subsequence_with_k([1, 2, 3, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_k([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_k([10, 22, 9, 33, 21, 50, 41, 60, 80], 5) == 5
    assert longest_increasing_subsequence_with_k([], 5) == 0
    assert longest_increasing_subsequence_with_k([1], 5) == 1
    assert longest_increasing_subsequence_with_k([1, 2], 2) == 1
    assert longest_increasing_subsequence_with_k([1, 3], 2) == 2
    assert longest_increasing_subsequence_with_k([1, 5, 2, 6, 3, 7, 4, 8], 3) == 4
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()