# Python Question: Longest Increasing Subsequence with Given Starting Number
'''
Given an array of integers `nums` and a starting number `start`, find the length of the longest increasing subsequence (LIS) that starts with `start`.  The increasing subsequence must strictly increase. If `start` is not present in `nums`, return 0.

Example:
Input: nums = [1, 3, 2, 4, 5], start = 2
Output: 3
Explanation: The longest increasing subsequence starting with 2 is [2, 4, 5], which has a length of 3.

Input: nums = [1, 3, 2, 4, 5], start = 6
Output: 0
Explanation: 6 is not present in nums, so the length is 0.

Input: nums = [10, 22, 9, 33, 21, 50, 41, 60, 80], start = 10
Output: 6
Explanation: One possible LIS starting with 10 is [10, 22, 33, 41, 60, 80], which has a length of 6.
'''

# Solution
def longest_increasing_subsequence_with_start(nums, start):
    """
    Finds the length of the longest increasing subsequence (LIS) that starts with `start`.

    Args:
        nums: A list of integers.
        start: The starting number for the LIS.

    Returns:
        The length of the LIS starting with `start`.  Returns 0 if `start` is not found in `nums`.
    """

    if start not in nums:
        return 0

    # dp[i] stores the length of the longest increasing subsequence ending at nums[i]
    dp = {}  # Dictionary to store (index, length of LIS ending at that index)

    def solve(index, last_element):
        """
        Recursive function to find the length of the LIS starting from a given index.

        Args:
            index: The current index in the nums array.
            last_element: The last element included in the LIS so far.

        Returns:
            The length of the LIS starting from the given index.
        """
        if index == len(nums):
            return 0

        if (index, last_element) in dp:
            return dp[(index, last_element)]

        # Option 1: Exclude the current element
        exclude = solve(index + 1, last_element)

        # Option 2: Include the current element if it's greater than the last element
        include = 0
        if nums[index] > last_element:
            include = 1 + solve(index + 1, nums[index])

        dp[(index, last_element)] = max(exclude, include)
        return dp[(index, last_element)]

    # Find the index of the start element
    start_indices = [i for i, x in enumerate(nums) if x == start]
    max_len = 0

    for start_index in start_indices:
        dp = {}
        max_len = max(max_len, 1 + solve(start_index + 1, nums[start_index]))
    return max_len


# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_start([1, 3, 2, 4, 5], 2) == 3
    assert longest_increasing_subsequence_with_start([1, 3, 2, 4, 5], 6) == 0
    assert longest_increasing_subsequence_with_start([10, 22, 9, 33, 21, 50, 41, 60, 80], 10) == 6
    assert longest_increasing_subsequence_with_start([1, 2, 3, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_start([5, 4, 3, 2, 1], 5) == 1
    assert longest_increasing_subsequence_with_start([1, 5, 2, 4, 3], 1) == 3
    assert longest_increasing_subsequence_with_start([2,2,2,2,2], 2) == 1
    assert longest_increasing_subsequence_with_start([1, 3, 2, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_start([0, 1, 0, 3, 2, 3], 0) == 4
    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()