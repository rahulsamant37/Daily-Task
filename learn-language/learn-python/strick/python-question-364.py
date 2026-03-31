# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence (LIS) where the difference between consecutive elements in the subsequence is exactly `diff`.

Example:
Input: nums = [3, 0, 3, 2, 4, 5], diff = 1
Output: 3
Explanation: The longest increasing subsequence with a difference of 1 is [2, 3, 4] or [3, 4, 5], both with a length of 3.

Input: nums = [1, 5, 7, 8, 5, 3, 4, 2, 1], diff = -2
Output: 4
Explanation: The longest increasing subsequence with a difference of -2 is [7, 5, 3, 1], with a length of 4.

Input: nums = [1, 2, 3, 4, 5], diff = 0
Output: 1
Explanation: The longest increasing subsequence with a difference of 0 must have all same elements. The longest subsequence are [1], [2], [3], [4], [5].
'''

# Solution
def solution(nums, diff):
    """
    Finds the length of the longest increasing subsequence with a specific difference.

    Args:
        nums: A list of integers.
        diff: The required difference between consecutive elements in the subsequence.

    Returns:
        The length of the longest increasing subsequence with the specified difference.
    """
    # Use a dictionary to store the length of the longest increasing subsequence ending at each number.
    # The key is the number, and the value is the length.
    dp = {}

    # Iterate through the numbers in the input array.
    for num in nums:
        # If the number minus the difference is already in the dictionary,
        # it means we can extend an existing subsequence.
        if num - diff in dp:
            # The length of the new subsequence ending at the current number
            # is one more than the length of the subsequence ending at num - diff.
            dp[num] = dp[num - diff] + 1
        else:
            # Otherwise, the current number starts a new subsequence of length 1.
            dp[num] = 1

    # The length of the longest increasing subsequence is the maximum value in the dictionary.
    if not dp:
        return 0 # Handle empty input case
    return max(dp.values())

# Test cases
def test_solution():
    assert solution([3, 0, 3, 2, 4, 5], 1) == 3
    assert solution([1, 5, 7, 8, 5, 3, 4, 2, 1], -2) == 4
    assert solution([1, 2, 3, 4, 5], 0) == 1
    assert solution([1, 1, 1, 1, 1], 0) == 5
    assert solution([1, 2, 3, 4, 5], 1) == 2
    assert solution([5, 4, 3, 2, 1], -1) == 2
    assert solution([], 1) == 0
    assert solution([1], 1) == 1
    assert solution([1,3,5,7], 2) == 4
    assert solution([7,5,3,1], -2) == 4
    print("All test cases passed")

if __name__ == "__main__":
    test_solution()