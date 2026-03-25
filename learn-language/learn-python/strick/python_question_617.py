# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) where the difference between consecutive elements is exactly `k`.

Example:
Input: nums = [3, 10, 3, 4, 5], k = 1
Output: 3
Explanation: The longest increasing subsequence with a difference of 1 is [3, 4, 5], which has a length of 3.

Input: nums = [1, 5, 7, 8, 5, 3, 4, 2, 1], k = 2
Output: 2
Explanation: The longest increasing subsequence with a difference of 2 is [1, 3], [5,7], [3,5] etc. which has a length of 2.
'''

# Solution
def solution():
    def longest_increasing_subsequence_with_difference(nums, k):
        """
        Finds the length of the longest increasing subsequence (LIS) where the difference
        between consecutive elements is exactly `k`.

        Args:
            nums: A list of integers.
            k: The required difference between consecutive elements in the LIS.

        Returns:
            The length of the longest increasing subsequence with the specified difference.
        """

        # dp[x] stores the length of the longest increasing subsequence ending at x
        dp = {}

        max_len = 0

        for num in nums:
            # If num - k exists in the dp, then we can extend the subsequence ending at num - k
            if num - k in dp:
                dp[num] = dp[num - k] + 1
            # Otherwise, we start a new subsequence of length 1
            else:
                dp[num] = 1

            # Update the maximum length found so far
            max_len = max(max_len, dp[num])

        return max_len

    return longest_increasing_subsequence_with_difference


# Test cases
def test_solution():
    func = solution()
    assert func([3, 10, 3, 4, 5], 1) == 3
    assert func([1, 5, 7, 8, 5, 3, 4, 2, 1], 2) == 2
    assert func([1, 2, 3, 4, 5], 1) == 5
    assert func([5, 4, 3, 2, 1], 1) == 1
    assert func([1, 3, 5, 7, 9], 2) == 5
    assert func([1, 3, 5, 7, 9], 1) == 1
    assert func([1, 2, 4, 6, 8, 10], 2) == 5
    assert func([1, 2, 4, 6, 8, 10], 3) == 1
    assert func([1], 1) == 1
    assert func([], 1) == 0
    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()