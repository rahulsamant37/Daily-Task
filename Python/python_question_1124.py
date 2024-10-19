# Python Question: Find the Longest Increasing Subsequence with given Constraints
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest strictly increasing subsequence (LIS) such that the difference between consecutive elements in the subsequence is at most `k`.

Example:
Input: nums = [3, 10, 2, 1, 20], k = 5
Output: 3
Explanation: The longest increasing subsequence satisfying the constraint is [3, 10, 20] or [2, 10, 20]. The length is 3.
Another valid subsequence is [1,2,3].

Input: nums = [4,2,1,4,3,1,5,6], k = 1
Output: 3
Explanation: One possible solution is [1, 1, 2]. Another one is [4, 5, 6].
'''

# Solution
def solution():
    def longest_increasing_subsequence_with_constraint(nums, k):
        """
        Finds the length of the longest strictly increasing subsequence (LIS)
        such that the difference between consecutive elements in the subsequence is at most `k`.

        Args:
            nums: A list of integers.
            k: An integer representing the maximum allowed difference between consecutive elements.

        Returns:
            The length of the longest increasing subsequence satisfying the constraint.
        """

        if not nums:
            return 0

        n = len(nums)
        dp = [1] * n  # dp[i] stores the length of the LIS ending at nums[i]

        for i in range(1, n):
            for j in range(i):
                # Check if nums[i] can be added to the LIS ending at nums[j]
                if nums[i] > nums[j] and nums[i] - nums[j] <= k:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

    return longest_increasing_subsequence_with_constraint

# Test cases
def test_solution():
    longest_increasing_subsequence_with_constraint = solution()

    # Test case 1
    nums1 = [3, 10, 2, 1, 20]
    k1 = 5
    expected1 = 3
    assert longest_increasing_subsequence_with_constraint(nums1, k1) == expected1, f"Test Case 1 Failed: Expected {expected1}, got {longest_increasing_subsequence_with_constraint(nums1, k1)}"

    # Test case 2
    nums2 = [4, 2, 1, 4, 3, 1, 5, 6]
    k2 = 1
    expected2 = 3
    assert longest_increasing_subsequence_with_constraint(nums2, k2) == expected2, f"Test Case 2 Failed: Expected {expected2}, got {longest_increasing_subsequence_with_constraint(nums2, k2)}"

    # Test case 3: Empty array
    nums3 = []
    k3 = 3
    expected3 = 0
    assert longest_increasing_subsequence_with_constraint(nums3, k3) == expected3, f"Test Case 3 Failed: Expected {expected3}, got {longest_increasing_subsequence_with_constraint(nums3, k3)}"

    # Test case 4: k = 0, no increasing subsequence possible
    nums4 = [1, 2, 3, 4, 5]
    k4 = 0
    expected4 = 1
    assert longest_increasing_subsequence_with_constraint(nums4, k4) == 1, f"Test Case 4 Failed: Expected {1}, got {longest_increasing_subsequence_with_constraint(nums4, k4)}"

    # Test case 5: All elements are the same
    nums5 = [5, 5, 5, 5, 5]
    k5 = 2
    expected5 = 1
    assert longest_increasing_subsequence_with_constraint(nums5, k5) == 1, f"Test Case 5 Failed: Expected {1}, got {longest_increasing_subsequence_with_constraint(nums5, k5)}"

    # Test case 6: k is large, basically find LIS
    nums6 = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    k6 = 100
    expected6 = 6
    assert longest_increasing_subsequence_with_constraint(nums6, k6) == expected6, f"Test Case 6 Failed: Expected {expected6}, got {longest_increasing_subsequence_with_constraint(nums6, k6)}"

    # Test case 7
    nums7 = [1, 5, 2, 4, 3]
    k7 = 2
    expected7 = 3
    assert longest_increasing_subsequence_with_constraint(nums7, k7) == 3, f"Test Case 7 Failed: Expected {expected7}, got {longest_increasing_subsequence_with_constraint(nums7, k7)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()