# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence (LIS) where the difference between consecutive elements in the subsequence is exactly `diff`.

Example:
Input: nums = [3, 0, 3, 4, 5, 6], diff = 3
Output: 4
Explanation: The longest increasing subsequence with a difference of 3 is [0, 3, 6], so the length is 3. Another one is [3, 6], so the length is 2. The longest one should be [3, 0, 3, 4, 5, 6] -> [3,6]. The longest is [3,0,3]->[0,3,6] or [3,6], [4,5] is not valid because diff = 3. Therefore, the longest subsequence with difference 3 is [3,6], with length 2. However, the actual correct longest subsequence is [3,6].
Another example:
Input: nums = [1, 5, 7, 8, 5, 3, 4, 2, 1], diff = -2
Output: 4
Explanation: One possible longest increasing subsequence with a difference of -2 is [7, 5, 3, 1], so the length is 4.
'''

# Solution
def longest_increasing_subsequence_with_diff(nums, diff):
    """
    Finds the length of the longest increasing subsequence with a specific difference.

    Args:
        nums: A list of integers.
        diff: The required difference between consecutive elements in the subsequence.

    Returns:
        The length of the longest increasing subsequence.
    """
    # Use a dictionary to store the length of the longest increasing subsequence ending at each number.
    dp = {}  # key: number, value: length of LIS ending at that number

    # Iterate through the numbers in the array.
    for num in nums:
        # If the number - diff is already in the dictionary, then we can extend the subsequence
        # ending at number - diff by adding the current number.
        if num - diff in dp:
            dp[num] = dp[num - diff] + 1
        # Otherwise, the longest increasing subsequence ending at the current number is just 1.
        else:
            dp[num] = 1

    # The maximum value in the dictionary is the length of the longest increasing subsequence.
    if not dp:
        return 0
    return max(dp.values())

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_diff([3, 0, 3, 4, 5, 6], 3) == 2
    assert longest_increasing_subsequence_with_diff([1, 5, 7, 8, 5, 3, 4, 2, 1], -2) == 4
    assert longest_increasing_subsequence_with_diff([1, 2, 3, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_diff([1, 3, 5, 7, 9], 2) == 5
    assert longest_increasing_subsequence_with_diff([5, 4, 3, 2, 1], -1) == 5
    assert longest_increasing_subsequence_with_diff([1, 2, 3, 4, 5], 0) == 1
    assert longest_increasing_subsequence_with_diff([1, 1, 1, 1, 1], 0) == 5
    assert longest_increasing_subsequence_with_diff([], 1) == 0
    assert longest_increasing_subsequence_with_diff([1], 1) == 1
    assert longest_increasing_subsequence_with_diff([1, 4, 7, 10], 3) == 4
    assert longest_increasing_subsequence_with_diff([1, 5, 9, 13], 4) == 4
    assert longest_increasing_subsequence_with_diff([0,0,0], 0) == 3
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()