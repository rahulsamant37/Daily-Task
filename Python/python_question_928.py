# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) where the difference between adjacent elements in the subsequence is at most `k`.

Example:
Input: nums = [3, 10, 2, 1, 20], k = 5
Output: 3
Explanation: The longest increasing subsequence with a maximum difference of 5 is [3, 2, 1] or [1, 2, 3]. Specifically, [1,2,3] has length 3 and 2-1 <=5 and 3-2 <= 5.  [3,2] is also a valid increasing subsequence with length 2, but is not the longest. Other valid sequences are [3,10,20] but 10-3>5 and 20-10>5, so this is not valid.  Another valid sequence is [1,2] since 2-1<=5.

Input: nums = [1, 5, 2, 4, 3], k = 1
Output: 3
Explanation: One possible LIS is [1, 2, 3]
'''

# Solution
def longest_increasing_subsequence_with_k_difference(nums, k):
    """
    Finds the length of the longest increasing subsequence where the difference between adjacent elements is at most k.

    Args:
      nums: A list of integers.
      k: An integer representing the maximum difference allowed between adjacent elements in the subsequence.

    Returns:
      The length of the longest increasing subsequence with a maximum difference of k.
    """
    n = len(nums)
    if n == 0:
        return 0

    # dp[i] stores the length of the longest increasing subsequence ending at nums[i]
    dp = [1] * n

    # Iterate through the array to build the dp array
    for i in range(1, n):
        for j in range(i):
            # If nums[i] > nums[j] and the difference is at most k, we can extend the subsequence ending at nums[j]
            if nums[i] > nums[j] and nums[i] - nums[j] <= k:
                dp[i] = max(dp[i], dp[j] + 1)

    # The maximum value in the dp array is the length of the longest increasing subsequence
    return max(dp)

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_k_difference([3, 10, 2, 1, 20], 5) == 3
    assert longest_increasing_subsequence_with_k_difference([1, 5, 2, 4, 3], 1) == 3
    assert longest_increasing_subsequence_with_k_difference([1, 2, 3, 4, 5], 1) == 2
    assert longest_increasing_subsequence_with_k_difference([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_k_difference([1, 2, 3, 4, 5], 10) == 5
    assert longest_increasing_subsequence_with_k_difference([], 5) == 0
    assert longest_increasing_subsequence_with_k_difference([1], 5) == 1
    assert longest_increasing_subsequence_with_k_difference([1, 3, 2, 5, 4], 2) == 3
    assert longest_increasing_subsequence_with_k_difference([1, 3, 2, 5, 4], 0) == 1
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()