# Python Question: Longest Increasing Subsequence with Given Starting Element
'''
Given an array of integers `nums` and a starting element `start`, find the length of the longest increasing subsequence (LIS) that starts with the given `start` element.

An increasing subsequence is a sequence of elements from the array where each element is strictly greater than the previous one. The subsequence does not have to be contiguous.

If the starting element is not found in the array, return 0.

Example:
Input: nums = [1, 3, 2, 4, 5], start = 1
Output: 4
Explanation: The longest increasing subsequence starting with 1 is [1, 2, 4, 5].

Input: nums = [5, 4, 3, 2, 1], start = 5
Output: 1
Explanation: The longest increasing subsequence starting with 5 is [5].

Input: nums = [5, 4, 3, 2, 1], start = 6
Output: 0
Explanation: 6 is not in the array.
'''

# Solution
def longest_increasing_subsequence_with_start(nums, start):
    """
    Finds the length of the longest increasing subsequence (LIS) starting with the given `start` element.

    Args:
        nums: A list of integers.
        start: The starting element for the LIS.

    Returns:
        The length of the LIS starting with `start`. Returns 0 if `start` is not found in `nums`.
    """

    if start not in nums:
        return 0

    # Find the index of the first occurrence of the start element.
    start_index = nums.index(start)

    # Use dynamic programming to find the LIS.
    # dp[i] stores the length of the LIS ending at index i.
    dp = [1] * len(nums)

    # Iterate through the array starting from the start_index.
    for i in range(start_index, len(nums)):
        # Iterate through the elements before the current element.
        for j in range(start_index, i):
            # If the current element is greater than the previous element,
            # and the LIS ending at the previous element + 1 is greater than the current LIS length,
            # update the LIS length.
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    # Find the maximum LIS length starting from the start_index.
    max_len = 0
    for i in range(start_index, len(nums)):
        max_len = max(max_len, dp[i])

    return max_len

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_start([1, 3, 2, 4, 5], 1) == 4
    assert longest_increasing_subsequence_with_start([5, 4, 3, 2, 1], 5) == 1
    assert longest_increasing_subsequence_with_start([5, 4, 3, 2, 1], 6) == 0
    assert longest_increasing_subsequence_with_start([1, 2, 3, 4, 5], 3) == 3
    assert longest_increasing_subsequence_with_start([10, 22, 9, 33, 21, 50, 41, 60, 80], 10) == 6
    assert longest_increasing_subsequence_with_start([1, 101, 2, 3, 100, 4, 5], 3) == 3
    assert longest_increasing_subsequence_with_start([0,1,0,3,2,3], 0) == 4
    assert longest_increasing_subsequence_with_start([1,3,6,7,9,4,10,5,6], 1) == 7
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()