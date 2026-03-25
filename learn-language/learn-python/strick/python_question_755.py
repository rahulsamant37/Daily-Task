# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence where the difference between consecutive elements in the subsequence is exactly `diff`.

Example:
Input: nums = [3, 0, 3, 2, 4, 5], diff = 1
Output: 4
Explanation: The longest increasing subsequence with a difference of 1 is [2, 3, 4, 5] or [3, 4, 5], which has length 4.

Input: nums = [1, 5, 7, 8, 5, 3, 4, 2, 1], diff = -2
Output: 4
Explanation: The longest increasing subsequence with a difference of -2 is [7, 5, 3, 1], which has length 4.
'''

# Solution
def solution():
    def longest_increasing_subsequence(nums, diff):
        """
        Finds the length of the longest increasing subsequence with a specific difference.

        Args:
            nums: A list of integers.
            diff: The required difference between consecutive elements in the subsequence.

        Returns:
            The length of the longest increasing subsequence.
        """

        # Use a dictionary to store the length of the longest increasing subsequence ending at each number.
        # The key is the number and the value is the length of the LIS ending at that number.
        dp = {}

        # Iterate through the numbers in the input array.
        for num in nums:
            # If the number minus the difference is already in the dictionary,
            # then we can extend the longest increasing subsequence ending at that number.
            if num - diff in dp:
                dp[num] = dp[num - diff] + 1
            # Otherwise, the longest increasing subsequence ending at this number is just 1 (the number itself).
            else:
                dp[num] = 1

        # The length of the longest increasing subsequence is the maximum value in the dictionary.
        if not dp:
            return 0
        return max(dp.values())

    return longest_increasing_subsequence


# Test cases
def test_solution():
    longest_increasing_subsequence = solution()

    # Test case 1
    nums1 = [3, 0, 3, 2, 4, 5]
    diff1 = 1
    expected1 = 4
    assert longest_increasing_subsequence(nums1, diff1) == expected1, f"Test Case 1 Failed: Expected {expected1}, got {longest_increasing_subsequence(nums1, diff1)}"

    # Test case 2
    nums2 = [1, 5, 7, 8, 5, 3, 4, 2, 1]
    diff2 = -2
    expected2 = 4
    assert longest_increasing_subsequence(nums2, diff2) == expected2, f"Test Case 2 Failed: Expected {expected2}, got {longest_increasing_subsequence(nums2, diff2)}"

    # Test case 3
    nums3 = [1, 2, 3, 4, 5]
    diff3 = 1
    expected3 = 5
    assert longest_increasing_subsequence(nums3, diff3) == expected3, f"Test Case 3 Failed: Expected {expected3}, got {longest_increasing_subsequence(nums3, diff3)}"

    # Test case 4
    nums4 = [5, 4, 3, 2, 1]
    diff4 = -1
    expected4 = 5
    assert longest_increasing_subsequence(nums4, diff4) == expected4, f"Test Case 4 Failed: Expected {expected4}, got {longest_increasing_subsequence(nums4, diff4)}"

    # Test case 5
    nums5 = [1, 2, 3, 4, 5]
    diff5 = 0
    expected5 = 1
    assert longest_increasing_subsequence(nums5, diff5) == 1, f"Test Case 5 Failed: Expected {expected5}, got {longest_increasing_subsequence(nums5, diff5)}"

    # Test case 6: Empty array
    nums6 = []
    diff6 = 1
    expected6 = 0
    assert longest_increasing_subsequence(nums6, diff6) == expected6, f"Test Case 6 Failed: Expected {expected6}, got {longest_increasing_subsequence(nums6, diff6)}"

    # Test case 7: Array with only one element
    nums7 = [5]
    diff7 = 2
    expected7 = 1
    assert longest_increasing_subsequence(nums7, diff7) == expected7, f"Test Case 7 Failed: Expected {expected7}, got {longest_increasing_subsequence(nums7, diff7)}"
    
    # Test case 8: Array with repeating elements
    nums8 = [1, 1, 1, 2, 2, 3]
    diff8 = 1
    expected8 = 3
    assert longest_increasing_subsequence(nums8, diff8) == expected8, f"Test Case 8 Failed: Expected {expected8}, got {longest_increasing_subsequence(nums8, diff8)}"


    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()