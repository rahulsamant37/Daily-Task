# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) such that the difference between consecutive elements in the subsequence is at most `k`.

Example:
Input: nums = [3, 10, 2, 1, 20], k = 5
Output: 3
Explanation: The longest increasing subsequence satisfying the condition is [3, 2, 1] or [1, 2, 3] or [1, 2, 10].  The order doesn't matter as long as the elements are increasing and the difference between consecutive elements is at most k. The length is 3. Another possible subsequence is [3, 10, 20], with difference 7 and 10 respectively, so it does not qualify.
'''

# Solution
def solution():
    def longest_increasing_subsequence_with_k_difference(nums, k):
        """
        Finds the length of the longest increasing subsequence in nums with a maximum difference of k between consecutive elements.

        Args:
            nums: A list of integers.
            k: The maximum difference allowed between consecutive elements in the subsequence.

        Returns:
            The length of the longest increasing subsequence.
        """
        n = len(nums)
        if n == 0:
            return 0

        # dp[i] stores the length of the longest increasing subsequence ending at nums[i]
        dp = [1] * n

        # Iterate through the array to build the dp table
        for i in range(1, n):
            for j in range(i):
                # Check if nums[i] is greater than nums[j] and the difference is at most k
                if nums[i] > nums[j] and nums[i] - nums[j] <= k:
                    # Update dp[i] if including nums[i] in the subsequence ending at nums[j] results in a longer subsequence
                    dp[i] = max(dp[i], dp[j] + 1)

        # The maximum value in the dp table is the length of the longest increasing subsequence
        return max(dp)

    return longest_increasing_subsequence_with_k_difference

# Test cases
def test_solution():
    func = solution()

    # Test case 1
    nums1 = [3, 10, 2, 1, 20]
    k1 = 5
    expected1 = 3
    assert func(nums1, k1) == expected1, f"Test Case 1 Failed: Expected {expected1}, Got {func(nums1, k1)}"

    # Test case 2
    nums2 = [1, 2, 3, 4, 5]
    k2 = 1
    expected2 = 2  # Only consecutive elements can be part of the increasing subsequence
    assert func(nums2, k2) == 2, f"Test Case 2 Failed: Expected {expected2}, Got {func(nums2, k2)}"

    # Test case 3
    nums3 = [5, 4, 3, 2, 1]
    k3 = 1
    expected3 = 1 # Only one element can be picked
    assert func(nums3, k3) == 1, f"Test Case 3 Failed: Expected {expected3}, Got {func(nums3, k3)}"

    # Test case 4
    nums4 = [1, 5, 2, 4, 3]
    k4 = 2
    expected4 = 3 # e.g., [1,2,3], [1,2,4], [1,3,4]
    assert func(nums4, k4) == 3, f"Test Case 4 Failed: Expected {expected4}, Got {func(nums4, k4)}"

    # Test case 5
    nums5 = []
    k5 = 5
    expected5 = 0
    assert func(nums5, k5) == expected5, f"Test Case 5 Failed: Expected {expected5}, Got {func(nums5, k5)}"

    # Test case 6
    nums6 = [1]
    k6 = 5
    expected6 = 1
    assert func(nums6, k6) == expected6, f"Test Case 6 Failed: Expected {expected6}, Got {func(nums6, k6)}"

    # Test case 7
    nums7 = [1, 1, 1, 1, 1]
    k7 = 0
    expected7 = 1
    assert func(nums7, k7) == 1, f"Test Case 7 Failed: Expected {1}, Got {func(nums7, k7)}"

    # Test case 8
    nums8 = [1, 2, 3, 6, 7, 8]
    k8 = 1
    expected8 = 2
    assert func(nums8, k8) == 2, f"Test Case 8 Failed: Expected {expected8}, Got {func(nums8, k8)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()