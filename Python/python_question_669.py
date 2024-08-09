# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) where the difference between consecutive elements in the subsequence is exactly `k`.

Example:
Input: nums = [3, 10, 3, 4, 5], k = 1
Output: 3
Explanation: The longest increasing subsequence with a difference of 1 is [3, 4, 5], which has a length of 3.

Input: nums = [1, 5, 7, 8, 5, 3, 4, 2, 1], k = -2
Output: 4
Explanation: The longest increasing subsequence with a difference of -2 is [7, 5, 3, 1], which has a length of 4.
'''

# Solution
def solution():
    def longest_increasing_subsequence_with_difference(nums, k):
        """
        Finds the length of the longest increasing subsequence (LIS) where the difference between consecutive elements in the subsequence is exactly k.

        Args:
            nums: A list of integers.
            k: The required difference between consecutive elements in the subsequence.

        Returns:
            The length of the LIS with the specified difference.
        """
        n = len(nums)
        # dp[i] stores the length of the LIS ending at nums[i]
        dp = {}  # Use a dictionary to store the lengths for each number encountered

        for num in nums:
            # If the previous number in the sequence (num - k) is present in the dp,
            # then we can extend that sequence by 1.
            if num - k in dp:
                dp[num] = dp[num - k] + 1
            else:
                # Otherwise, start a new sequence of length 1.
                dp[num] = 1

        # The maximum value in the dp represents the length of the longest sequence.
        return max(dp.values()) if dp else 0

    return longest_increasing_subsequence_with_difference
    
# Test cases
def test_solution():
    lis_with_diff = solution()
    
    # Test case 1
    nums1 = [3, 10, 3, 4, 5]
    k1 = 1
    expected1 = 3
    assert lis_with_diff(nums1, k1) == expected1, f"Test Case 1 Failed: Expected {expected1}, Got {lis_with_diff(nums1, k1)}"
    
    # Test case 2
    nums2 = [1, 5, 7, 8, 5, 3, 4, 2, 1]
    k2 = -2
    expected2 = 4
    assert lis_with_diff(nums2, k2) == expected2, f"Test Case 2 Failed: Expected {expected2}, Got {lis_with_diff(nums2, k2)}"
    
    # Test case 3
    nums3 = [1, 2, 3, 4, 5]
    k3 = 0
    expected3 = 1
    assert lis_with_diff(nums3, k3) == expected3, f"Test Case 3 Failed: Expected {expected3}, Got {lis_with_diff(nums3, k3)}"
    
    # Test case 4
    nums4 = [1, 2, 3, 4, 5]
    k4 = 1
    expected4 = 5
    assert lis_with_diff(nums4, k4) == expected4, f"Test Case 4 Failed: Expected {expected4}, Got {lis_with_diff(nums4, k4)}"

    # Test case 5
    nums5 = [5, 4, 3, 2, 1]
    k5 = -1
    expected5 = 5
    assert lis_with_diff(nums5, k5) == expected5, f"Test Case 5 Failed: Expected {expected5}, Got {lis_with_diff(nums5, k5)}"

    # Test case 6 (empty array)
    nums6 = []
    k6 = 2
    expected6 = 0
    assert lis_with_diff(nums6, k6) == expected6, f"Test Case 6 Failed: Expected {expected6}, Got {lis_with_diff(nums6, k6)}"

    # Test case 7 (single element)
    nums7 = [5]
    k7 = 2
    expected7 = 1
    assert lis_with_diff(nums7, k7) == expected7, f"Test Case 7 Failed: Expected {expected7}, Got {lis_with_diff(nums7, k7)}"

    # Test case 8 (all same elements)
    nums8 = [2, 2, 2, 2, 2]
    k8 = 0
    expected8 = 1
    assert lis_with_diff(nums8, k8) == expected8, f"Test Case 8 Failed: Expected {expected8}, Got {lis_with_diff(nums8, k8)}"

    # Test case 9
    nums9 = [1, 2, 4, 6, 8, 10]
    k9 = 2
    expected9 = 6
    assert lis_with_diff(nums9, k9) == expected9, f"Test Case 9 Failed: Expected {expected9}, Got {lis_with_diff(nums9, k9)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()