# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums`, find the length of the longest increasing subsequence such that the difference between any two adjacent elements in the subsequence is at most `k`.

Example:
Input: nums = [1, 3, 2, 4, 5], k = 1
Output: 4
Explanation: The longest increasing subsequence is [1, 2, 3, 4] or [2, 3, 4, 5], and the difference between adjacent elements is at most 1.
'''

# Solution
def longest_increasing_subsequence_with_difference(nums, k):
    """
    Finds the length of the longest increasing subsequence with a maximum difference of k between adjacent elements.

    Args:
        nums: A list of integers.
        k: The maximum allowed difference between adjacent elements.

    Returns:
        The length of the longest increasing subsequence satisfying the condition.
    """
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n  # dp[i] stores the length of the longest increasing subsequence ending at nums[i]

    # Iterate through the array
    for i in range(1, n):
        # For each element, check all previous elements
        for j in range(i):
            # If the current element is greater than the previous element and the difference is at most k
            if nums[i] > nums[j] and nums[i] - nums[j] <= k:
                # Update the length of the longest increasing subsequence ending at nums[i]
                dp[i] = max(dp[i], dp[j] + 1)

    # Return the maximum length found
    return max(dp)

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_difference([1, 3, 2, 4, 5], 1) == 4
    assert longest_increasing_subsequence_with_difference([1, 3, 2, 4, 5], 2) == 5
    assert longest_increasing_subsequence_with_difference([1, 2, 3, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_difference([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_difference([1, 5, 2, 6, 3, 7, 4, 8], 2) == 4
    assert longest_increasing_subsequence_with_difference([1, 5, 2, 6, 3, 7, 4, 8], 1) == 1
    assert longest_increasing_subsequence_with_difference([1], 1) == 1
    assert longest_increasing_subsequence_with_difference([], 1) == 0
    assert longest_increasing_subsequence_with_difference([1, 1, 1, 1], 0) == 1
    assert longest_increasing_subsequence_with_difference([1, 2, 3, 5, 7, 9, 11, 13], 2) == 8
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()