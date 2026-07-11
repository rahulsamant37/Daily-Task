# Python Question: Find the Longest Increasing Subsequence with Given Starting Number
'''
Given an array of integers `nums` and a starting number `start`, find the length of the longest increasing subsequence (LIS) that starts with the given `start` number.
An increasing subsequence is a sequence of numbers from the array such that each number is strictly greater than the previous one. The subsequence doesn't have to be contiguous.

Example:
Input: nums = [10, 9, 2, 5, 3, 7, 101, 18], start = 2
Output: 4
Explanation: The longest increasing subsequence starting with 2 is [2, 5, 7, 18], which has a length of 4.

Input: nums = [4, 10, 4, 3, 8, 9], start = 4
Output: 3
Explanation: The longest increasing subsequences starting with 4 are [4, 8, 9] and [4, 10], which has a length of 3.

Input: nums = [7, 8, 9, 1, 2, 3], start = 4
Output: 0
Explanation: Because 4 is not in `nums`, return 0.

Input: nums = [7, 8, 9, 1, 2, 3], start = 7
Output: 3
Explanation: The longest increasing subsequence starting with 7 is [7, 8, 9], which has a length of 3.
'''

# Solution
def longest_increasing_subsequence_with_start(nums, start):
    """
    Finds the length of the longest increasing subsequence (LIS) in `nums` that starts with `start`.

    Args:
        nums: A list of integers.
        start: The starting number for the LIS.

    Returns:
        The length of the LIS that starts with `start`.  Returns 0 if `start` is not in `nums` or if no increasing sequence can be constructed.
    """

    if start not in nums:
        return 0

    def find_lis(current_num, remaining_nums):
        """
        Recursively finds the length of the longest increasing subsequence starting with current_num.

        Args:
            current_num: The last number added to the subsequence.
            remaining_nums: The remaining numbers to consider in the subsequence.

        Returns:
            The length of the longest increasing subsequence starting with current_num.
        """
        max_len = 0
        for i in range(len(remaining_nums)):
            if remaining_nums[i] > current_num:
                max_len = max(max_len, 1 + find_lis(remaining_nums[i], remaining_nums[i+1:])) # Explore further sequences including nums[i]
        return max_len

    # Find the index of the first occurence of start.
    start_index = nums.index(start)
    return 1 + find_lis(start, nums[start_index + 1:])

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_start([10, 9, 2, 5, 3, 7, 101, 18], 2) == 4
    assert longest_increasing_subsequence_with_start([4, 10, 4, 3, 8, 9], 4) == 3
    assert longest_increasing_subsequence_with_start([7, 8, 9, 1, 2, 3], 4) == 0
    assert longest_increasing_subsequence_with_start([7, 8, 9, 1, 2, 3], 7) == 3
    assert longest_increasing_subsequence_with_start([1, 2, 3, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_start([5, 4, 3, 2, 1], 5) == 1
    assert longest_increasing_subsequence_with_start([1, 5, 2, 6, 3, 7, 4, 8], 1) == 8
    assert longest_increasing_subsequence_with_start([1, 2, 3, 4, 5], 3) == 3
    assert longest_increasing_subsequence_with_start([2,2,2,2,2], 2) == 1
    assert longest_increasing_subsequence_with_start([1,100,2,3,4,5], 1) == 6
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()