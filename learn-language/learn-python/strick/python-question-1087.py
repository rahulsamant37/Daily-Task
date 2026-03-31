# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) where the difference between any two adjacent elements in the subsequence must be at most `k`.

Example:
Input: nums = [3, 10, 2, 1, 20], k = 5
Output: 4
Explanation: The longest increasing subsequence with the difference at most 5 is [3, 2, 1, 20] which has length 4. Note that [1,2,3,10,20] is not a subsequence, but [3,2,1,20] is.
'''

# Solution
def longest_increasing_subsequence_with_k(nums, k):
    """
    Finds the length of the longest increasing subsequence (LIS) where the difference
    between any two adjacent elements in the subsequence must be at most k.

    Args:
        nums: A list of integers.
        k: An integer representing the maximum allowed difference between adjacent elements.

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
        # Iterate through all previous elements
        for j in range(i):
            # If nums[i] is greater than nums[j] and their difference is at most k
            if nums[i] > nums[j] and nums[i] - nums[j] <= k:
                # Update dp[i] if a longer subsequence can be formed
                dp[i] = max(dp[i], dp[j] + 1)

    # The maximum value in the dp table is the length of the LIS
    return max(dp)

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_k([3, 10, 2, 1, 20], 5) == 4
    assert longest_increasing_subsequence_with_k([1, 2, 3, 4, 5], 1) == 2
    assert longest_increasing_subsequence_with_k([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_k([1, 5, 2, 6, 3, 7], 2) == 3
    assert longest_increasing_subsequence_with_k([10, 22, 9, 33, 21, 50, 41, 60, 80], 10) == 6
    assert longest_increasing_subsequence_with_k([], 5) == 0
    assert longest_increasing_subsequence_with_k([5], 5) == 1
    assert longest_increasing_subsequence_with_k([1, 2, 3, 4, 5], 0) == 1
    assert longest_increasing_subsequence_with_k([1, 3, 2, 4, 5], 1) == 2
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()