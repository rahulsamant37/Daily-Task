# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) such that the difference between consecutive elements in the subsequence is at most `k`.

Example:
Input: nums = [3, 10, 2, 1, 20], k = 5
Output: 3
Explanation: The longest increasing subsequence with a difference of at most 5 is [3, 2, 1] or [1, 2, 3] or [1, 2, 10]. The length is 3.
Another possible subsequence is [1,2,3].

Input: nums = [1, 5, 2, 4, 3], k = 1
Output: 3
Explanation: One possible longest increasing subsequence is [1, 2, 3].
'''

# Solution
def solution():
    def longest_increasing_subsequence_with_k_difference(nums, k):
        """
        Finds the length of the longest increasing subsequence with a difference of at most k.

        Args:
            nums: A list of integers.
            k: The maximum difference between consecutive elements in the subsequence.

        Returns:
            The length of the longest increasing subsequence.
        """

        n = len(nums)
        if n == 0:
            return 0

        # dp[i] stores the length of the longest increasing subsequence ending at nums[i].
        dp = [1] * n

        # Iterate through all possible ending positions of the subsequence.
        for i in range(1, n):
            # Iterate through all possible previous elements in the subsequence.
            for j in range(i):
                # Check if nums[i] can be added to the subsequence ending at nums[j].
                if nums[i] > nums[j] and nums[i] - nums[j] <= k:
                    # Update the length of the subsequence ending at nums[i].
                    dp[i] = max(dp[i], dp[j] + 1)

        # Return the maximum length of all subsequences.
        return max(dp)
    
    return longest_increasing_subsequence_with_k_difference


# Test cases
def test_solution():
    func = solution()
    assert func([3, 10, 2, 1, 20], 5) == 3
    assert func([1, 5, 2, 4, 3], 1) == 3
    assert func([1, 2, 3, 4, 5], 0) == 1
    assert func([5, 4, 3, 2, 1], 1) == 1
    assert func([1, 2, 3, 4, 5], 1) == 5
    assert func([1, 5, 2, 4, 3], 2) == 4
    assert func([1, 2, 3, 4, 5], 10) == 5
    assert func([5, 4, 3, 2, 1], 10) == 1
    assert func([1], 5) == 1
    assert func([], 5) == 0
    assert func([2,2,2,2,2], 0) == 1
    assert func([2,2,2,2,2], 1) == 1
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()