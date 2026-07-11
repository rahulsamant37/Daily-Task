# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) with the following constraint:

For any two consecutive elements `nums[i]` and `nums[j]` in the subsequence, where `i < j`,  `nums[j] - nums[i] <= k`.

Example:
Input: nums = [3, 10, 2, 1, 20], k = 5
Output: 3
Explanation: The longest increasing subsequence that satisfies the constraint is [3, 2, 1]. The subsequence is [1, 2, 3] after sorting them based on index.
Another solution is [1,2,3]
Input: nums = [1, 5, 2, 4, 3], k = 2
Output: 4
Explanation: The longest increasing subsequence that satisfies the constraint is [1, 2, 3, 4].
'''

# Solution
def longest_increasing_subsequence_with_k(nums, k):
    """
    Finds the length of the longest increasing subsequence with the given constraint.

    Args:
        nums: A list of integers.
        k: An integer representing the maximum difference between consecutive elements in the subsequence.

    Returns:
        The length of the longest increasing subsequence.
    """

    n = len(nums)
    if n == 0:
        return 0

    # dp[i] stores the length of the longest increasing subsequence ending at nums[i]
    dp = [1] * n

    # Iterate through the array to build the dp array
    for i in range(1, n):
        for j in range(i):
            # Check if nums[i] can be added to the subsequence ending at nums[j]
            if nums[i] > nums[j] and nums[i] - nums[j] <= k:
                dp[i] = max(dp[i], dp[j] + 1)

    # The maximum value in the dp array is the length of the LIS
    return max(dp)


# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_k([3, 10, 2, 1, 20], 5) == 3
    assert longest_increasing_subsequence_with_k([1, 5, 2, 4, 3], 2) == 4
    assert longest_increasing_subsequence_with_k([1, 2, 3, 4, 5], 1) == 2
    assert longest_increasing_subsequence_with_k([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_k([1, 2, 3, 4, 5], 0) == 1
    assert longest_increasing_subsequence_with_k([1, 1, 1, 1, 1], 0) == 1
    assert longest_increasing_subsequence_with_k([], 5) == 0
    assert longest_increasing_subsequence_with_k([1], 5) == 1
    assert longest_increasing_subsequence_with_k([1, 6, 2, 7, 3, 8, 4, 9, 5, 10], 2) == 6
    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()