# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence such that the difference between consecutive elements in the subsequence is exactly `diff`.

Example:
Input: nums = [3, 0, 3, 4, 5], diff = 3
Output: 3
Explanation: The longest increasing subsequence with a difference of 3 is [0, 3, 6]. In this case, it is [0, 3]. Then [3, 6] doesn't exist. The next longest is [3, 3+3=6], which doesn't exist. The next longest is [0, 3].
However, [3, 0, 3, 4, 5] => [0,3] => [3,4] is not increasing. We need to find an increasing subsequence.

Input: nums = [1, 2, 3, 4, 5], diff = 1
Output: 5
Explanation: The longest increasing subsequence with a difference of 1 is [1, 2, 3, 4, 5].

Input: nums = [1, 5, 7, 8, 5, 3, 4, 2, 1], diff = -2
Output: 4
Explanation: The longest increasing subsequence with a difference of -2 is [7, 5, 3, 1].

Input: nums = [4,12,10,0,3,10,15,16,17,8,9,2,11,12,11,2,7,15,19,20], diff = 5
Output: 5
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
            The length of the longest increasing subsequence.
        """

        # Create a dictionary to store the length of the longest increasing subsequence
        # ending at each number.  We use a dictionary instead of an array because the
        # numbers in `nums` might not be contiguous, and an array would waste space.
        dp = {}

        max_len = 0  # Initialize the maximum length of the subsequence

        # Iterate through the numbers in the input array
        for num in nums:
            # If the number minus the difference is already in the dictionary, it means
            # we can extend an existing subsequence.
            if num - diff in dp:
                dp[num] = dp[num - diff] + 1
            else:
                # Otherwise, start a new subsequence of length 1.
                dp[num] = 1

            # Update the maximum length of the subsequence
            max_len = max(max_len, dp[num])

        return max_len

    return longest_increasing_subsequence_with_diff
    # Test cases
def test_solution():
    longest_increasing_subsequence_with_diff = solution()
    # Test case 1
    nums1 = [3, 0, 3, 4, 5]
    diff1 = 3
    expected1 = 2
    assert longest_increasing_subsequence_with_diff(nums1, diff1) == expected1, f"Test Case 1 Failed: Expected {expected1}, Got {longest_increasing_subsequence_with_diff(nums1, diff1)}"

    # Test case 2
    nums2 = [1, 2, 3, 4, 5]
    diff2 = 1
    expected2 = 5
    assert longest_increasing_subsequence_with_diff(nums2, diff2) == expected2, f"Test Case 2 Failed: Expected {expected2}, Got {longest_increasing_subsequence_with_diff(nums2, diff2)}"

    # Test case 3
    nums3 = [1, 5, 7, 8, 5, 3, 4, 2, 1]
    diff3 = -2
    expected3 = 4
    assert longest_increasing_subsequence_with_diff(nums3, diff3) == expected3, f"Test Case 3 Failed: Expected {expected3}, Got {longest_increasing_subsequence_with_diff(nums3, diff3)}"

    # Test case 4
    nums4 = [4,12,10,0,3,10,15,16,17,8,9,2,11,12,11,2,7,15,19,20]
    diff4 = 5
    expected4 = 5
    assert longest_increasing_subsequence_with_diff(nums4, diff4) == expected4, f"Test Case 4 Failed: Expected {expected4}, Got {longest_increasing_subsequence_with_diff(nums4, diff4)}"

    # Test case 5: Empty array
    nums5 = []
    diff5 = 2
    expected5 = 0
    assert longest_increasing_subsequence_with_diff(nums5, diff5) == expected5, f"Test Case 5 Failed: Expected {expected5}, Got {longest_increasing_subsequence_with_diff(nums5, diff5)}"

    # Test case 6: Array with no increasing subsequence with given difference
    nums6 = [1, 2, 3, 4, 5]
    diff6 = 10
    expected6 = 1
    assert longest_increasing_subsequence_with_diff(nums6, diff6) == expected6, f"Test Case 6 Failed: Expected {expected6}, Got {longest_increasing_subsequence_with_diff(nums6, diff6)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()