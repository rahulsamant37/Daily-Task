# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence (LIS) such that the difference between consecutive elements in the subsequence is exactly `diff`.

Example:
Input: nums = [3, 0, 3, 4, 5], diff = 3
Output: 3
Explanation: The longest increasing subsequence with a difference of 3 is [0, 3, 6]. In the given array, [0, 3], [3, 6] are not present. However [0, 3, 6] is not constructable from the input.
The longest increasing subsequence with a difference of 3 is [0, 3]. However, we can also have [3, 0, 3, 4, 5], thus [3, 3, 3] is not acceptable.
The longest increasing subsequence with a difference of 3 is [3]. However, we can also have [0].

Input: nums = [1,5,7,8,5,3,4,2,1], diff = -2
Output: 4
Explanation: The longest increasing subsequence with a difference of -2 is [7, 5, 3, 1].

Input: nums = [1, 3, 5, 7], diff = 2
Output: 4
Explanation: The longest increasing subsequence with a difference of 2 is [1, 3, 5, 7].
'''

# Solution
def longest_increasing_subsequence_with_diff(nums, diff):
    """
    Finds the length of the longest increasing subsequence with a specific difference.

    Args:
        nums: A list of integers.
        diff: The difference between consecutive elements in the subsequence.

    Returns:
        The length of the longest increasing subsequence with the given difference.
    """

    # Create a dictionary to store the length of the longest increasing subsequence
    # ending at each number.
    dp = {}

    # Iterate over the numbers in the array.
    for num in nums:
        # If the number minus the difference is in the dictionary, then the length
        # of the longest increasing subsequence ending at the current number is
        # one more than the length of the longest increasing subsequence ending at
        # the number minus the difference.
        if num - diff in dp:
            dp[num] = dp[num - diff] + 1
        # Otherwise, the length of the longest increasing subsequence ending at
        # the current number is 1.
        else:
            dp[num] = 1

    # Return the maximum value in the dictionary.
    return max(dp.values()) if dp else 0

# Test cases
def test_longest_increasing_subsequence_with_diff():
    assert longest_increasing_subsequence_with_diff([3, 0, 3, 4, 5], 3) == 2
    assert longest_increasing_subsequence_with_diff([1,5,7,8,5,3,4,2,1], -2) == 4
    assert longest_increasing_subsequence_with_diff([1, 3, 5, 7], 2) == 4
    assert longest_increasing_subsequence_with_diff([1, 2, 3, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_diff([5, 4, 3, 2, 1], -1) == 5
    assert longest_increasing_subsequence_with_diff([1, 2, 3, 4, 5], -1) == 1
    assert longest_increasing_subsequence_with_diff([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_diff([1, 1, 1, 1, 1], 0) == 5
    assert longest_increasing_subsequence_with_diff([], 0) == 0
    assert longest_increasing_subsequence_with_diff([7, 7, 7, 7, 7], 0) == 5
    assert longest_increasing_subsequence_with_diff([7, 7, 7, 7, 7], 1) == 1
    print("All test cases passed")

if __name__ == "__main__":
    test_longest_increasing_subsequence_with_diff()