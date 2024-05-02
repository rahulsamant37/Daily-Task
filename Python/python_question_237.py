# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums`, find the length of the longest increasing subsequence where the difference between consecutive elements in the subsequence must be less than or equal to a given integer `k`.

Example:
Input: nums = [3, 10, 2, 1, 20], k = 5
Output: 3
Explanation: One longest increasing subsequence is [3, 2, 1].  Another is [1, 2, 3]. [1, 2, 20] is not valid since 20-2 > 5. The length is 3.

Input: nums = [1, 3, 2, 4, 5], k = 2
Output: 4
Explanation: One longest increasing subsequence is [1, 3, 4, 5]. The differences are 3-1=2, 4-3=1, 5-4=1, all <= 2.
Another is [1, 2, 4, 5].
'''

# Solution
def solution():
    def longest_increasing_subsequence_with_k(nums, k):
        """
        Finds the length of the longest increasing subsequence with a difference constraint k.

        Args:
            nums: A list of integers.
            k: The maximum allowed difference between consecutive elements.

        Returns:
            The length of the longest increasing subsequence.
        """
        n = len(nums)
        if n == 0:
            return 0

        # dp[i] stores the length of the longest increasing subsequence ending at nums[i].
        dp = [1] * n

        # Iterate through the array to build the dp table.
        for i in range(1, n):
            for j in range(i):
                # Check if nums[i] can extend the subsequence ending at nums[j].
                if nums[i] > nums[j] and nums[i] - nums[j] <= k:
                    dp[i] = max(dp[i], dp[j] + 1)

        # The maximum value in the dp table is the length of the longest increasing subsequence.
        return max(dp)

    return longest_increasing_subsequence_with_k
    # Test cases
def test_solution():
    longest_increasing_subsequence_with_k = solution()
    # Test case 1
    nums1 = [3, 10, 2, 1, 20]
    k1 = 5
    expected1 = 3
    assert longest_increasing_subsequence_with_k(nums1, k1) == expected1, f"Test Case 1 Failed: Expected {expected1}, got {longest_increasing_subsequence_with_k(nums1, k1)}"

    # Test case 2
    nums2 = [1, 3, 2, 4, 5]
    k2 = 2
    expected2 = 4
    assert longest_increasing_subsequence_with_k(nums2, k2) == expected2, f"Test Case 2 Failed: Expected {expected2}, got {longest_increasing_subsequence_with_k(nums2, k2)}"

    # Test case 3
    nums3 = [1, 2, 3, 4, 5]
    k3 = 1
    expected3 = 2
    assert longest_increasing_subsequence_with_k(nums3, k3) == 2, f"Test Case 3 Failed: Expected {expected3}, got {longest_increasing_subsequence_with_k(nums3, k3)}"

    # Test case 4
    nums4 = [5, 4, 3, 2, 1]
    k4 = 1
    expected4 = 1
    assert longest_increasing_subsequence_with_k(nums4, k4) == expected4, f"Test Case 4 Failed: Expected {expected4}, got {longest_increasing_subsequence_with_k(nums4, k4)}"

    # Test case 5
    nums5 = [1, 1, 1, 1, 1]
    k5 = 0
    expected5 = 1
    assert longest_increasing_subsequence_with_k(nums5, k5) == expected5, f"Test Case 5 Failed: Expected {expected5}, got {longest_increasing_subsequence_with_k(nums5, k5)}"

    # Test case 6
    nums6 = []
    k6 = 5
    expected6 = 0
    assert longest_increasing_subsequence_with_k(nums6, k6) == expected6, f"Test Case 6 Failed: Expected {expected6}, got {longest_increasing_subsequence_with_k(nums6, k6)}"

    # Test case 7
    nums7 = [7,8,9,1,2,3]
    k7 = 2
    expected7 = 3
    assert longest_increasing_subsequence_with_k(nums7, k7) == expected7, f"Test Case 7 Failed: Expected {expected7}, got {longest_increasing_subsequence_with_k(nums7, k7)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()