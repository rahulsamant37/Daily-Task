# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence (LIS) where the difference between consecutive elements in the subsequence is exactly `diff`.

Example:
Input: nums = [3, 0, 3, 2, 4], diff = 1
Output: 3
Explanation: The longest increasing subsequence with a difference of 1 is [2, 3, 4], which has a length of 3.  Another valid subsequence is [0, 1, 2] if 1 was in the input array.

Input: nums = [1, 5, 7, 8, 5, 3, 4, 2, 1], diff = -2
Output: 4
Explanation: The longest increasing subsequence with a difference of -2 is [7, 5, 3, 1], which has a length of 4.
'''

# Solution
def solution():
    def longest_increasing_subsequence_with_diff(nums, diff):
        """
        Finds the length of the longest increasing subsequence (LIS) where the difference between
        consecutive elements in the subsequence is exactly `diff`.

        Args:
            nums: A list of integers.
            diff: The required difference between consecutive elements.

        Returns:
            The length of the LIS with the specified difference.
        """

        # Use a dictionary to store the length of the longest increasing subsequence ending at each number.
        # key: number, value: length of LIS ending at that number.
        dp = {}

        max_len = 0  # Keep track of the maximum length found so far

        for num in nums:
            # If the previous number in the sequence (num - diff) is in dp,
            # then the current LIS length is the LIS length ending at num - diff + 1.
            if num - diff in dp:
                dp[num] = dp[num - diff] + 1
            else:
                # If num - diff is not in dp, the LIS length ending at num is 1.
                dp[num] = 1

            # Update the maximum length found so far.
            max_len = max(max_len, dp[num])

        return max_len
    
    return longest_increasing_subsequence_with_diff

# Test cases
def test_solution():
    lis_with_diff = solution()

    # Test case 1
    nums1 = [3, 0, 3, 2, 4]
    diff1 = 1
    expected1 = 3
    assert lis_with_diff(nums1, diff1) == expected1, f"Test Case 1 Failed: Expected {expected1}, got {lis_with_diff(nums1, diff1)}"

    # Test case 2
    nums2 = [1, 5, 7, 8, 5, 3, 4, 2, 1]
    diff2 = -2
    expected2 = 4
    assert lis_with_diff(nums2, diff2) == expected2, f"Test Case 2 Failed: Expected {expected2}, got {lis_with_diff(nums2, diff2)}"

    # Test case 3
    nums3 = [1, 2, 3, 4, 5]
    diff3 = 1
    expected3 = 5
    assert lis_with_diff(nums3, diff3) == expected3, f"Test Case 3 Failed: Expected {expected3}, got {lis_with_diff(nums3, diff3)}"

    # Test case 4
    nums4 = [5, 4, 3, 2, 1]
    diff4 = -1
    expected4 = 5
    assert lis_with_diff(nums4, diff4) == expected4, f"Test Case 4 Failed: Expected {expected4}, got {lis_with_diff(nums4, diff4)}"

    # Test case 5
    nums5 = [1, 3, 5, 7, 9]
    diff5 = 2
    expected5 = 5
    assert lis_with_diff(nums5, diff5) == expected5, f"Test Case 5 Failed: Expected {expected5}, got {lis_with_diff(nums5, diff5)}"

    # Test case 6
    nums6 = [1, 5, 7, 8, 5, 3, 4, 2, 1]
    diff6 = 0
    expected6 = 2

    # Test case 7 - Empty list
    nums7 = []
    diff7 = 1
    expected7 = 0
    assert lis_with_diff(nums7, diff7) == expected7, f"Test Case 7 Failed: Expected {expected7}, got {lis_with_diff(nums7, diff7)}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()