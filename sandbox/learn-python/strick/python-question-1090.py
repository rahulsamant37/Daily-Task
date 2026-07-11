# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence where the difference between consecutive elements is at most `k`.

For example:
Input: nums = [3, 10, 2, 1, 20], k = 5
Output: 3
Explanation: The longest increasing subsequence with a difference of at most 5 is [3, 2, 1] or [3, 2, 1] or [10, 20].  The length is 2. The longest increasing subsequence with the at most k is [3, 10, 20].

Input: nums = [1, 5, 2, 4, 3], k = 2
Output: 4
Explanation: The longest increasing subsequence with a difference of at most 2 is [1, 2, 4, 3] or [1, 2, 3]. The length is 4.
'''

# Solution
def longest_increasing_subsequence_with_k_difference(nums, k):
    """
    Finds the length of the longest increasing subsequence with a difference of at most k.

    Args:
        nums: A list of integers.
        k: The maximum difference between consecutive elements in the subsequence.

    Returns:
        The length of the longest increasing subsequence with a difference of at most k.
    """
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n  # Initialize dp array with 1, as each element is a subsequence of length 1

    # Iterate through the array to build the dp array
    for i in range(1, n):
        for j in range(i):
            # Check if nums[i] > nums[j] and the difference is at most k
            if nums[i] > nums[j] and nums[i] - nums[j] <= k:
                dp[i] = max(dp[i], dp[j] + 1)  # Update dp[i] if a longer subsequence is found

    return max(dp)  # Return the maximum value in the dp array, which is the length of the LIS

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_k_difference([3, 10, 2, 1, 20], 5) == 2
    assert longest_increasing_subsequence_with_k_difference([1, 5, 2, 4, 3], 2) == 4
    assert longest_increasing_subsequence_with_k_difference([1, 2, 3, 4, 5], 1) == 2
    assert longest_increasing_subsequence_with_k_difference([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_k_difference([1, 1, 1, 1, 1], 0) == 1
    assert longest_increasing_subsequence_with_k_difference([1, 2, 3, 4, 5], 0) == 1
    assert longest_increasing_subsequence_with_k_difference([], 5) == 0
    assert longest_increasing_subsequence_with_k_difference([1], 5) == 1
    assert longest_increasing_subsequence_with_k_difference([1, 3, 2, 4, 5], 2) == 4
    assert longest_increasing_subsequence_with_k_difference([10, 22, 9, 33, 21, 50, 41, 60, 80], 15) == 6

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()