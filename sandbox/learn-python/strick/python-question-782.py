# Python Question: Longest Increasing Subsequence with Given Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence where the difference between consecutive elements is exactly `diff`.

Example:
Input: nums = [3, 0, 3, 4, 5, 6], diff = 3
Output: 4
Explanation: The longest increasing subsequence with a difference of 3 is [0, 3, 6], which has a length of 3.  Another one is [3, 6]. The subsequence [3,4,5,6] is of length 4 but the difference between consecutive elements is 1, so it does not satisfy the condition.

Input: nums = [1,5,7,8,5,3,4,2,1], diff = -2
Output: 4
Explanation: The longest increasing subsequence with a difference of -2 is [7, 5, 3, 1], which has a length of 4.
'''

# Solution
def longest_increasing_subsequence_with_diff(nums, diff):
    """
    Finds the length of the longest increasing subsequence with a given difference.

    Args:
        nums: A list of integers.
        diff: The required difference between consecutive elements in the subsequence.

    Returns:
        The length of the longest increasing subsequence with the given difference.
    """
    # Use a dictionary to store the length of the longest increasing subsequence
    # ending at each number.
    dp = {}  # key: number, value: length of LIS ending at that number

    max_len = 0  # Initialize the maximum length found so far

    for num in nums:
        # If the number - diff is in the dictionary, it means we can extend
        # an existing subsequence.
        if num - diff in dp:
            dp[num] = dp[num - diff] + 1
        else:
            # Otherwise, we start a new subsequence of length 1.
            dp[num] = 1

        # Update the maximum length found so far.
        max_len = max(max_len, dp[num])

    return max_len


# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_diff([3, 0, 3, 4, 5, 6], 3) == 3
    assert longest_increasing_subsequence_with_diff([1, 5, 7, 8, 5, 3, 4, 2, 1], -2) == 4
    assert longest_increasing_subsequence_with_diff([1, 2, 3, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_diff([1, 2, 3, 4, 5], 2) == 1
    assert longest_increasing_subsequence_with_diff([1, 3, 5, 7, 9], 2) == 5
    assert longest_increasing_subsequence_with_diff([5, 4, 3, 2, 1], -1) == 5
    assert longest_increasing_subsequence_with_diff([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_diff([1, 1, 1, 1, 1], 0) == 5
    assert longest_increasing_subsequence_with_diff([], 1) == 0
    assert longest_increasing_subsequence_with_diff([5], 2) == 1
    assert longest_increasing_subsequence_with_diff([1,2,3,1,2,3,4,5], 1) == 5
    assert longest_increasing_subsequence_with_diff([1,2,3,1,2,3,4,5], -1) == 1
    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()