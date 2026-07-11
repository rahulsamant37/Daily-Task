# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums`, find the length of the longest increasing subsequence such that the absolute difference between consecutive elements in the subsequence is less than or equal to a given integer `k`.

Example:
Input: nums = [3, 10, 2, 1, 20], k = 3
Output: 4
Explanation: The longest increasing subsequence is [3, 2, 1, 20] with length 4, where the absolute difference between consecutive elements is <= 3.  Another possible subsequence is [3, 2, 20]

Input: nums = [1, 3, 2, 4, 5], k = 2
Output: 4
Explanation: The longest increasing subsequence is [1, 3, 4, 5] with length 4.
'''

# Solution
def longest_increasing_subsequence_with_k_difference(nums, k):
    """
    Finds the length of the longest increasing subsequence in `nums` such that the absolute difference
    between consecutive elements in the subsequence is less than or equal to `k`.

    Args:
        nums: A list of integers.
        k: An integer representing the maximum allowed absolute difference between consecutive elements.

    Returns:
        The length of the longest increasing subsequence.
    """

    if not nums:
        return 0

    n = len(nums)
    # dp[i] stores the length of the longest increasing subsequence ending at nums[i].
    dp = [1] * n

    # Iterate through the array to build the dp table.
    for i in range(1, n):
        # For each element nums[i], iterate through the elements before it.
        for j in range(i):
            # If nums[i] is greater than nums[j] and the absolute difference between them is less than or equal to k,
            # then we can extend the subsequence ending at nums[j] by adding nums[i] to it.
            if nums[i] > nums[j] and abs(nums[i] - nums[j]) <= k:
                dp[i] = max(dp[i], dp[j] + 1)

    # The maximum value in the dp table is the length of the longest increasing subsequence.
    return max(dp)

# Test cases
def test_longest_increasing_subsequence_with_k_difference():
    assert longest_increasing_subsequence_with_k_difference([3, 10, 2, 1, 20], 3) == 4
    assert longest_increasing_subsequence_with_k_difference([1, 3, 2, 4, 5], 2) == 4
    assert longest_increasing_subsequence_with_k_difference([1, 2, 3, 4, 5], 1) == 2
    assert longest_increasing_subsequence_with_k_difference([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_k_difference([1, 5, 2, 4, 3], 2) == 3
    assert longest_increasing_subsequence_with_k_difference([], 5) == 0
    assert longest_increasing_subsequence_with_k_difference([1], 5) == 1
    assert longest_increasing_subsequence_with_k_difference([1, 1, 1, 1, 1], 0) == 1
    assert longest_increasing_subsequence_with_k_difference([1, 4, 2, 5, 3], 2) == 3
    assert longest_increasing_subsequence_with_k_difference([10, 22, 9, 33, 21, 50, 41, 60, 80], 10) == 6
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_increasing_subsequence_with_k_difference()