# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence (LIS) where the difference between consecutive elements in the subsequence is exactly `diff`.

Example:
Input: nums = [3, 0, 3, 4, 5, 6], diff = 3
Output: 4
Explanation: The longest increasing subsequence with a difference of 3 is [0, 3, 6], with a length of 3. Another one is [3, 6]. The longest increasing subsequence with a difference of 3 is [3, 0, 3, 4, 5, 6] is [3,6].
Input: nums = [1, 5, 7, 8, 5, 3, 4, 2, 1], diff = -2
Output: 4
Explanation: The longest increasing subsequence with a difference of -2 is [7, 5, 3, 1], with a length of 4.
'''

# Solution
def solution():
    def longest_increasing_subsequence_with_difference(nums, diff):
        """
        Finds the length of the longest increasing subsequence (LIS) where the difference between consecutive elements in the subsequence is exactly `diff`.

        Args:
            nums: A list of integers.
            diff: The required difference between consecutive elements in the subsequence.

        Returns:
            The length of the longest increasing subsequence with the specified difference.
        """

        # Create a dictionary to store the length of the longest increasing subsequence ending at each number.
        dp = {}

        # Iterate through the numbers in the input array.
        for num in nums:
            # If the number preceding the current number (num - diff) is already in the dictionary,
            # it means that there is an existing subsequence that can be extended by adding the current number.
            if num - diff in dp:
                # The length of the new subsequence is the length of the existing subsequence plus 1.
                dp[num] = dp[num - diff] + 1
            else:
                # If the number preceding the current number is not in the dictionary,
                # it means that the current number starts a new subsequence of length 1.
                dp[num] = 1

        # Return the maximum length of any subsequence.
        return max(dp.values()) if dp else 0

    return longest_increasing_subsequence_with_difference

# Test cases
def test_solution():
    func = solution()
    assert func([3, 0, 3, 4, 5, 6], 3) == 4
    assert func([1, 5, 7, 8, 5, 3, 4, 2, 1], -2) == 4
    assert func([1, 2, 3, 4, 5], 1) == 5
    assert func([1, 3, 5, 7, 9], 2) == 5
    assert func([5, 4, 3, 2, 1], -1) == 5
    assert func([5, 4, 3, 2, 1], 1) == 1
    assert func([1, 1, 1, 1, 1], 0) == 5
    assert func([1, 1, 1, 1, 1], 1) == 1
    assert func([], 1) == 0
    assert func([1], 1) == 1
    assert func([1, 2], 1) == 2
    assert func([2, 1], -1) == 2
    assert func([2, 1], 1) == 1
    assert func([7, 1, 8, 5, 0, 9, 2, 6, 3, 4], 1) == 4

if __name__ == "__main__":
    test_solution()