# Python Question: Longest Increasing Subsequence with Maximum Sum
'''
Given an array of integers `nums`, find the longest increasing subsequence (LIS) such that the sum of its elements is maximized. Return the maximum sum of such an LIS.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

An increasing subsequence is a subsequence where the elements are strictly increasing.

Example:
Input: nums = [1, 101, 2, 3, 100, 4, 5]
Output: 106
Explanation: The longest increasing subsequence with maximum sum is [1, 2, 3, 100], which has a sum of 106. Another possible LIS is [1, 2, 3, 4, 5], which has a sum of 15.

Input: nums = [10, 5, 4, 3]
Output: 10
Explanation: The longest increasing subsequence is [10], which has a sum of 10.
'''

# Solution
def solution():
    def longest_increasing_subsequence_sum(nums):
        """
        Finds the longest increasing subsequence with maximum sum.

        Args:
            nums: A list of integers.

        Returns:
            The maximum sum of a longest increasing subsequence.
        """

        n = len(nums)
        if n == 0:
            return 0

        # dp[i] stores the maximum sum of an increasing subsequence ending at index i.
        dp = [0] * n

        # Initialize dp with the value of each element itself, as a single element is an increasing subsequence.
        for i in range(n):
            dp[i] = nums[i]

        # Iterate through the array to find increasing subsequences.
        for i in range(1, n):
            for j in range(i):
                # If nums[i] is greater than nums[j], it can be added to the increasing subsequence ending at nums[j].
                if nums[i] > nums[j]:
                    # Update dp[i] if adding nums[i] to the subsequence ending at nums[j] results in a larger sum.
                    dp[i] = max(dp[i], dp[j] + nums[i])

        # The maximum value in dp is the maximum sum of an increasing subsequence.
        return max(dp)

    return longest_increasing_subsequence_sum


# Test cases
def test_solution():
    nums1 = [1, 101, 2, 3, 100, 4, 5]
    expected1 = 106
    assert solution()(nums1) == expected1, f"Test Case 1 Failed: Expected {expected1}, got {solution()(nums1)}"

    nums2 = [10, 5, 4, 3]
    expected2 = 10
    assert solution()(nums2) == expected2, f"Test Case 2 Failed: Expected {expected2}, got {solution()(nums2)}"

    nums3 = [3, 2, 6, 4, 5, 1, 7]
    expected3 = 15
    assert solution()(nums3) == expected3, f"Test Case 3 Failed: Expected {expected3}, got {solution()(nums3)}"

    nums4 = [0]
    expected4 = 0
    assert solution()(nums4) == expected4, f"Test Case 4 Failed: Expected {expected4}, got {solution()(nums4)}"

    nums5 = []
    expected5 = 0
    assert solution()(nums5) == 0, f"Test Case 5 Failed: Expected {expected5}, got {solution()(nums5)}"

    nums6 = [1, 2, 3, 4, 5]
    expected6 = 15
    assert solution()(nums6) == 15, f"Test Case 6 Failed: Expected {expected6}, got {solution()(nums6)}"

    nums7 = [5, 4, 3, 2, 1]
    expected7 = 5
    assert solution()(nums7) == 5, f"Test Case 7 Failed: Expected {expected7}, got {solution()(nums7)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()