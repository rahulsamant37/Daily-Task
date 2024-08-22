# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) of `nums` such that the difference between consecutive elements in the subsequence is at most `k`.

Example:
Input: nums = [3, 10, 2, 1, 20], k = 5
Output: 3
Explanation: The longest increasing subsequence with a difference of at most 5 is [3, 2, 1] -> incorrect. The correct LIS is [3, 2, 1] is not increasing. The correct LIS is [1, 2, 3, 10, 20]. The longest increasing subsequence with difference at most 5 is [1,2,3].
Another correct LIS is [3,2] -> incorrect, it's decreasing
Another correct LIS is [2,1] -> incorrect, it's decreasing

Input: nums = [1, 5, 2, 4, 3], k = 2
Output: 4
Explanation: The longest increasing subsequence with a difference of at most 2 is [1, 2, 3, 4].

Input: nums = [1, 2, 3, 4, 5], k = 1
Output: 5
Explanation: The longest increasing subsequence with a difference of at most 1 is [1, 2, 3, 4, 5].

Input: nums = [5, 4, 3, 2, 1], k = 1
Output: 1
Explanation: The longest increasing subsequence with a difference of at most 1 is [5] or [4] or [3] or [2] or [1].
'''

# Solution
def longest_increasing_subsequence_with_k_difference(nums, k):
    """
    Finds the length of the longest increasing subsequence of nums such that the
    difference between consecutive elements in the subsequence is at most k.

    Args:
        nums: A list of integers.
        k: An integer representing the maximum allowed difference.

    Returns:
        The length of the longest increasing subsequence with a difference of at most k.
    """

    n = len(nums)
    if n == 0:
        return 0

    # dp[i] stores the length of the longest increasing subsequence ending at nums[i]
    dp = [1] * n

    # Iterate through the array to build the dp table
    for i in range(1, n):
        for j in range(i):
            # If nums[i] is greater than nums[j] and the difference is at most k,
            # then update dp[i] if a longer subsequence is found
            if nums[i] > nums[j] and nums[i] - nums[j] <= k:
                dp[i] = max(dp[i], dp[j] + 1)

    # The maximum value in the dp table is the length of the LIS
    return max(dp)

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_k_difference([3, 10, 2, 1, 20], 5) == 3
    assert longest_increasing_subsequence_with_k_difference([1, 5, 2, 4, 3], 2) == 4
    assert longest_increasing_subsequence_with_k_difference([1, 2, 3, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_k_difference([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_k_difference([1, 2, 3, 4, 5], 0) == 1
    assert longest_increasing_subsequence_with_k_difference([5, 4, 3, 2, 1], 0) == 1
    assert longest_increasing_subsequence_with_k_difference([1, 2, 1, 3, 2, 4, 3], 1) == 4
    assert longest_increasing_subsequence_with_k_difference([1], 5) == 1
    assert longest_increasing_subsequence_with_k_difference([], 5) == 0
    assert longest_increasing_subsequence_with_k_difference([1, 3, 2, 4, 5], 1) == 3
    assert longest_increasing_subsequence_with_k_difference([1, 3, 2, 4, 5], 2) == 5

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()