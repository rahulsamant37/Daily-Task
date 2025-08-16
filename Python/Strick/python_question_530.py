# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence such that the difference between consecutive elements in the subsequence is exactly `diff`.

Example:
Input: nums = [3, 0, 3, 4, 5, 6], diff = 3
Output: 4
Explanation: The longest increasing subsequence with difference 3 is [0, 3, 6], and its length is 3. Another one is [3, 6], and its length is 2. [3, 4, 5, 6] is not a valid subsequence. [3, 6] and [0, 3, 6] are valid and the longest is [0, 3, 6]. The longest increasing subsequence with difference 3 is [3, 6]. If we start from 0, then [0, 3, 6]. If we start from 3, then [3, 6]. If we start from 4, then there is nothing. If we start from 5, then there is nothing. If we start from 6, then there is nothing.

Input: nums = [1,5,7,8,5,3,4,2,1], diff = -2
Output: 4
Explanation: The longest increasing subsequence with difference -2 is [7, 5, 3, 1], and its length is 4.

Input: nums = [1, 2, 3, 4, 5, 6], diff = 1
Output: 6
Explanation: The longest increasing subsequence with difference 1 is [1, 2, 3, 4, 5, 6], and its length is 6.

Input: nums = [1, 3, 5, 7, 9], diff = 2
Output: 5
Explanation: The longest increasing subsequence with difference 2 is [1, 3, 5, 7, 9], and its length is 5.
'''

# Solution
def longest_increasing_subsequence_with_difference(nums, diff):
    """
    Finds the length of the longest increasing subsequence with a specific difference.

    Args:
        nums: A list of integers.
        diff: The required difference between consecutive elements in the subsequence.

    Returns:
        The length of the longest increasing subsequence with the given difference.
    """

    # Create a dictionary to store the length of the longest increasing subsequence
    # ending at each number.
    dp = {}

    # Iterate through the numbers in the input array.
    for num in nums:
        # If the number minus the difference is already in the dictionary,
        # then the length of the longest increasing subsequence ending at the current number
        # is one more than the length of the longest increasing subsequence ending at
        # the number minus the difference.
        if num - diff in dp:
            dp[num] = dp[num - diff] + 1
        # Otherwise, the length of the longest increasing subsequence ending at the current number
        # is 1.
        else:
            dp[num] = 1

    # Return the maximum value in the dictionary.
    return max(dp.values()) if dp else 0

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_difference([3, 0, 3, 4, 5, 6], 3) == 4
    assert longest_increasing_subsequence_with_difference([1,5,7,8,5,3,4,2,1], -2) == 4
    assert longest_increasing_subsequence_with_difference([1, 2, 3, 4, 5, 6], 1) == 6
    assert longest_increasing_subsequence_with_difference([1, 3, 5, 7, 9], 2) == 5
    assert longest_increasing_subsequence_with_difference([1, 3, 5, 7, 9], 4) == 1
    assert longest_increasing_subsequence_with_difference([1, 3, 5, 7, 9], 0) == 1
    assert longest_increasing_subsequence_with_difference([1], 0) == 1
    assert longest_increasing_subsequence_with_difference([], 0) == 0
    assert longest_increasing_subsequence_with_difference([7,7,7,7,7,7,7], 0) == 7
    assert longest_increasing_subsequence_with_difference([7,7,7,7,7,7,7], 1) == 1
    assert longest_increasing_subsequence_with_difference([1, 2, 3, 1, 2, 3], 1) == 3
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()