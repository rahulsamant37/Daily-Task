# Python Question: Longest Increasing Subsequence with Constraints
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) of `nums` such that the difference between any two consecutive elements in the subsequence is at most `k`.

Example:
Input: nums = [3, 10, 2, 1, 20], k = 5
Output: 3
Explanation: The longest increasing subsequence with the given constraint is [3, 2, 1] or [1,2,3] which are not valid since they are not subsequences of the original array. Valid subsequences are [3,10,20], [3,10], [3,20], etc. The longest increasing subsequence where the difference between any two consecutive elements is at most 5 is [3, 2, 1]. The length of this subsequence is 3. Note that the order of elements in the subsequence must be the same as in the original array.

Input: nums = [4, 2, 1, 4, 3, 5], k = 2
Output: 4
Explanation: The longest increasing subsequence with the given constraint is [2, 1, 3, 5]. The length of this subsequence is 4.
'''

# Solution
def longest_increasing_subsequence_with_constraints(nums, k):
    """
    Finds the length of the longest increasing subsequence of nums such that the
    difference between any two consecutive elements in the subsequence is at most k.

    Args:
        nums: A list of integers.
        k: An integer representing the maximum difference between consecutive elements.

    Returns:
        The length of the longest increasing subsequence satisfying the constraints.
    """
    n = len(nums)
    if n == 0:
        return 0

    # dp[i] stores the length of the longest increasing subsequence ending at nums[i]
    dp = [1] * n

    # Iterate through the array
    for i in range(1, n):
        # For each element nums[i], iterate through the previous elements
        for j in range(i):
            # Check if nums[i] can extend the subsequence ending at nums[j]
            if nums[i] > nums[j] and nums[i] - nums[j] <= k:
                # If it can, update dp[i]
                dp[i] = max(dp[i], dp[j] + 1)

    # The result is the maximum value in the dp array
    return max(dp)

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_constraints([3, 10, 2, 1, 20], 5) == 3
    assert longest_increasing_subsequence_with_constraints([4, 2, 1, 4, 3, 5], 2) == 4
    assert longest_increasing_subsequence_with_constraints([1, 2, 3, 4, 5], 1) == 2
    assert longest_increasing_subsequence_with_constraints([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_constraints([1, 5, 2, 6, 3, 7, 4, 8], 2) == 4
    assert longest_increasing_subsequence_with_constraints([1], 5) == 1
    assert longest_increasing_subsequence_with_constraints([], 5) == 0
    assert longest_increasing_subsequence_with_constraints([1,1,1,1,1],0) == 1
    assert longest_increasing_subsequence_with_constraints([1,2,3,4,5], 0) == 1
    assert longest_increasing_subsequence_with_constraints([5, 3, 4, 1, 2], 1) == 2

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()