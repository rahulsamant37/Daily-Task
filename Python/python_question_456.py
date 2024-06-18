# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) where the difference between consecutive elements in the subsequence is exactly `k`.

Example:
Input: nums = [3, 10, 3, 6, 7, 8], k = 3
Output: 3
Explanation: The longest increasing subsequence with a difference of 3 is [3, 6, 9] or [7, 10].  In the given array, the subsequence is [3, 6]. Another subsequence would be [7, 10] if 10 was in the array.  So the longest sequence with difference 3 is [3,6]. So we look for [3,6,9], [7,10,13], etc. We have [3,6], [7], and [10]. The longest one is [3,6], so we should return 2.

Input: nums = [1, 5, 7, 8, 5, 3, 4, 2, 1], k = -2
Output: 4
Explanation:  The longest increasing subsequence with a difference of -2 is [7, 5, 3, 1].

Input: nums = [4, 12, 10, 0, -2, 10, 6, 10, 8, -4, 6, 0], k = 2
Output: 3
Explanation: One longest increasing subsequence with a difference of 2 is [-4, -2, 0]. Another is [6, 8, 10].
'''

# Solution
def solution():
    def longest_increasing_subsequence_with_difference(nums, k):
        """
        Finds the length of the longest increasing subsequence with a specific difference.

        Args:
            nums: A list of integers.
            k: The difference between consecutive elements in the subsequence.

        Returns:
            The length of the longest increasing subsequence with a difference of k.
        """

        # dp[num] stores the length of the longest increasing subsequence ending at num
        dp = {}

        max_length = 0

        for num in nums:
            # If num - k is in dp, then we can extend the subsequence ending at num - k
            if num - k in dp:
                dp[num] = dp[num - k] + 1
            else:
                # Otherwise, the subsequence starting at num has length 1
                dp[num] = 1

            # Update the maximum length
            max_length = max(max_length, dp[num])

        return max_length
    return longest_increasing_subsequence_with_difference

# Test cases
def test_solution():
    func = solution()
    assert func([3, 10, 3, 6, 7, 8], 3) == 2
    assert func([1, 5, 7, 8, 5, 3, 4, 2, 1], -2) == 4
    assert func([4, 12, 10, 0, -2, 10, 6, 10, 8, -4, 6, 0], 2) == 3
    assert func([1,2,3,4,5], 1) == 5
    assert func([5,4,3,2,1], -1) == 5
    assert func([1,2,3,4,5], 0) == 1
    assert func([1,1,1,1,1], 0) == 1
    assert func([1,1,1,1,1], 1) == 1
    assert func([1], 1) == 1
    assert func([], 1) == 0
    print("All test cases passed")

if __name__ == "__main__":
    test_solution()