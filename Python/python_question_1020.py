# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence (LIS) where the difference between consecutive elements in the subsequence is exactly `diff`.

Example:
Input: nums = [3, 0, 3, 4, 5, 6], diff = 3
Output: 4
Explanation: The longest increasing subsequence with a difference of 3 is [0, 3, 6] (length 3) or [3,6] (length 2) or [3,6,9] if we had a 9. Considering [3, 4, 5, 6], the subsequence is [3,6]. Considering [0,3,4,5,6], the longest subsequence is [0,3,6]. Now considering [3,0,3,4,5,6], the longest subsequence is [3,6]. If diff =1, the longest subsequence is [3,4,5,6] with length 4.
Input: nums = [1, 5, 7, 8, 5, 3, 4, 2, 1], diff = -2
Output: 4
Explanation: The longest increasing subsequence with a difference of -2 is [7, 5, 3, 1] (length 4).
'''

# Solution
def longest_increasing_subsequence_with_diff(nums, diff):
    """
    Finds the length of the longest increasing subsequence (LIS) where the difference
    between consecutive elements in the subsequence is exactly `diff`.

    Args:
        nums: A list of integers.
        diff: The required difference between consecutive elements.

    Returns:
        The length of the longest increasing subsequence with the specified difference.
    """

    # Use a dictionary to store the length of the longest increasing subsequence
    # ending at each number. The key is the number, and the value is the length.
    dp = {}

    # Iterate through the numbers in the input array
    for num in nums:
        # If the number - diff is already in the dp, it means there is a subsequence
        # ending at num - diff. In this case, we can extend that subsequence by adding
        # the current number to it.
        if num - diff in dp:
            dp[num] = dp[num - diff] + 1
        # Otherwise, the longest increasing subsequence ending at the current number
        # is just 1 (the number itself).
        else:
            dp[num] = 1

    # Find the maximum value in the dp dictionary, which is the length of the
    # longest increasing subsequence with the specified difference.
    if not dp:
      return 0
    return max(dp.values())


# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_diff([3, 0, 3, 4, 5, 6], 3) == 4
    assert longest_increasing_subsequence_with_diff([1, 5, 7, 8, 5, 3, 4, 2, 1], -2) == 4
    assert longest_increasing_subsequence_with_diff([1, 2, 3, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_diff([1, 2, 3, 4, 5], 0) == 1
    assert longest_increasing_subsequence_with_diff([1, 2, 3, 4, 5], -1) == 1
    assert longest_increasing_subsequence_with_diff([5, 4, 3, 2, 1], -1) == 5
    assert longest_increasing_subsequence_with_diff([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_diff([1, 1, 1, 1, 1], 0) == 5
    assert longest_increasing_subsequence_with_diff([1, 1, 1, 1, 1], 1) == 1
    assert longest_increasing_subsequence_with_diff([], 1) == 0
    assert longest_increasing_subsequence_with_diff([1], 1) == 1
    assert longest_increasing_subsequence_with_diff([1,3,5,7,9], 2) == 5
    assert longest_increasing_subsequence_with_diff([9,7,5,3,1], -2) == 5
    assert longest_increasing_subsequence_with_diff([0, 1, 2, 3, 4, 5, 6, 7], 1) == 8
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()