# Python Question: Longest Increasing Subsequence with Limited Differences
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) where the difference between consecutive elements in the subsequence is at most `k`.

Example:
Input: nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], k = 2
Output: 4
Explanation: One possible LIS is [1, 1, 2, 3], where the difference between consecutive elements is at most 2. Another possible LIS is [3, 4, 5, 6]. The length of the longest such subsequence is 4.
'''

# Solution
def solution():
    def longest_increasing_subsequence_with_limited_differences(nums, k):
        """
        Finds the length of the longest increasing subsequence (LIS) where the difference between
        consecutive elements in the subsequence is at most `k`.

        Args:
            nums: A list of integers.
            k: An integer representing the maximum allowed difference between consecutive elements.

        Returns:
            The length of the longest increasing subsequence.
        """

        n = len(nums)
        if n == 0:
            return 0

        # dp[i] stores the length of the longest increasing subsequence ending at index i.
        dp = [1] * n

        # Iterate through the array to build the dp array.
        for i in range(1, n):
            # Iterate through the elements before nums[i].
            for j in range(i):
                # If nums[i] is greater than nums[j] and the difference is at most k,
                # update dp[i] if necessary.
                if nums[i] > nums[j] and nums[i] - nums[j] <= k:
                    dp[i] = max(dp[i], dp[j] + 1)

        # The maximum value in the dp array is the length of the LIS.
        return max(dp)

    return longest_increasing_subsequence_with_limited_differences

# Test cases
def test_solution():
    nums1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    k1 = 2
    expected1 = 4
    assert solution()(nums1, k1) == expected1

    nums2 = [1, 2, 3, 4, 5]
    k2 = 1
    expected2 = 5
    assert solution()(nums2, k2) == 5

    nums3 = [5, 4, 3, 2, 1]
    k3 = 1
    expected3 = 1
    assert solution()(nums3, k3) == 1

    nums4 = [1, 5, 2, 4, 3]
    k4 = 2
    expected4 = 3
    assert solution()(nums4, k4) == 3

    nums5 = [1, 1, 1, 1, 1]
    k5 = 0
    expected5 = 1
    assert solution()(nums5, k5) == 1

    nums6 = []
    k6 = 5
    expected6 = 0
    assert solution()(nums6, k6) == 0

    nums7 = [10, 20, 15, 30, 25]
    k7 = 5
    expected7 = 3
    assert solution()(nums7, k7) == 3

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()