# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence (LIS) such that the difference between consecutive elements in the subsequence is exactly `diff`.

Example:
Input: nums = [3, 0, 3, 2, 4, 5], diff = 1
Output: 3
Explanation: The longest increasing subsequence with a difference of 1 is [3, 4, 5], which has length 3.

Input: nums = [1, 5, 7, 8, 5, 3, 4, 2, 1], diff = -2
Output: 4
Explanation: The longest increasing subsequence with a difference of -2 is [7, 5, 3, 1], which has length 4.
'''

# Solution
def longest_increasing_subsequence_with_diff(nums, diff):
    """
    Finds the length of the longest increasing subsequence with a specific difference.

    Args:
        nums: A list of integers.
        diff: The required difference between consecutive elements.

    Returns:
        The length of the longest increasing subsequence with the specified difference.
    """

    # Create a dictionary to store the length of the longest increasing subsequence ending at each number.
    # The key is the number, and the value is the length of the longest increasing subsequence ending at that number.
    dp = {}

    # Iterate through the numbers in the input array.
    for num in nums:
        # If the number minus the difference is in the dictionary, then we can extend the longest increasing subsequence ending at that number.
        if num - diff in dp:
            dp[num] = dp[num - diff] + 1
        # Otherwise, the longest increasing subsequence ending at this number is just 1.
        else:
            dp[num] = 1

    # Return the maximum value in the dictionary.
    return max(dp.values()) if dp else 0

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_diff([3, 0, 3, 2, 4, 5], 1) == 3
    assert longest_increasing_subsequence_with_diff([1, 5, 7, 8, 5, 3, 4, 2, 1], -2) == 4
    assert longest_increasing_subsequence_with_diff([1, 2, 3, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_diff([1, 2, 3, 4, 5], 0) == 1
    assert longest_increasing_subsequence_with_diff([5, 4, 3, 2, 1], -1) == 5
    assert longest_increasing_subsequence_with_diff([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_diff([1, 1, 1, 1, 1], 0) == 5
    assert longest_increasing_subsequence_with_diff([], 1) == 0
    assert longest_increasing_subsequence_with_diff([7,7,7,7,7], 0) == 5
    assert longest_increasing_subsequence_with_diff([4,12,10,0,-2,10,7,9,-2,6,10,-9,1,-7,7,-8,9,11,-5,-3,7,-1,6,-10,-6,0,6,10,1,-1,-2,0,3,-8,9,1,-1,10,7,5,6,-5,4,8,9,2,12,3,-3,5,10,1,9], 0) == 3

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()