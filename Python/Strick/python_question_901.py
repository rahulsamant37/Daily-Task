# Python Question:  Longest Increasing Subsequence with Maximum Sum
'''
Given an array of integers `nums`, find the longest increasing subsequence (LIS) such that the sum of its elements is maximized.  Return the maximum sum of such a subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.  For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

An increasing subsequence is a subsequence where the elements are strictly increasing.

Example:
Input: nums = [1, 101, 2, 3, 100, 4, 5]
Output: 106
Explanation: The longest increasing subsequence with maximum sum is [1, 2, 3, 100], which has a sum of 106.  Another valid LIS is [1, 2, 3, 4, 5] which has a sum of 15.  We want the one with the maximum sum.

Input: nums = [10, 5, 4, 3]
Output: 10
Explanation: The longest increasing subsequence is [10], [5], [4], or [3]. The maximum sum is 10.

Input: nums = [1, 3, 2, 4, 5]
Output: 15
Explanation: The longest increasing subsequence is [1, 2, 4, 5] or [1, 3, 4, 5].  The maximum sum is 1 + 3 + 4 + 5 = 15.
'''

# Solution
def solution():
    def longest_increasing_subsequence_sum(nums):
        """
        Calculates the maximum sum of the longest increasing subsequence of a given array.

        Args:
            nums: A list of integers.

        Returns:
            The maximum sum of the longest increasing subsequence.
        """

        n = len(nums)
        # dp[i] stores the maximum sum of an increasing subsequence ending at nums[i]
        dp = [0] * n

        # Initialize dp with the values of nums itself (each element is an increasing subsequence of length 1)
        for i in range(n):
            dp[i] = nums[i]

        # Iterate through the array to find increasing subsequences
        for i in range(1, n):
            for j in range(i):
                # If nums[i] can extend the increasing subsequence ending at nums[j]
                if nums[i] > nums[j]:
                    # Update dp[i] if extending the subsequence at j gives a larger sum
                    dp[i] = max(dp[i], dp[j] + nums[i])

        # The maximum value in dp is the maximum sum of any increasing subsequence
        return max(dp) if dp else 0
    
    return longest_increasing_subsequence_sum

# Test cases
def test_solution():
    lis_sum = solution()
    assert lis_sum([1, 101, 2, 3, 100, 4, 5]) == 106
    assert lis_sum([10, 5, 4, 3]) == 10
    assert lis_sum([1, 3, 2, 4, 5]) == 15
    assert lis_sum([1, 2, 3, 4, 5]) == 15
    assert lis_sum([5, 4, 3, 2, 1]) == 5
    assert lis_sum([1]) == 1
    assert lis_sum([]) == 0
    assert lis_sum([1, 1, 1, 1]) == 1
    assert lis_sum([10, 22, 9, 33, 21, 50, 41, 60, 80]) == 255
    assert lis_sum([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]) == 50

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()