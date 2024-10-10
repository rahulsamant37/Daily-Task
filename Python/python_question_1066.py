# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence (LIS) where the difference between consecutive elements in the subsequence is exactly `diff`.

Example:
Input: nums = [3, 0, 3, 2, 4, 5], diff = 1
Output: 3
Explanation: The longest increasing subsequence with a difference of 1 is [2, 3, 4] or [3, 4, 5].  Both have length 3.

Input: nums = [1, 5, 7, 8, 5, 3, 4, 2, 1], diff = -2
Output: 4
Explanation: The longest increasing subsequence with a difference of -2 is [7, 5, 3, 1].

Input: nums = [4, 12, 10, 0, -2, 10, -7, -9, 2, -10, -4, 11, 10, 10, 14, 13, 14, 10, 0, 12], diff = 3
Output: 3
'''

# Solution
def longest_increasing_subsequence_with_diff(nums, diff):
    """
    Finds the length of the longest increasing subsequence in `nums` with a difference of `diff`.

    Args:
        nums: A list of integers.
        diff: The required difference between consecutive elements in the subsequence.

    Returns:
        The length of the longest increasing subsequence with the specified difference.
    """

    # Create a dictionary to store the length of the LIS ending at each number.
    # The key is the number, and the value is the length of the LIS ending at that number.
    lis_lengths = {}

    # Iterate through the numbers in the input array.
    for num in nums:
        # If the number minus the difference is already in the dictionary,
        # it means we can extend an existing LIS.
        if num - diff in lis_lengths:
            lis_lengths[num] = lis_lengths[num - diff] + 1
        # Otherwise, this number starts a new LIS of length 1.
        else:
            lis_lengths[num] = 1

    # Find the maximum length of the LIS in the dictionary.
    max_length = 0
    for length in lis_lengths.values():
        max_length = max(max_length, length)

    return max_length

# Test cases
def test_longest_increasing_subsequence_with_diff():
    """
    Tests the longest_increasing_subsequence_with_diff function with various test cases.
    """

    # Test case 1
    nums1 = [3, 0, 3, 2, 4, 5]
    diff1 = 1
    expected1 = 3
    assert longest_increasing_subsequence_with_diff(nums1, diff1) == expected1, f"Test Case 1 Failed: Expected {expected1}, got {longest_increasing_subsequence_with_diff(nums1, diff1)}"

    # Test case 2
    nums2 = [1, 5, 7, 8, 5, 3, 4, 2, 1]
    diff2 = -2
    expected2 = 4
    assert longest_increasing_subsequence_with_diff(nums2, diff2) == expected2, f"Test Case 2 Failed: Expected {expected2}, got {longest_increasing_subsequence_with_diff(nums2, diff2)}"

    # Test case 3
    nums3 = [4, 12, 10, 0, -2, 10, -7, -9, 2, -10, -4, 11, 10, 10, 14, 13, 14, 10, 0, 12]
    diff3 = 3
    expected3 = 3
    assert longest_increasing_subsequence_with_diff(nums3, diff3) == expected3, f"Test Case 3 Failed: Expected {expected3}, got {longest_increasing_subsequence_with_diff(nums3, diff3)}"

    # Test case 4: Empty array
    nums4 = []
    diff4 = 2
    expected4 = 0
    assert longest_increasing_subsequence_with_diff(nums4, diff4) == expected4, f"Test Case 4 Failed: Expected {expected4}, got {longest_increasing_subsequence_with_diff(nums4, diff4)}"

    # Test case 5: No valid subsequence
    nums5 = [1, 2, 3, 4, 5]
    diff5 = -1
    expected5 = 1
    assert longest_increasing_subsequence_with_diff(nums5, diff5) == expected5, f"Test Case 5 Failed: Expected {expected5}, got {longest_increasing_subsequence_with_diff(nums5, diff5)}"

    # Test case 6: All same numbers
    nums6 = [5, 5, 5, 5, 5]
    diff6 = 0
    expected6 = 1
    assert longest_increasing_subsequence_with_diff(nums6, diff6) == 5, f"Test Case 6 Failed: Expected {5}, got {longest_increasing_subsequence_with_diff(nums6, diff6)}"
    
    nums6 = [5, 5, 5, 5, 5]
    diff6 = 1
    expected6 = 1
    assert longest_increasing_subsequence_with_diff(nums6, diff6) == expected6, f"Test Case 6 Failed: Expected {expected6}, got {longest_increasing_subsequence_with_diff(nums6, diff6)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_increasing_subsequence_with_diff()