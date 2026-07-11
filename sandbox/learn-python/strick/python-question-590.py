# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) where the difference between consecutive elements in the subsequence must be less than or equal to `k`.

Example:
Input: nums = [3, 10, 2, 1, 20], k = 5
Output: 3
Explanation: The longest increasing subsequence with a difference <= 5 is [3, 10, 20] which has length 3 or [1, 2, 3, 10]. The correct sequence should be [1,2,3,8,10] since there is a subsequence of length 3.

Input: nums = [4, 6, 5, 7, 8], k = 1
Output: 3
Explanation: The longest increasing subsequence with a difference <= 1 is [4, 5, 6, 7, 8]. The length is 5. Note that consecutive elements must be increasing and the difference between them must be <= k. However, [4,5,7,8] is not a valid sequence because 5 and 7 are not consecutive in the original array.
'''

# Solution
def longest_increasing_subsequence_with_k_difference(nums, k):
    """
    Finds the length of the longest increasing subsequence in `nums` where the difference
    between consecutive elements in the subsequence is less than or equal to `k`.

    Args:
        nums: A list of integers.
        k: An integer representing the maximum allowed difference.

    Returns:
        The length of the longest increasing subsequence.
    """
    n = len(nums)
    if n == 0:
        return 0

    # dp[i] stores the length of the longest increasing subsequence ending at nums[i].
    dp = [1] * n

    # Iterate through the array to build the dp array.
    for i in range(1, n):
        for j in range(i):
            # Check if nums[i] can extend the subsequence ending at nums[j].
            if nums[i] > nums[j] and nums[i] - nums[j] <= k:
                dp[i] = max(dp[i], dp[j] + 1)

    # The maximum value in the dp array is the length of the LIS.
    return max(dp)

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_k_difference([3, 10, 2, 1, 20], 5) == 3
    assert longest_increasing_subsequence_with_k_difference([4, 6, 5, 7, 8], 1) == 3 # Corrected test case
    assert longest_increasing_subsequence_with_k_difference([1, 2, 3, 4, 5], 1) == 2
    assert longest_increasing_subsequence_with_k_difference([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_k_difference([1, 5, 2, 6, 3, 7, 4, 8], 2) == 4
    assert longest_increasing_subsequence_with_k_difference([1, 2, 3, 8, 9, 10], 1) == 2
    assert longest_increasing_subsequence_with_k_difference([1, 2, 3, 8, 10], 5) == 3
    assert longest_increasing_subsequence_with_k_difference([10, 22, 9, 33, 21, 50, 41, 60, 80], 10) == 6
    assert longest_increasing_subsequence_with_k_difference([], 5) == 0
    assert longest_increasing_subsequence_with_k_difference([1], 5) == 1
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()