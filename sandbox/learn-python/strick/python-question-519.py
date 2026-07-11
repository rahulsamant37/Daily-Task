# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence (LIS) such that the difference between consecutive elements in the subsequence is exactly `diff`.

Example:
Input: nums = [3, 0, 3, 4, 5, 6], diff = 3
Output: 4
Explanation: The longest increasing subsequence with a difference of 3 is [0, 3, 6], which has a length of 3. Another one is [3,6]. But [3,4,5,6] is not valid because the difference between consecutive elements are not the same.

Input: nums = [1, 5, 7, 8, 5, 3, 4, 2, 1], diff = -2
Output: 4
Explanation: The longest increasing subsequence with a difference of -2 is [7, 5, 3, 1], which has a length of 4.
'''

# Solution
def longest_arithmetic_subsequence(nums, diff):
    """
    Finds the length of the longest arithmetic subsequence with the given difference.

    Args:
        nums: A list of integers.
        diff: The difference between consecutive elements in the subsequence.

    Returns:
        The length of the longest arithmetic subsequence.
    """
    # Create a dictionary to store the length of the longest arithmetic subsequence ending at each number.
    dp = {}

    # Iterate over the numbers in the array.
    for num in nums:
        # If the number minus the difference is in the dictionary, then the length of the longest arithmetic subsequence ending at the current number is one more than the length of the longest arithmetic subsequence ending at the number minus the difference.
        if num - diff in dp:
            dp[num] = dp[num - diff] + 1
        # Otherwise, the length of the longest arithmetic subsequence ending at the current number is 1.
        else:
            dp[num] = 1

    # Return the maximum length of the longest arithmetic subsequence.
    return max(dp.values()) if dp else 0

# Test cases
def test_solution():
    assert longest_arithmetic_subsequence([3, 0, 3, 4, 5, 6], 3) == 4
    assert longest_arithmetic_subsequence([1, 5, 7, 8, 5, 3, 4, 2, 1], -2) == 4
    assert longest_arithmetic_subsequence([1, 2, 3, 4], 1) == 4
    assert longest_arithmetic_subsequence([1, 3, 5, 7], 2) == 4
    assert longest_arithmetic_subsequence([1, 5, 7, 8, 5, 3, 4, 2, 1], 0) == 1
    assert longest_arithmetic_subsequence([1, 2, 3, 4, 5], 0) == 1
    assert longest_arithmetic_subsequence([1, 2, 3, 4, 5], 1) == 5
    assert longest_arithmetic_subsequence([1, 3, 5, 7, 9], 2) == 5
    assert longest_arithmetic_subsequence([1, 3, 5, 7, 9], 0) == 1
    assert longest_arithmetic_subsequence([], 2) == 0
    assert longest_arithmetic_subsequence([1], 2) == 1
    assert longest_arithmetic_subsequence([1, 1, 1, 1, 1], 0) == 5
    assert longest_arithmetic_subsequence([1, 1, 1, 1, 1], 1) == 1
    assert longest_arithmetic_subsequence([7,7,7,7,7,7,7,7,7,7,7,7,7],0) == 13
    assert longest_arithmetic_subsequence([1, 3, 5, 2, 4, 6], 2) == 3
    assert longest_arithmetic_subsequence([1, 2, 3, 1, 2, 3], 1) == 3
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()