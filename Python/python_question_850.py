# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums`, find the length of the longest increasing subsequence such that each element in the subsequence must be a multiple of the previous element in the sequence.

Example:
Input: nums = [1, 3, 6, 12, 18]
Output: 4
Explanation: The longest increasing subsequence is [1, 3, 6, 12] or [1, 3, 6, 18].

Input: nums = [1, 5, 2, 4, 8]
Output: 4
Explanation: The longest increasing subsequence is [1, 2, 4, 8].

Input: nums = [2, 3, 4, 5, 6]
Output: 3
Explanation: The longest increasing subsequence is [2, 4, 6].

Input: nums = [4, 8, 10, 12, 16]
Output: 4
Explanation: The longest increasing subsequence is [4, 8, 16].

Input: nums = [1, 2, 3, 4, 5]
Output: 5
Explanation: The longest increasing subsequence is [1, 2, 3, 4, 5].
'''

# Solution
def solution():
    def longest_increasing_subsequence_multiple(nums):
        """
        Finds the length of the longest increasing subsequence where each element is a multiple of the previous one.

        Args:
            nums: A list of integers.

        Returns:
            The length of the longest increasing subsequence.
        """

        n = len(nums)
        if n == 0:
            return 0

        # dp[i] stores the length of the longest increasing subsequence ending at nums[i]
        dp = [1] * n

        # Iterate through the array
        for i in range(1, n):
            # For each element, iterate through the elements before it
            for j in range(i):
                # If nums[i] is a multiple of nums[j] and the subsequence ending at nums[j]
                # plus nums[i] is longer than the current subsequence ending at nums[i], update dp[i]
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)

        # The maximum value in dp is the length of the longest increasing subsequence
        return max(dp)

    return longest_increasing_subsequence_multiple

# Test cases
def test_solution():
    func = solution()
    assert func([1, 3, 6, 12, 18]) == 4
    assert func([1, 5, 2, 4, 8]) == 4
    assert func([2, 3, 4, 5, 6]) == 3
    assert func([4, 8, 10, 12, 16]) == 4
    assert func([1, 2, 3, 4, 5]) == 5
    assert func([2]) == 1
    assert func([]) == 0
    assert func([1, 2, 4, 6, 8, 10, 12, 14, 16]) == 5
    assert func([3, 6, 9, 12, 15, 18]) == 6
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()