# Python Question: Longest Increasing Subsequence with Limited Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence (LIS) where the difference between consecutive elements in the subsequence is at most `diff`.

Example:
Input: nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], diff = 2
Output: 4
Explanation: One possible LIS with difference at most 2 is [1, 1, 2, 3].  Another is [3, 4, 5, 6]. The length of these subsequences is 4.
'''

# Solution
def solution():
    def longest_increasing_subsequence_with_diff(nums, diff):
        """
        Finds the length of the longest increasing subsequence (LIS) in `nums` where the difference
        between consecutive elements in the subsequence is at most `diff`.

        Args:
            nums: A list of integers.
            diff: The maximum allowed difference between consecutive elements in the LIS.

        Returns:
            The length of the longest increasing subsequence with the given difference constraint.
        """

        n = len(nums)
        if n == 0:
            return 0

        # dp[i] stores the length of the longest increasing subsequence ending at nums[i]
        dp = [1] * n

        # Iterate through the array to build the LIS lengths
        for i in range(1, n):
            # For each element nums[i], check all previous elements nums[j]
            for j in range(i):
                # If nums[i] is greater than nums[j] and the difference is within the limit
                if nums[i] > nums[j] and nums[i] - nums[j] <= diff:
                    # Update dp[i] if including nums[i] in the subsequence gives a longer LIS
                    dp[i] = max(dp[i], dp[j] + 1)

        # The maximum value in dp is the length of the longest increasing subsequence
        return max(dp)

    return longest_increasing_subsequence_with_diff
    

# Test cases
def test_solution():
    lis_with_diff = solution()

    # Test case 1
    nums1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    diff1 = 2
    expected1 = 4
    assert lis_with_diff(nums1, diff1) == expected1, f"Test Case 1 Failed: Expected {expected1}, got {lis_with_diff(nums1, diff1)}"

    # Test case 2
    nums2 = [1, 2, 3, 4, 5]
    diff2 = 1
    expected2 = 5
    assert lis_with_diff(nums2, diff2) == expected2, f"Test Case 2 Failed: Expected {expected2}, got {lis_with_diff(nums2, diff2)}"

    # Test case 3
    nums3 = [5, 4, 3, 2, 1]
    diff3 = 1
    expected3 = 1
    assert lis_with_diff(nums3, diff3) == expected3, f"Test Case 3 Failed: Expected {expected3}, got {lis_with_diff(nums3, diff3)}"

    # Test case 4
    nums4 = [1, 5, 2, 4, 3]
    diff4 = 2
    expected4 = 3
    assert lis_with_diff(nums4, diff4) == expected4, f"Test Case 4 Failed: Expected {expected4}, got {lis_with_diff(nums4, diff4)}"

    # Test case 5
    nums5 = []
    diff5 = 2
    expected5 = 0
    assert lis_with_diff(nums5, diff5) == expected5, f"Test Case 5 Failed: Expected {expected5}, got {lis_with_diff(nums5, diff5)}"

    # Test case 6
    nums6 = [1, 1, 1, 1, 1]
    diff6 = 0
    expected6 = 1
    assert lis_with_diff(nums6, diff6) == expected6, f"Test Case 6 Failed: Expected {expected6}, got {lis_with_diff(nums6, diff6)}"

    # Test case 7
    nums7 = [1, 3, 2, 4, 5]
    diff7 = 1
    expected7 = 3
    assert lis_with_diff(nums7, diff7) == expected7, f"Test Case 7 Failed: Expected {expected7}, got {lis_with_diff(nums7, diff7)}"
    
    # Test case 8: Large numbers
    nums8 = [100, 102, 101, 103, 105, 104]
    diff8 = 2
    expected8 = 5
    assert lis_with_diff(nums8, diff8) == expected8, f"Test Case 8 Failed: Expected {expected8}, got {lis_with_diff(nums8, diff8)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()