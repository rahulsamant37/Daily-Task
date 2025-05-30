# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) such that the difference between consecutive elements in the subsequence is at most `k`.

Example:
Input: nums = [3, 10, 2, 1, 20], k = 5
Output: 3
Explanation: One possible LIS is [3, 2, 1], but it is not increasing. A valid LIS is [3, 2, 1] with difference constraint.
Another possible LIS is [1, 2, 3], but the numbers are not from the input array.

Another possible LIS is [3, 2, 1], but it is not strictly increasing.
A valid LIS is [3, 10, 20] with length 3 and difference between consecutive elements is at most 5.
[2, 3, 10, 20] is also a valid LIS with length 4.

Input: nums = [4,2,4,5,3,7], k = 1
Output: 3
Explanation: One of the longest increasing subsequences is [2, 3, 4] of length 3. The differences between the elements are 1 and 1, both are <= 1.

Input: nums = [1, 5, 2, 6, 3, 7, 4], k = 2
Output: 4
Explanation: One of the longest increasing subsequences is [1, 2, 3, 4] of length 4.
'''

# Solution
def longest_increasing_subsequence_with_k_difference(nums, k):
    """
    Finds the length of the longest increasing subsequence with a difference constraint.

    Args:
        nums: A list of integers.
        k: The maximum difference allowed between consecutive elements.

    Returns:
        The length of the longest increasing subsequence.
    """

    n = len(nums)
    if n == 0:
        return 0

    # dp[i] stores the length of the longest increasing subsequence ending at nums[i]
    dp = [1] * n

    # Iterate through the array to build the dp table
    for i in range(1, n):
        for j in range(i):
            # Check if nums[i] can be added to the subsequence ending at nums[j]
            if nums[i] > nums[j] and abs(nums[i] - nums[j]) <= k:
                dp[i] = max(dp[i], dp[j] + 1)

    # The maximum value in the dp table is the length of the LIS
    return max(dp)

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_k_difference([3, 10, 2, 1, 20], 5) == 3
    assert longest_increasing_subsequence_with_k_difference([4,2,4,5,3,7], 1) == 3
    assert longest_increasing_subsequence_with_k_difference([1, 5, 2, 6, 3, 7, 4], 2) == 4
    assert longest_increasing_subsequence_with_k_difference([1, 2, 3, 4, 5], 0) == 1
    assert longest_increasing_subsequence_with_k_difference([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_k_difference([1, 2, 3, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_k_difference([], 5) == 0
    assert longest_increasing_subsequence_with_k_difference([1], 5) == 1
    assert longest_increasing_subsequence_with_k_difference([1, 3, 2, 4, 5], 1) == 3 # e.g., [1,2,3]
    assert longest_increasing_subsequence_with_k_difference([1, 3, 2, 4, 5], 2) == 5

if __name__ == "__main__":
    test_solution()