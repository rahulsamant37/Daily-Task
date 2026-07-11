# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) of `nums` such that the difference between any two consecutive elements in the subsequence is at most `k`.

Example:
Input: nums = [3, 10, 2, 1, 20], k = 5
Output: 3
Explanation: The longest increasing subsequence with a maximum difference of 5 is [3, 2, 1] (or [3, 2, 1], [1, 2, 3] but with reordering). Another possible sequence is [1, 2, 3]. The length is 3. Note that [1, 10, 20] is an increasing subsequence, but the difference between 1 and 10 (9) is greater than k (5). Also, the subsequence needs to be in the same order as the original array. In this case, [1, 2, 3] is invalid because it would need to reorder the array.

Input: nums = [1, 5, 3, 8, 9], k = 2
Output: 3
Explanation: The longest increasing subsequence with a maximum difference of 2 is [8,9] or [1,3]. [5,3] is not increasing. [3,8,9] is not allowed because 8-3 > 2. [1,3] has length 2. [8,9] also has length 2.

Input: nums = [1, 2, 3, 4, 5], k = 1
Output: 5
'''

# Solution
def longest_increasing_subsequence_with_k(nums, k):
    """
    Finds the length of the longest increasing subsequence of nums such that
    the difference between any two consecutive elements in the subsequence is at most k.

    Args:
        nums: A list of integers.
        k: An integer representing the maximum allowed difference.

    Returns:
        An integer representing the length of the longest increasing subsequence.
    """
    n = len(nums)
    if n == 0:
        return 0

    # dp[i] stores the length of the longest increasing subsequence ending at index i
    dp = [1] * n

    # Iterate through the array
    for i in range(1, n):
        # Iterate through all previous elements
        for j in range(i):
            # If nums[i] is greater than nums[j] and the difference is at most k,
            # then we can extend the subsequence ending at j to include nums[i]
            if nums[i] > nums[j] and nums[i] - nums[j] <= k:
                dp[i] = max(dp[i], dp[j] + 1)

    # Return the maximum value in the dp array
    return max(dp)

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_k([3, 10, 2, 1, 20], 5) == 3
    assert longest_increasing_subsequence_with_k([1, 5, 3, 8, 9], 2) == 2
    assert longest_increasing_subsequence_with_k([1, 2, 3, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_k([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_k([1, 2, 3, 4, 5], 0) == 1
    assert longest_increasing_subsequence_with_k([1, 1, 1, 1, 1], 0) == 1
    assert longest_increasing_subsequence_with_k([1, 3, 2, 4, 5], 2) == 4
    assert longest_increasing_subsequence_with_k([10, 22, 9, 33, 21, 50, 41, 60, 80], 10) == 6
    assert longest_increasing_subsequence_with_k([], 5) == 0
    assert longest_increasing_subsequence_with_k([7], 3) == 1
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()