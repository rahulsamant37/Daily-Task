# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) such that the difference between any two consecutive elements in the subsequence is at most `k`.

Example:
Input: nums = [3, 10, 2, 1, 20], k = 5
Output: 3
Explanation: One possible LIS is [3, 2, 1]. Another one is [3, 2, 20]. The length is 3.

Input: nums = [1, 3, 5, 2, 4], k = 1
Output: 2
Explanation: One possible LIS is [1, 2]. Another one is [3, 4].

Input: nums = [1, 5, 2, 4, 3], k = 2
Output: 3
Explanation: One possible LIS is [1, 2, 3].
'''

# Solution
def solution():
    def longest_increasing_subsequence_with_difference(nums, k):
        """
        Finds the length of the longest increasing subsequence with a maximum difference of k between consecutive elements.

        Args:
            nums: A list of integers.
            k: The maximum allowed difference between consecutive elements in the subsequence.

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
            # Iterate through the previous elements
            for j in range(i):
                # If nums[i] is greater than nums[j] and the difference is at most k
                if nums[i] > nums[j] and nums[i] - nums[j] <= k:
                    # Update dp[i] if a longer subsequence is found
                    dp[i] = max(dp[i], dp[j] + 1)

        # Return the maximum value in the dp array, which represents the length of the LIS
        return max(dp)

    return longest_increasing_subsequence_with_difference

# Test cases
def test_solution():
    lis_func = solution()

    # Test case 1
    nums1 = [3, 10, 2, 1, 20]
    k1 = 5
    expected1 = 3
    result1 = lis_func(nums1, k1)
    assert result1 == expected1, f"Test Case 1 Failed: Expected {expected1}, got {result1}"

    # Test case 2
    nums2 = [1, 3, 5, 2, 4]
    k2 = 1
    expected2 = 2
    result2 = lis_func(nums2, k2)
    assert result2 == expected2, f"Test Case 2 Failed: Expected {expected2}, got {result2}"

    # Test case 3
    nums3 = [1, 5, 2, 4, 3]
    k3 = 2
    expected3 = 3
    result3 = lis_func(nums3, k3)
    assert result3 == expected3, f"Test Case 3 Failed: Expected {expected3}, got {result3}"

    # Test case 4: Empty input array
    nums4 = []
    k4 = 3
    expected4 = 0
    result4 = lis_func(nums4, k4)
    assert result4 == expected4, f"Test Case 4 Failed: Expected {expected4}, got {result4}"

    # Test case 5: k = 0
    nums5 = [1, 2, 3, 4, 5]
    k5 = 0
    expected5 = 1
    result5 = lis_func(nums5, k5)
    assert result5 == expected5, f"Test Case 5 Failed: Expected {expected5}, got {result5}"

    # Test case 6: All elements are the same
    nums6 = [5, 5, 5, 5, 5]
    k6 = 5
    expected6 = 1
    result6 = lis_func(nums6, k6)
    assert result6 == expected6, f"Test Case 6 Failed: Expected {expected6}, got {result6}"
    
    # Test case 7: k is very large
    nums7 = [1, 2, 3, 4, 5]
    k7 = 100
    expected7 = 5
    result7 = lis_func(nums7, k7)
    assert result7 == expected7, f"Test Case 7 Failed: Expected {expected7}, got {result7}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()