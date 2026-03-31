# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence where the difference between consecutive elements is exactly `k`.

Example:
Input: nums = [3, 10, 3, 4, 5], k = 1
Output: 3
Explanation: The longest increasing subsequence with a difference of 1 is [3, 4, 5], which has length 3.

Input: nums = [1, 5, 7, 8, 5, 3, 4, 2, 1], k = -2
Output: 4
Explanation: The longest increasing subsequence with a difference of -2 is [7, 5, 3, 1], which has length 4.
'''

# Solution
def longest_increasing_subsequence_with_difference(nums, k):
    """
    Finds the length of the longest increasing subsequence where the difference between consecutive elements is exactly k.

    Args:
        nums: A list of integers.
        k: The required difference between consecutive elements in the subsequence.

    Returns:
        The length of the longest increasing subsequence with difference k.
    """

    # dp[num] stores the length of the longest increasing subsequence ending with num.
    dp = {}  # Initialize a dictionary to store the lengths of LIS ending at each number.

    max_length = 0  # Initialize the maximum length found so far.

    for num in nums:
        # If the previous number in the sequence (num - k) exists in the dp table,
        # then the current number can extend that sequence by 1.
        if num - k in dp:
            dp[num] = dp[num - k] + 1  # Extend the sequence.
        else:
            dp[num] = 1  # Start a new sequence of length 1.

        max_length = max(max_length, dp[num])  # Update the maximum length.

    return max_length  # Return the maximum length found.


# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_difference([3, 10, 3, 4, 5], 1) == 3
    assert longest_increasing_subsequence_with_difference([1, 5, 7, 8, 5, 3, 4, 2, 1], -2) == 4
    assert longest_increasing_subsequence_with_difference([1, 2, 3, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_difference([5, 4, 3, 2, 1], -1) == 5
    assert longest_increasing_subsequence_with_difference([1, 1, 1, 1, 1], 0) == 5
    assert longest_increasing_subsequence_with_difference([1, 3, 5, 7, 9], 2) == 5
    assert longest_increasing_subsequence_with_difference([9, 7, 5, 3, 1], -2) == 5
    assert longest_increasing_subsequence_with_difference([1, 2, 3, 5, 6, 7], 1) == 3
    assert longest_increasing_subsequence_with_difference([7, 6, 5, 3, 2, 1], -1) == 3
    assert longest_increasing_subsequence_with_difference([2, 4, 6, 8, 10], 2) == 5
    assert longest_increasing_subsequence_with_difference([10, 8, 6, 4, 2], -2) == 5
    assert longest_increasing_subsequence_with_difference([], 1) == 0
    assert longest_increasing_subsequence_with_difference([5], 2) == 1
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()