# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence (LIS) where the difference between consecutive elements in the subsequence is exactly `diff`.

Example:
Input: nums = [3, 0, 3, 4, 5, 6], diff = 3
Output: 4
Explanation: The longest increasing subsequence with a difference of 3 is [0, 3, 6], which has a length of 3.  Another possible LIS is [3, 6] with length 2. However, [3, 4, 5, 6] is also a valid LIS with a difference of 1 (not diff=3).  The longest subsequence with diff=3 is [3, 6], [0, 3, 6], [3, 0]. The subsequence [3, 0] is invalid because it is not increasing. The longest increasing subsequence with a difference of 3 is [3, 6]. However, the problem states that the subsequence must be increasing. Therefore, [0, 3, 6] with length 3 is a possible LIS. [3, 6] is also a possible LIS with length 2.

Input: nums = [1, 5, 7, 8, 5, 3, 4, 2, 1], diff = -2
Output: 4
Explanation: The longest increasing subsequence with a difference of -2 is [7, 5, 3, 1], which has a length of 4.

Input: nums = [1, 2, 3, 4, 5], diff = 1
Output: 5
Explanation: The longest increasing subsequence with a difference of 1 is [1, 2, 3, 4, 5], which has a length of 5.
'''

# Solution
def longest_increasing_subsequence_with_difference(nums, diff):
    """
    Finds the length of the longest increasing subsequence in `nums`
    where the difference between consecutive elements is exactly `diff`.

    Args:
        nums: A list of integers.
        diff: The required difference between consecutive elements.

    Returns:
        The length of the longest increasing subsequence with the specified difference.
    """

    # Use a dictionary to store the length of the LIS ending at each number.
    # The key is the number, and the value is the length of the LIS ending at that number.
    dp = {}

    # Iterate through the numbers in the input array.
    for num in nums:
        # If the number minus the difference is already in the dp dictionary,
        # then we can extend the LIS ending at that number by adding the current number.
        if num - diff in dp:
            dp[num] = dp[num - diff] + 1
        # Otherwise, the LIS ending at the current number has length 1.
        else:
            dp[num] = 1

    # Return the maximum value in the dp dictionary.
    return max(dp.values()) if dp else 0

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_difference([3, 0, 3, 4, 5, 6], 3) == 3
    assert longest_increasing_subsequence_with_difference([1, 5, 7, 8, 5, 3, 4, 2, 1], -2) == 4
    assert longest_increasing_subsequence_with_difference([1, 2, 3, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_difference([1, 2, 3, 4, 5], 0) == 1
    assert longest_increasing_subsequence_with_difference([1, 1, 1, 1, 1], 0) == 5
    assert longest_increasing_subsequence_with_difference([], 1) == 0
    assert longest_increasing_subsequence_with_difference([5], 2) == 1
    assert longest_increasing_subsequence_with_difference([1, 3, 5, 7, 9], 2) == 5
    assert longest_increasing_subsequence_with_difference([9, 7, 5, 3, 1], -2) == 5
    assert longest_increasing_subsequence_with_difference([1, 2, 4, 6, 8, 10], 2) == 5

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()