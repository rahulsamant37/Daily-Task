# Python Question: Longest Increasing Subsequence with Minimum Last Element
'''
Given an array of integers `nums`, find the length of the longest increasing subsequence (LIS).

However, if there are multiple LISs with the same length, return the LIS that has the smallest last element.

For example:
Input: nums = [1, 3, 2, 4, 5]
Output: 3 (The LIS is [1, 2, 4, 5], or [1, 3, 4, 5]. [1,2,4,5] has the smallest last element)

Input: nums = [1, 2, 3, 1, 2, 3]
Output: 3 (The LIS is [1, 2, 3])

Input: nums = [4, 3, 2, 1]
Output: 1

'''

# Solution
def solution():
    def longest_increasing_subsequence_with_min_last(nums):
        """
        Finds the length of the longest increasing subsequence with the minimum last element.

        Args:
            nums: A list of integers.

        Returns:
            The length of the longest increasing subsequence with the minimum last element.
        """

        if not nums:
            return 0

        # dp[i] stores the smallest last element of an increasing subsequence of length i+1.
        # Initialize dp with infinity for all lengths.
        dp = [float('inf')] * (len(nums) + 1)
        dp[0] = float('-inf')  # Base case: subsequence of length 0 has last element -inf

        # lengths[i] stores the number of subsequences of length i+1 ending with element dp[i]
        lengths = [0] * (len(nums) + 1)
        lengths[0] = 1

        max_len = 0  # Keep track of the maximum length of the increasing subsequence found so far

        for num in nums:
            # Binary search to find the smallest element in dp that is greater than or equal to num.
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if dp[mid] < num:
                    left = mid + 1
                else:
                    right = mid

            # If we found a smaller last element for an increasing subsequence of length left,
            # or if we can extend an existing subsequence to a longer one, update dp and lengths.
            if dp[left - 1] < num < dp[left]:
                dp[left] = num
                max_len = max(max_len, left)

        return max_len
    return longest_increasing_subsequence_with_min_last

# Test cases
def test_solution():
    func = solution()
    assert func([1, 3, 2, 4, 5]) == 5
    assert func([1, 2, 3, 1, 2, 3]) == 3
    assert func([4, 3, 2, 1]) == 1
    assert func([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert func([0, 1, 0, 3, 2, 3]) == 4
    assert func([]) == 0
    assert func([1]) == 1
    assert func([2,1,5,3,6,4,8,9,7]) == 6
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()