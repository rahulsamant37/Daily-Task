# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums`, find the length of the longest increasing subsequence where the difference between consecutive elements is at most 1.

Example:
Input: nums = [3, 10, 3, 2, 1, 20]
Output: 2
Explanation: The longest increasing subsequence with a difference of at most 1 is [3, 2, 1] or [1,2] with length 2.

Input: nums = [1, 2, 3, 4, 5]
Output: 5
Explanation: The longest increasing subsequence with a difference of at most 1 is [1, 2, 3, 4, 5] with length 5.

Input: nums = [5, 4, 3, 2, 1]
Output: 1
Explanation: The longest increasing subsequence with a difference of at most 1 is [5], [4], [3], [2], or [1] with length 1.

Input: nums = [1, 3, 2, 4, 5]
Output: 3
Explanation: The longest increasing subsequence with a difference of at most 1 is [1, 2, 4] or [1, 2, 3] with length 3.
'''

# Solution
def solution():
    def longest_increasing_subsequence_with_difference_one(nums):
        """
        Finds the length of the longest increasing subsequence where the difference
        between consecutive elements is at most 1.
        """
        if not nums:
            return 0

        n = len(nums)
        dp = [1] * n  # Initialize dp array with 1, as each element is a subsequence of length 1

        # Iterate through the array
        for i in range(1, n):
            # Iterate through the elements before the current element
            for j in range(i):
                # Check if the current element is greater than the previous element and
                # if the difference between them is at most 1
                if nums[i] > nums[j] and nums[i] - nums[j] <= 1:
                    # Update the dp array if a longer subsequence is found
                    dp[i] = max(dp[i], dp[j] + 1)

        # Return the maximum value in the dp array, which is the length of the
        # longest increasing subsequence with a difference of at most 1
        return max(dp)

    return longest_increasing_subsequence_with_difference_one

# Test cases
def test_solution():
    func = solution()
    assert func([3, 10, 3, 2, 1, 20]) == 2
    assert func([1, 2, 3, 4, 5]) == 5
    assert func([5, 4, 3, 2, 1]) == 1
    assert func([1, 3, 2, 4, 5]) == 3
    assert func([1, 2, 1, 2, 3, 2, 3, 4]) == 4
    assert func([1]) == 1
    assert func([]) == 0
    assert func([2, 2, 2, 2]) == 1
    assert func([1, 2, 3, 1, 2, 3]) == 3
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()