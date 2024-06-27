# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) such that the difference between any two consecutive elements in the subsequence is at most `k`.

Example:
Input: nums = [3, 10, 2, 1, 20], k = 5
Output: 3
Explanation: The longest increasing subsequence with a maximum difference of 5 is [3, 2, 1] or [1,2,3] with length 3. Another valid subsequence is [3, 2, 1].  Note, the subsequence must be increasing.

Input: nums = [1, 3, 5, 2, 4], k = 2
Output: 3
Explanation: The longest increasing subsequence with a maximum difference of 2 is [1, 2, 4] with length 3.

Input: nums = [1, 5, 9, 13], k = 3
Output: 1
Explanation: No increasing subsequence with a difference <= k can be formed with more than 1 element.
'''

# Solution
def solution():
    def longest_increasing_subsequence_with_difference(nums, k):
        """
        Finds the length of the longest increasing subsequence of nums such that the
        difference between consecutive elements is at most k.

        Args:
            nums: A list of integers.
            k: The maximum allowed difference between consecutive elements.

        Returns:
            The length of the longest increasing subsequence with the given constraint.
        """
        n = len(nums)
        if n == 0:
            return 0

        # dp[i] stores the length of the longest increasing subsequence ending at nums[i].
        dp = [1] * n

        # Iterate through the array to build the dp array.
        for i in range(1, n):
            for j in range(i):
                # Check if nums[i] can be added to the subsequence ending at nums[j].
                if nums[i] > nums[j] and nums[i] - nums[j] <= k:
                    dp[i] = max(dp[i], dp[j] + 1)

        # The maximum value in dp is the length of the longest increasing subsequence.
        return max(dp)

    return longest_increasing_subsequence_with_difference

# Test cases
def test_solution():
    func = solution()

    # Test case 1
    nums1 = [3, 10, 2, 1, 20]
    k1 = 5
    expected1 = 3
    assert func(nums1, k1) == expected1, f"Test Case 1 Failed: Expected {expected1}, got {func(nums1, k1)}"

    # Test case 2
    nums2 = [1, 3, 5, 2, 4]
    k2 = 2
    expected2 = 3
    assert func(nums2, k2) == expected2, f"Test Case 2 Failed: Expected {expected2}, got {func(nums2, k2)}"

    # Test case 3
    nums3 = [1, 5, 9, 13]
    k3 = 3
    expected3 = 1
    assert func(nums3, k3) == expected3, f"Test Case 3 Failed: Expected {expected3}, got {func(nums3, k3)}"

    # Test case 4: Empty array
    nums4 = []
    k4 = 5
    expected4 = 0
    assert func(nums4, k4) == expected4, f"Test Case 4 Failed: Expected {expected4}, got {func(nums4, k4)}"

    # Test case 5: Array with one element
    nums5 = [5]
    k5 = 5
    expected5 = 1
    assert func(nums5, k5) == expected5, f"Test Case 5 Failed: Expected {expected5}, got {func(nums5, k5)}"

    # Test case 6: All same numbers
    nums6 = [2, 2, 2, 2]
    k6 = 0
    expected6 = 1
    assert func(nums6, k6) == expected6, f"Test Case 6 Failed: Expected {expected6}, got {func(nums6, k6)}"

    # Test case 7: k is very large
    nums7 = [1, 3, 5, 7]
    k7 = 100
    expected7 = 4
    assert func(nums7, k7) == 4, f"Test Case 7 Failed: Expected {expected7}, got {func(nums7, k7)}"

    # Test case 8
    nums8 = [5, 4, 3, 2, 1]
    k8 = 1
    expected8 = 1
    assert func(nums8, k8) == expected8, f"Test Case 8 Failed: Expected {expected8}, got {func(nums8, k8)}"
    
    nums9 = [1, 2, 3, 4, 5]
    k9 = 1
    expected9 = 2
    assert func(nums9, k9)([1, 2, 3, 4, 5], 1) == 2, f"Test Case 9 Failed: Expected {expected9}, got {func(nums9, k9)([1, 2, 3, 4, 5], 1)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()