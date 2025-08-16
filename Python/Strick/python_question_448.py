# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) with the following twist:

You are allowed to change at most `k` elements in the array to any other integer.  The goal is to maximize the length of the longest increasing subsequence after making at most `k` changes.

Example:
Input: nums = [4, 2, 3, 4, 5], k = 1
Output: 5
Explanation: We can change 2 to 1 (or any number smaller than 3), and the array becomes [4, 1, 3, 4, 5], which has a LIS of length 5 ([1, 3, 4, 5]).

Input: nums = [1, 5, 2, 3, 4], k = 2
Output: 5
Explanation: We can change 5 to 2 and 1 to 1, making the array [1, 2, 2, 3, 4], which has a LIS of length 5 ([1, 2, 3, 4]). Alternatively, we can change 1 to 2 and 5 to 1, making the array [2, 1, 2, 3, 4], which has a LIS of length 4 ([1, 2, 3, 4]).

Input: nums = [1, 2, 3, 4, 5], k = 0
Output: 5
Explanation: The array is already an increasing sequence.

Input: nums = [5, 4, 3, 2, 1], k = 2
Output: 3
Explanation: We can change 5 to 1 and 4 to 2, making the array [1, 2, 3, 2, 1], which has a LIS of length 3 ([1, 2, 3]).
'''

# Solution
def solution():
    def longest_increasing_subsequence_with_k_changes(nums, k):
        """
        Finds the length of the longest increasing subsequence (LIS) with at most k changes.

        Args:
            nums: A list of integers.
            k: The maximum number of changes allowed.

        Returns:
            The length of the LIS with at most k changes.
        """
        n = len(nums)
        dp = [[0] * (k + 1) for _ in range(n)]

        for i in range(n):
            for j in range(k + 1):
                dp[i][j] = 1  # Initialize with 1 (single element is an increasing subsequence)
                for l in range(i):
                    if nums[i] >= nums[l]:
                        dp[i][j] = max(dp[i][j], dp[l][j] + 1)
                    elif j > 0:  # If we can make a change
                        dp[i][j] = max(dp[i][j], dp[l][j - 1] + 1)

        max_len = 0
        for i in range(n):
            max_len = max(max_len, dp[i][k])
        return max_len
    
    return longest_increasing_subsequence_with_k_changes

# Test cases
def test_solution():
    func = solution()

    # Test case 1
    nums1 = [4, 2, 3, 4, 5]
    k1 = 1
    expected1 = 5
    assert func(nums1, k1) == expected1, f"Test Case 1 Failed: Expected {expected1}, Got {func(nums1, k1)}"

    # Test case 2
    nums2 = [1, 5, 2, 3, 4]
    k2 = 2
    expected2 = 5
    assert func(nums2, k2) == expected2, f"Test Case 2 Failed: Expected {expected2}, Got {func(nums2, k2)}"

    # Test case 3
    nums3 = [1, 2, 3, 4, 5]
    k3 = 0
    expected3 = 5
    assert func(nums3, k3) == expected3, f"Test Case 3 Failed: Expected {expected3}, Got {func(nums3, k3)}"

    # Test case 4
    nums4 = [5, 4, 3, 2, 1]
    k4 = 2
    expected4 = 3
    assert func(nums4, k4) == expected4, f"Test Case 4 Failed: Expected {expected4}, Got {func(nums4, k4)}"

    # Test case 5
    nums5 = [5, 4, 3, 2, 1]
    k5 = 0
    expected5 = 1
    assert func(nums5, k5) == expected5, f"Test Case 5 Failed: Expected {expected5}, Got {func(nums5, k5)}"
    
    # Test case 6: All same numbers, k = 0, 1, 2
    nums6 = [1, 1, 1, 1, 1]
    k6_0 = 0
    expected6_0 = 1
    assert func(nums6, k6_0) == expected6_0, f"Test Case 6 (k=0) Failed: Expected {expected6_0}, Got {func(nums6, k6_0)}"
    
    k6_1 = 1
    expected6_1 = 2
    assert func(nums6, k6_1) == expected6_1, f"Test Case 6 (k=1) Failed: Expected {expected6_1}, Got {func(nums6, k6_1)}"

    k6_2 = 2
    expected6_2 = 3
    assert func(nums6, k6_2) == expected6_2, f"Test Case 6 (k=2) Failed: Expected {expected6_2}, Got {func(nums6, k6_2)}"

    # Test case 7: Empty list
    nums7 = []
    k7 = 0
    expected7 = 0
    assert func(nums7, k7) == expected7, f"Test Case 7 Failed: Expected {expected7}, Got {func(nums7, k7)}"

    # Test case 8
    nums8 = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    k8 = 1
    expected8 = 7 # [10, 22, 33, 41, 50, 60, 80] - Change 9 to something between 22 and 33

    assert func(nums8, k8) == expected8, f"Test Case 8 Failed: Expected {expected8}, Got {func(nums8, k8)}"

    # Test case 9
    nums9 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    k9 = 5
    expected9 = 6
    assert func(nums9, k9) == expected9, f"Test Case 9 Failed: Expected {expected9}, Got {func(nums9, k9)}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()