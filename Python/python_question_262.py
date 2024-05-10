# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) such that the difference between adjacent elements in the subsequence is exactly `k`.

Example:
Input: nums = [3, 10, 3, 15, 3, 5, 7], k = 2
Output: 4
Explanation: The longest increasing subsequence with a difference of 2 is [3, 5, 7, 9].
The subsequence [3, 5, 7] has length 3.  However, the subsequence [3, 5, 7, 9] needs to find the number 9, which is not in the original list. Note that the element 3 can be used multiple times.
Another possible longest increasing subsequence is [3, 5, 7, 9, 11, 13, 15]. But we can only use the elements that exist in the original list.
In this example, the longest increasing subsequence with difference 2 is [3, 5, 7] with length 3.
However, if we start with the second 3, we have [3, 5, 7]. However, the longest sequence is actually [3, 5, 7, 9, 11, 13, 15]. But 9, 11, 13 are not in the list. The longest one is [3, 5, 7] with length 3.

Input: nums = [1, 2, 3, 4, 5], k = 1
Output: 5
Explanation: The longest increasing subsequence with a difference of 1 is [1, 2, 3, 4, 5] with length 5.

Input: nums = [1, 5, 7, 9, 11, 13, 15], k = 2
Output: 7
'''

# Solution
def longest_increasing_subsequence_with_difference(nums, k):
    """
    Finds the length of the longest increasing subsequence with a specific difference.

    Args:
        nums: A list of integers.
        k: The required difference between adjacent elements in the subsequence.

    Returns:
        The length of the longest increasing subsequence with difference k.
    """

    # Create a dictionary to store the length of the longest increasing subsequence
    # ending at each number.
    dp = {}

    # Iterate through the numbers in the input list.
    for num in nums:
        # If the number minus k is already in the dictionary, it means we can
        # extend an existing subsequence.
        if num - k in dp:
            dp[num] = dp[num - k] + 1
        # Otherwise, this number starts a new subsequence of length 1.
        else:
            dp[num] = 1

    # Return the maximum value in the dictionary, which represents the length of
    # the longest increasing subsequence.
    return max(dp.values()) if dp else 0

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_difference([3, 10, 3, 15, 3, 5, 7], 2) == 3
    assert longest_increasing_subsequence_with_difference([1, 2, 3, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_difference([1, 5, 7, 9, 11, 13, 15], 2) == 7
    assert longest_increasing_subsequence_with_difference([1, 2, 3, 4, 5], 2) == 1
    assert longest_increasing_subsequence_with_difference([1, 3, 5, 7, 9], 2) == 5
    assert longest_increasing_subsequence_with_difference([1, 3, 5, 2, 4, 6], 2) == 3
    assert longest_increasing_subsequence_with_difference([], 2) == 0
    assert longest_increasing_subsequence_with_difference([5], 2) == 1
    assert longest_increasing_subsequence_with_difference([5, 5, 5, 5], 2) == 1
    assert longest_increasing_subsequence_with_difference([1, 3, 1, 3, 1, 3], 2) == 3
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()