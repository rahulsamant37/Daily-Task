# Python Question: Longest Increasing Subsequence with Given Starting Element
'''
Given an array of integers `nums` and a starting element `start`, find the length of the longest increasing subsequence (LIS) that starts with `start`.  An increasing subsequence is a sequence of elements from the array such that each element is strictly greater than the previous one. The elements in the subsequence do not need to be contiguous in the original array.

If `start` is not present in `nums`, return 0.

Example:
Input: nums = [1, 3, 2, 4, 5], start = 1
Output: 4
Explanation: The longest increasing subsequence starting with 1 is [1, 2, 4, 5].

Input: nums = [5, 4, 3, 2, 1], start = 10
Output: 0
Explanation: 10 is not in nums.

Input: nums = [10, 22, 9, 33, 21, 50, 41, 60, 80], start = 10
Output: 6
Explanation: The longest increasing subsequence starting with 10 is [10, 22, 33, 41, 50, 60, 80].  However, we can also get [10, 22, 33, 50, 60, 80] which has length 6.
'''

# Solution
def longest_increasing_subsequence_with_start(nums, start):
    """
    Finds the length of the longest increasing subsequence starting with a given element.

    Args:
        nums: A list of integers.
        start: The starting element for the subsequence.

    Returns:
        The length of the longest increasing subsequence starting with `start`.
    """

    if start not in nums:
        return 0

    def find_lis_length(current_subsequence, remaining_nums):
        """
        Recursively finds the length of the longest increasing subsequence.

        Args:
            current_subsequence: The current increasing subsequence being built.
            remaining_nums: The remaining elements in the array to consider.

        Returns:
            The length of the longest increasing subsequence found.
        """

        if not remaining_nums:
            return len(current_subsequence)

        max_length = len(current_subsequence)  # Initialize with the length of the current subsequence

        # Iterate through the remaining numbers
        for i in range(len(remaining_nums)):
            # Check if the current number is greater than the last number in the subsequence
            if not current_subsequence or remaining_nums[i] > current_subsequence[-1]:
                # If it is, recursively call the function with the current number added to the subsequence
                max_length = max(max_length, find_lis_length(current_subsequence + [remaining_nums[i]], remaining_nums[i+1:]))

        return max_length

    # Find the index of the starting element in the array.
    start_index = nums.index(start)

    # Call the recursive function to find the LIS length.
    return find_lis_length([start], nums[start_index+1:])

# Test cases
def test_solution():
    """
    Tests the longest_increasing_subsequence_with_start function.
    """

    assert longest_increasing_subsequence_with_start([1, 3, 2, 4, 5], 1) == 4
    assert longest_increasing_subsequence_with_start([5, 4, 3, 2, 1], 10) == 0
    assert longest_increasing_subsequence_with_start([10, 22, 9, 33, 21, 50, 41, 60, 80], 10) == 6
    assert longest_increasing_subsequence_with_start([1, 2, 3, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_start([5, 4, 3, 2, 1], 5) == 1
    assert longest_increasing_subsequence_with_start([1, 5, 2, 4, 3], 1) == 3
    assert longest_increasing_subsequence_with_start([1, 2, 3, 4, 5], 3) == 3
    assert longest_increasing_subsequence_with_start([1, 1, 1, 1, 1], 1) == 1
    assert longest_increasing_subsequence_with_start([1, 2, 3, 4, 5], 6) == 0
    assert longest_increasing_subsequence_with_start([1], 1) == 1
    assert longest_increasing_subsequence_with_start([2,1,5,3,6,4,8,9,7], 2) == 6
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()