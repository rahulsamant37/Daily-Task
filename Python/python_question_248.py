# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence (LIS) where the difference between consecutive elements in the subsequence is exactly `diff`.

Example:
Input: nums = [3, 0, 3, 4, 5, 6], diff = 3
Output: 4
Explanation: The longest increasing subsequence with a difference of 3 is [0, 3, 6], or [3, 6]. The length is 3. But also we have [3,0,3,4,5,6] -> [3,6]
Another example:
Input: nums = [1, 5, 7, 8, 5, 3, 4, 2, 1], diff = -2
Output: 3
Explanation: The longest increasing subsequence with a difference of -2 is [7, 5, 3]. The length is 3.

Input: nums = [4, 12, 10, 0, -2, 10, -7, 7, -9, 2, -5, 11, 12, -5, 6, 11, 4, -10, 4, 5], diff = 3
Output: 2
'''

# Solution
def longest_arithmetic_subsequence(nums, diff):
    """
    Finds the length of the longest arithmetic subsequence with a given difference.

    Args:
        nums: A list of integers.
        diff: The difference between consecutive elements in the subsequence.

    Returns:
        The length of the longest arithmetic subsequence.
    """

    # Create a dictionary to store the length of the longest arithmetic subsequence
    # ending at each number. The key is the number, and the value is the length.
    dp = {}

    # Iterate over the numbers in the input list.
    for num in nums:
        # If the number minus the difference is in the dictionary, then the length of
        # the longest arithmetic subsequence ending at the current number is one more
        # than the length of the longest arithmetic subsequence ending at the number
        # minus the difference. Otherwise, the length is 1.
        if num - diff in dp:
            dp[num] = dp[num - diff] + 1
        else:
            dp[num] = 1

    # Return the maximum value in the dictionary.
    return max(dp.values()) if dp else 0

# Test cases
def test_solution():
    assert longest_arithmetic_subsequence([3, 0, 3, 4, 5, 6], 3) == 4
    assert longest_arithmetic_subsequence([1, 5, 7, 8, 5, 3, 4, 2, 1], -2) == 3
    assert longest_arithmetic_subsequence([4, 12, 10, 0, -2, 10, -7, 7, -9, 2, -5, 11, 12, -5, 6, 11, 4, -10, 4, 5], 3) == 2
    assert longest_arithmetic_subsequence([1,2,3,4],1) == 4
    assert longest_arithmetic_subsequence([1,3,5,7],2) == 4
    assert longest_arithmetic_subsequence([1,5],4) == 2
    assert longest_arithmetic_subsequence([1,2,3,4,5],1) == 5
    assert longest_arithmetic_subsequence([1,2,3,4,5],0) == 1
    assert longest_arithmetic_subsequence([], 0) == 0
    assert longest_arithmetic_subsequence([5], 0) == 1

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()