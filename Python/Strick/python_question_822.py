# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence where the difference between consecutive elements in the subsequence is exactly `diff`.

Example:
Input: nums = [3, 0, 3, 2, 4, 5], diff = 1
Output: 3
Explanation: The longest increasing subsequence with a difference of 1 is [2, 3, 4] or [3, 4, 5].  The length is 3.

Input: nums = [1, 5, 7, 8, 5, 3, 4, 2, 1], diff = -2
Output: 4
Explanation: The longest increasing subsequence with a difference of -2 is [7, 5, 3, 1]. The length is 4.
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

    # Create a dictionary to store the length of the longest arithmetic subsequence ending at each number.
    dp = {}  # Key: number, Value: length of LIS ending at that number

    # Iterate over the numbers in the input array.
    for num in nums:
        # If the number minus the difference is in the dictionary, then we can extend the subsequence ending at that number.
        if num - diff in dp:
            dp[num] = dp[num - diff] + 1
        # Otherwise, this is the start of a new subsequence of length 1.
        else:
            dp[num] = 1

    # Return the maximum length of all the subsequences.
    return max(dp.values()) if dp else 0


# Test cases
def test_solution():
    assert longest_arithmetic_subsequence([3, 0, 3, 2, 4, 5], 1) == 3
    assert longest_arithmetic_subsequence([1, 5, 7, 8, 5, 3, 4, 2, 1], -2) == 4
    assert longest_arithmetic_subsequence([1, 2, 3, 4, 5], 1) == 5
    assert longest_arithmetic_subsequence([1, 3, 5, 7, 9], 2) == 5
    assert longest_arithmetic_subsequence([1, 3, 5, 7, 9], 1) == 1
    assert longest_arithmetic_subsequence([1, 1, 1, 1, 1], 0) == 5
    assert longest_arithmetic_subsequence([], 1) == 0
    assert longest_arithmetic_subsequence([5], 2) == 1
    assert longest_arithmetic_subsequence([0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15], 6) == 3
    assert longest_arithmetic_subsequence([4,12,10,0,2,10,7,8,5,11,1,14,6,1,12,13,0,10,14,3,6,4,6,1,9,11,14,4,13,13,12,11,5,12,6,0,13,13,10,10,15,15,1,13,1,14,4,13,5,10,12,10,0,10,10,14,3,13,14,10,8,1,14,7,6,11,1,8,15,0,14,10,13,2,10,13,0,5,3,12,10,6,14,13,15,0,8,5,7,11,2,1,12,0,12,12,12,15], 0) == 4
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()