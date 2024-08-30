# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) such that the difference between consecutive elements in the subsequence is at most `k`.

Example:
Input: nums = [3, 10, 2, 1, 20], k = 5
Output: 3
Explanation: The longest increasing subsequence with a difference of at most 5 is [3, 10, 20] or [2, 10, 20], which has length 3.  Other possible subsequences include [1,2], [1,2,3], [2,3].

Input: nums = [1, 3, 5, 2, 4, 6], k = 1
Output: 4
Explanation: The longest increasing subsequence with a difference of at most 1 is [1, 2, 3, 4] or [3, 4, 5, 6], which has length 4.

Input: nums = [1, 5, 2, 4, 3], k = 0
Output: 1
Explanation: The longest increasing subsequence with a difference of at most 0 is [1], [5], [2], [4], or [3], which has length 1.
'''

# Solution
def solution():
    def longest_increasing_subsequence_with_k_difference(nums, k):
        """
        Finds the length of the longest increasing subsequence in nums such that the difference
        between consecutive elements is at most k.

        Args:
            nums: A list of integers.
            k: The maximum difference allowed between consecutive elements.

        Returns:
            The length of the longest increasing subsequence.
        """

        n = len(nums)
        if n == 0:
            return 0

        # dp[i] stores the length of the longest increasing subsequence ending at nums[i]
        dp = [1] * n

        # Iterate through the nums array
        for i in range(1, n):
            # For each element nums[i], iterate through the elements before it
            for j in range(i):
                # If nums[i] is greater than nums[j] and the difference is at most k,
                # update dp[i] if a longer subsequence can be formed
                if nums[i] > nums[j] and nums[i] - nums[j] <= k:
                    dp[i] = max(dp[i], dp[j] + 1)

        # The maximum value in dp array is the length of the LIS
        return max(dp)

    return longest_increasing_subsequence_with_k_difference

# Test cases
def test_solution():
    lis_with_k = solution()

    # Test case 1
    nums1 = [3, 10, 2, 1, 20]
    k1 = 5
    expected1 = 3
    actual1 = lis_with_k(nums1, k1)
    assert actual1 == expected1, f"Test Case 1 Failed: Expected {expected1}, got {actual1}"
    print("Test Case 1 Passed")

    # Test case 2
    nums2 = [1, 3, 5, 2, 4, 6]
    k2 = 1
    expected2 = 4
    actual2 = lis_with_k(nums2, k2)
    assert actual2 == expected2, f"Test Case 2 Failed: Expected {expected2}, got {actual2}"
    print("Test Case 2 Passed")

    # Test case 3
    nums3 = [1, 5, 2, 4, 3]
    k3 = 0
    expected3 = 1
    actual3 = lis_with_k(nums3, k3)
    assert actual3 == expected3, f"Test Case 3 Failed: Expected {expected3}, got {actual3}"
    print("Test Case 3 Passed")

    # Test case 4
    nums4 = [1, 2, 3, 4, 5]
    k4 = 1
    expected4 = 5
    actual4 = lis_with_k(nums4, k4)
    assert actual4 == expected4, f"Test Case 4 Failed: Expected {expected4}, got {actual4}"
    print("Test Case 4 Passed")

    # Test case 5
    nums5 = [5, 4, 3, 2, 1]
    k5 = 1
    expected5 = 1
    actual5 = lis_with_k(nums5, k5)
    assert actual5 == expected5, f"Test Case 5 Failed: Expected {expected5}, got {actual5}"
    print("Test Case 5 Passed")

    # Test case 6
    nums6 = []
    k6 = 5
    expected6 = 0
    actual6 = lis_with_k(nums6, k6)
    assert actual6 == expected6, f"Test Case 6 Failed: Expected {expected6}, got {actual6}"
    print("Test Case 6 Passed")

    # Test case 7
    nums7 = [1, 1, 1, 1, 1]
    k7 = 0
    expected7 = 1
    actual7 = lis_with_k(nums7, k7)
    assert actual7 == expected7, f"Test Case 7 Failed: Expected {expected7}, got {actual7}"
    print("Test Case 7 Passed")

    # Test case 8
    nums8 = [1, 4, 2, 3, 5]
    k8 = 2
    expected8 = 4
    actual8 = lis_with_k(nums8, k8)
    assert actual8 == expected8, f"Test Case 8 Failed: Expected {expected8}, got {actual8}"
    print("Test Case 8 Passed")

if __name__ == "__main__":
    test_solution()