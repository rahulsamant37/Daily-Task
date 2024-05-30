# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence (LIS) where the difference between consecutive elements in the subsequence is exactly `diff`.

Example:
Input: nums = [3, 0, 3, 4, 5, 6], diff = 3
Output: 4
Explanation: The longest increasing subsequence with a difference of 3 is [0, 3, 6], which has length 3. Another one is [3, 6] which has length 2.  [3, 4, 5, 6] has length 4 and difference 1, but we want difference 3. Thus the subsequence [3, 6] is not a valid answer. Another valid subsequence is [3].

Input: nums = [1, 5, 7, 8, 5, 3, 4, 2, 1], diff = -2
Output: 3
Explanation: The longest increasing subsequence with a difference of -2 is [7, 5, 3] which has length 3. Another one is [5, 3, 1] which has length 3.
'''

# Solution
def longest_arithmetic_subsequence(nums, diff):
    """
    Finds the length of the longest increasing subsequence with a specific difference.

    Args:
        nums: A list of integers.
        diff: The difference between consecutive elements in the subsequence.

    Returns:
        The length of the longest increasing subsequence with the given difference.
    """

    # Create a dictionary to store the length of the longest arithmetic subsequence
    # ending at each number.
    dp = {}

    # Initialize the maximum length to 0.
    max_length = 0

    # Iterate over the numbers in the input array.
    for num in nums:
        # If the number minus the difference is in the dictionary,
        # then the length of the longest arithmetic subsequence ending at the current number
        # is one more than the length of the longest arithmetic subsequence ending at the
        # number minus the difference.
        if num - diff in dp:
            dp[num] = dp[num - diff] + 1
        # Otherwise, the length of the longest arithmetic subsequence ending at the current number
        # is 1.
        else:
            dp[num] = 1

        # Update the maximum length.
        max_length = max(max_length, dp[num])

    # Return the maximum length.
    return max_length

# Test cases
def test_longest_arithmetic_subsequence():
    assert longest_arithmetic_subsequence([3, 0, 3, 4, 5, 6], 3) == 4
    assert longest_arithmetic_subsequence([1, 5, 7, 8, 5, 3, 4, 2, 1], -2) == 3
    assert longest_arithmetic_subsequence([1, 2, 3, 4, 5], 1) == 5
    assert longest_arithmetic_subsequence([1, 3, 5, 7, 9], 2) == 5
    assert longest_arithmetic_subsequence([1, 5, 9, 13, 17], 4) == 5
    assert longest_arithmetic_subsequence([1, 2, 3, 4, 5], -1) == 1
    assert longest_arithmetic_subsequence([1, 1, 1, 1, 1], 0) == 5
    assert longest_arithmetic_subsequence([1, 2, 3, 4, 5], 2) == 3
    assert longest_arithmetic_subsequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], 6) == 2
    assert longest_arithmetic_subsequence([4,12,10,0,7,9,2,8,1,11,3,5,6], 4) == 3
    print("All test cases passed")

if __name__ == "__main__":
    test_longest_arithmetic_subsequence()