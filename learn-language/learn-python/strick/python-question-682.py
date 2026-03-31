# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence where the difference between consecutive elements is exactly `diff`.

Example:
Input: nums = [3, 0, 3, 2, 4, 5], diff = 1
Output: 3
Explanation: The longest increasing subsequence with a difference of 1 is [2, 3, 4] or [3, 4, 5], both having a length of 3.

Input: nums = [1, 5, 7, 8, 5, 3, 4, 2, 1], diff = -2
Output: 4
Explanation: The longest increasing subsequence with a difference of -2 is [7, 5, 3, 1], having a length of 4.
'''

# Solution
def solution():
    def longest_increasing_subsequence_with_diff(nums, diff):
        """
        Finds the length of the longest increasing subsequence with a specific difference.

        Args:
            nums: A list of integers.
            diff: The required difference between consecutive elements in the subsequence.

        Returns:
            The length of the longest increasing subsequence with the given difference.
        """

        # Use a dictionary to store the length of the longest subsequence ending at each number.
        # Key: number, Value: length of the longest subsequence ending at that number.
        dp = {}

        max_length = 0  # Initialize the maximum length found so far.

        for num in nums:
            # If the previous number in the sequence (num - diff) exists in the dp dictionary,
            # then we can extend the subsequence ending at (num - diff) by 1.
            if num - diff in dp:
                dp[num] = dp[num - diff] + 1
            else:
                # If the previous number doesn't exist, then the subsequence starting at the current number has length 1.
                dp[num] = 1

            # Update the maximum length found so far.
            max_length = max(max_length, dp[num])

        return max_length

    return longest_increasing_subsequence_with_diff
    

# Test cases
def test_solution():
    longest_increasing_subsequence_with_diff = solution()

    # Test case 1
    nums1 = [3, 0, 3, 2, 4, 5]
    diff1 = 1
    expected1 = 3
    actual1 = longest_increasing_subsequence_with_diff(nums1, diff1)
    assert actual1 == expected1, f"Test Case 1 Failed: Expected {expected1}, got {actual1}"
    print("Test Case 1 Passed")

    # Test case 2
    nums2 = [1, 5, 7, 8, 5, 3, 4, 2, 1]
    diff2 = -2
    expected2 = 4
    actual2 = longest_increasing_subsequence_with_diff(nums2, diff2)
    assert actual2 == expected2, f"Test Case 2 Failed: Expected {expected2}, got {actual2}"
    print("Test Case 2 Passed")

    # Test case 3
    nums3 = [1, 2, 3, 4, 5]
    diff3 = 1
    expected3 = 5
    actual3 = longest_increasing_subsequence_with_diff(nums3, diff3)
    assert actual3 == expected3, f"Test Case 3 Failed: Expected {expected3}, got {actual3}"
    print("Test Case 3 Passed")

    # Test case 4
    nums4 = [5, 4, 3, 2, 1]
    diff4 = -1
    expected4 = 5
    actual4 = longest_increasing_subsequence_with_diff(nums4, diff4)
    assert actual4 == expected4, f"Test Case 4 Failed: Expected {expected4}, got {actual4}"
    print("Test Case 4 Passed")

    # Test case 5: Empty array
    nums5 = []
    diff5 = 1
    expected5 = 0
    actual5 = longest_increasing_subsequence_with_diff(nums5, diff5)
    assert actual5 == expected5, f"Test Case 5 Failed: Expected {expected5}, got {actual5}"
    print("Test Case 5 Passed")

    # Test case 6: No valid subsequence
    nums6 = [1, 2, 3, 4, 5]
    diff6 = -1
    expected6 = 1
    actual6 = longest_increasing_subsequence_with_diff(nums6, diff6)
    assert actual6 == expected6, f"Test Case 6 Failed: Expected {expected6}, got {actual6}"
    print("Test Case 6 Passed")

    # Test case 7: Repeating numbers
    nums7 = [1, 3, 1, 5, 3, 7]
    diff7 = 2
    expected7 = 3
    actual7 = longest_increasing_subsequence_with_diff(nums7, diff7)
    assert actual7 == expected7, f"Test Case 7 Failed: Expected {expected7}, got {actual7}"
    print("Test Case 7 Passed")

if __name__ == "__main__":
    test_solution()