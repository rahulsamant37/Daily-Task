# Python Question: Longest Increasing Subsequence with Given Starting Element
'''
Given an array of integers `nums` and a starting element `start`, find the length of the longest increasing subsequence (LIS) that starts with `start`.  An increasing subsequence is a sequence of elements from the array such that each element is strictly greater than the previous one. The subsequence must start with the given `start` element.

Example:
Input: nums = [10, 9, 2, 5, 3, 7, 101, 18], start = 2
Output: 4
Explanation: The longest increasing subsequence starting with 2 is [2, 5, 7, 18].

Input: nums = [4, 10, 4, 3, 8, 9], start = 4
Output: 3
Explanation: The longest increasing subsequence starting with 4 is [4, 8, 9].  Note that the first 4 is used.

Input: nums = [7,7,7,7,7,7,7], start = 7
Output: 1
Explanation: The longest increasing subsequence starting with 7 is [7].
'''

# Solution
def longest_increasing_subsequence_with_start(nums, start):
    """
    Finds the length of the longest increasing subsequence starting with a given element.

    Args:
        nums: A list of integers.
        start: The starting element for the subsequence.

    Returns:
        The length of the longest increasing subsequence starting with the start element.
    """

    # Find the index of the first occurrence of the start element.  If it doesn't exist, return 0
    try:
        start_index = nums.index(start)
    except ValueError:
        return 0

    # Initialize the LIS length to 1 (the starting element itself)
    max_length = 1

    # Recursive helper function to find the length of the LIS
    def find_lis_length(current_index, last_element):
        """
        Recursive helper function to find the length of the LIS.

        Args:
            current_index: The current index in the nums array.
            last_element: The last element in the current subsequence.

        Returns:
            The length of the LIS starting from the current element.
        """
        nonlocal max_length

        # Base case: if we reach the end of the array, return 0
        if current_index == len(nums):
            return 0

        # Option 1: Exclude the current element
        exclude_length = find_lis_length(current_index + 1, last_element)

        # Option 2: Include the current element if it's greater than the last element
        include_length = 0
        if nums[current_index] > last_element:
            include_length = 1 + find_lis_length(current_index + 1, nums[current_index])

        # Return the maximum length between including and excluding the current element
        return max(exclude_length, include_length)

    # Call the recursive helper function starting from the element after the start element
    # and the start element as the last element
    max_length += find_lis_length(start_index + 1, start)

    return max_length

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_start([10, 9, 2, 5, 3, 7, 101, 18], 2) == 4
    assert longest_increasing_subsequence_with_start([4, 10, 4, 3, 8, 9], 4) == 3
    assert longest_increasing_subsequence_with_start([7,7,7,7,7,7,7], 7) == 1
    assert longest_increasing_subsequence_with_start([1, 2, 3, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_start([5, 4, 3, 2, 1], 5) == 1
    assert longest_increasing_subsequence_with_start([1, 3, 2, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_start([1, 2, 3, 4, 5], 6) == 0
    assert longest_increasing_subsequence_with_start([], 1) == 0
    assert longest_increasing_subsequence_with_start([1], 1) == 1
    assert longest_increasing_subsequence_with_start([1, 5, 2, 4, 3], 1) == 4
    assert longest_increasing_subsequence_with_start([10,22,9,33,21,50,41,60,80], 10) == 6

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()