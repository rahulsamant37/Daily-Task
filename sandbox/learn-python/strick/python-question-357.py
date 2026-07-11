# Python Question:  Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence (LIS) where the difference between consecutive elements in the subsequence is exactly `diff`.

Example:
Input: nums = [3, 0, 3, 4, 5, 6], diff = 1
Output: 4
Explanation: The longest increasing subsequence with a difference of 1 is [3, 4, 5, 6], which has a length of 4.

Input: nums = [1, 5, 7, 8, 5, 3, 4, 2, 1], diff = 2
Output: 3
Explanation: The longest increasing subsequence with a difference of 2 is [1, 3, 5] or [5, 7, 9] where 9 is not present and so the subsequence [5,7] can be followed by subsequence [2,4] with difference 2. The longest is of length 3, e.g., [1, 3, 5]
'''

# Solution
def longest_increasing_subsequence_with_diff(nums, diff):
    """
    Finds the length of the longest increasing subsequence with a specific difference.

    Args:
        nums: A list of integers.
        diff: The difference between consecutive elements in the subsequence.

    Returns:
        The length of the longest increasing subsequence with the specified difference.
    """

    # Use a dictionary to store the length of the longest increasing subsequence ending at each number.
    dp = {}  # key: number, value: length of LIS ending at that number

    # Iterate through the numbers in the input array.
    for num in nums:
        # If the number minus the difference is in the dictionary,
        # it means we can extend an existing subsequence.
        if num - diff in dp:
            dp[num] = dp[num - diff] + 1
        # Otherwise, this number starts a new subsequence of length 1.
        else:
            dp[num] = 1

    # Return the maximum value in the dictionary, which represents the length of the longest subsequence.
    return max(dp.values()) if dp else 0

# Test cases
def test_longest_increasing_subsequence_with_diff():
    """
    Tests the longest_increasing_subsequence_with_diff function with several test cases.
    """

    # Test case 1
    nums1 = [3, 0, 3, 4, 5, 6]
    diff1 = 1
    expected1 = 4
    assert longest_increasing_subsequence_with_diff(nums1, diff1) == expected1, f"Test Case 1 Failed: Expected {expected1}, Got {longest_increasing_subsequence_with_diff(nums1, diff1)}"

    # Test case 2
    nums2 = [1, 5, 7, 8, 5, 3, 4, 2, 1]
    diff2 = 2
    expected2 = 3
    assert longest_increasing_subsequence_with_diff(nums2, diff2) == expected2, f"Test Case 2 Failed: Expected {expected2}, Got {longest_increasing_subsequence_with_diff(nums2, diff2)}"

    # Test case 3
    nums3 = [1, 2, 3, 4, 5]
    diff3 = 1
    expected3 = 5
    assert longest_increasing_subsequence_with_diff(nums3, diff3) == expected3, f"Test Case 3 Failed: Expected {expected3}, Got {longest_increasing_subsequence_with_diff(nums3, diff3)}"

    # Test case 4
    nums4 = [5, 4, 3, 2, 1]
    diff4 = 1
    expected4 = 1
    assert longest_increasing_subsequence_with_diff(nums4, diff4) == expected4, f"Test Case 4 Failed: Expected {expected4}, Got {longest_increasing_subsequence_with_diff(nums4, diff4)}"

    # Test case 5
    nums5 = [1, 1, 1, 1, 1]
    diff5 = 0
    expected5 = 5
    assert longest_increasing_subsequence_with_diff(nums5, diff5) == expected5, f"Test Case 5 Failed: Expected {expected5}, Got {longest_increasing_subsequence_with_diff(nums5, diff5)}"

    # Test case 6
    nums6 = []
    diff6 = 1
    expected6 = 0
    assert longest_increasing_subsequence_with_diff(nums6, diff6) == expected6, f"Test Case 6 Failed: Expected {expected6}, Got {longest_increasing_subsequence_with_diff(nums6, diff6)}"

    # Test case 7
    nums7 = [4,12,10,0,7,9,2,11,1,6,3,13]
    diff7 = 3
    expected7 = 4
    assert longest_increasing_subsequence_with_diff(nums7, diff7) == 4, f"Test Case 7 Failed: Expected {4}, Got {longest_increasing_subsequence_with_diff(nums7, diff7)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_increasing_subsequence_with_diff()