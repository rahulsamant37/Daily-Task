# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) such that the difference between any two adjacent elements in the subsequence is at most `k`.

Example:
Input: nums = [3, 10, 2, 1, 20], k = 5
Output: 3
Explanation: The longest increasing subsequence with a difference at most 5 is [3, 10, 20] or [1, 2, 3, 4, 5]. Length is 3.

Input: nums = [1, 5, 3, 8, 9], k = 2
Output: 3
Explanation: The longest increasing subsequence with a difference at most 2 is [1, 3, 5]. Length is 3.
'''

# Solution
def longest_increasing_subsequence_with_k(nums, k):
    """
    Finds the length of the longest increasing subsequence (LIS) such that the
    difference between any two adjacent elements in the subsequence is at most k.

    Args:
        nums: A list of integers.
        k: The maximum allowed difference between adjacent elements.

    Returns:
        The length of the longest increasing subsequence with the given constraint.
    """

    if not nums:
        return 0

    n = len(nums)
    # dp[i] stores the length of the longest increasing subsequence ending at nums[i]
    dp = [1] * n

    # Iterate through each element in the array
    for i in range(1, n):
        # For each element, iterate through all the previous elements
        for j in range(i):
            # If the current element is greater than the previous element and
            # the difference between them is at most k, then we can extend the
            # longest increasing subsequence ending at nums[j] by including nums[i]
            if nums[i] > nums[j] and nums[i] - nums[j] <= k:
                dp[i] = max(dp[i], dp[j] + 1)

    # The maximum value in the dp array is the length of the longest increasing
    # subsequence with the given constraint
    return max(dp)

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_k([3, 10, 2, 1, 20], 5) == 3
    assert longest_increasing_subsequence_with_k([1, 5, 3, 8, 9], 2) == 3
    assert longest_increasing_subsequence_with_k([1, 2, 3, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_k([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_k([1, 2, 3, 4, 5], 0) == 1
    assert longest_increasing_subsequence_with_k([1, 1, 1, 1, 1], 0) == 1
    assert longest_increasing_subsequence_with_k([], 5) == 0
    assert longest_increasing_subsequence_with_k([1], 5) == 1
    assert longest_increasing_subsequence_with_k([1, 6, 2, 7, 3, 8, 4, 9, 5, 10], 1) == 1
    assert longest_increasing_subsequence_with_k([1, 6, 2, 7, 3, 8, 4, 9, 5, 10], 5) == 5

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()