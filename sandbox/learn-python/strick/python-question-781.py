# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence (LIS) such that the difference between consecutive elements in the subsequence is exactly `diff`.

Example:
Input: nums = [3, 0, 3, 4, 5, 6], diff = 3
Output: 4
Explanation: The longest increasing subsequence with a difference of 3 is [0, 3, 6], or [3, 6] which is not the longest, or [3, 0, 3, 6] which is not increasing. One possible LIS is [3, 6]. The length is 2. Another possible LIS is [0, 3, 6]. The length is 3.  Another possible LIS is [3, 4, 5, 6] with diff = 1, but we require diff = 3. The correct LIS is [3, 6] or [0, 3, 6], so the length is 3.
Another example:
Input: nums = [1,5,7,8,5,3,4,2,1], diff = -2
Output: 4
Explanation: The longest increasing subsequence with a difference of -2 is [7, 5, 3, 1]. The length is 4.
'''

# Solution
def longest_increasing_subsequence_with_diff(nums, diff):
    """
    Finds the length of the longest increasing subsequence with a specific difference.

    Args:
        nums: A list of integers.
        diff: The required difference between consecutive elements in the subsequence.

    Returns:
        The length of the longest increasing subsequence with the given difference.
    """

    # Use a dictionary to store the length of the longest increasing subsequence
    # ending at each number.  The key is the number, and the value is the length.
    dp = {}

    # Iterate through the numbers in the input array.
    for num in nums:
        # If the number - diff is in the dictionary, it means we can extend an
        # existing subsequence.
        if num - diff in dp:
            # The length of the subsequence ending at the current number is one more
            # than the length of the subsequence ending at num - diff.
            dp[num] = dp[num - diff] + 1
        else:
            # If num - diff is not in the dictionary, it means we are starting a new
            # subsequence.  The length of the subsequence ending at the current
            # number is 1.
            dp[num] = 1

    # The maximum value in the dictionary is the length of the longest increasing
    # subsequence.
    if not dp:
        return 0
    return max(dp.values())

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_diff([3, 0, 3, 4, 5, 6], 3) == 3
    assert longest_increasing_subsequence_with_diff([1, 5, 7, 8, 5, 3, 4, 2, 1], -2) == 4
    assert longest_increasing_subsequence_with_diff([1, 2, 3, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_diff([1, 3, 5, 7, 9], 2) == 5
    assert longest_increasing_subsequence_with_diff([1, 2, 3, 4, 5], 2) == 1
    assert longest_increasing_subsequence_with_diff([1, 2, 4, 6, 8], 2) == 4
    assert longest_increasing_subsequence_with_diff([5, 4, 3, 2, 1], -1) == 5
    assert longest_increasing_subsequence_with_diff([1, 1, 1, 1, 1], 0) == 5
    assert longest_increasing_subsequence_with_diff([], 1) == 0
    assert longest_increasing_subsequence_with_diff([5], 2) == 1
    assert longest_increasing_subsequence_with_diff([1,2,3,4,5,6,7,8,9], 0) == 1
    assert longest_increasing_subsequence_with_diff([10,12,14,16,18], 2) == 5
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()