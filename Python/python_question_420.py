# Python Question: Find the Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence where the difference between consecutive elements is exactly `diff`.

Example:
Input: nums = [3, 0, 3, 4, 5, 6], diff = 3
Output: 4
Explanation: The longest increasing subsequence with a difference of 3 is [0, 3, 6]. Its length is 3.
Another possible subsequence is [3, 6], with length 2. However, [3,4,5,6] is not a valid subsequence because the difference is 1 and not 3.
Another possible subsequence is [3,6], with length 2. However, the longest one is [3, 0, 3, 6] where the subsequence is [3,6] and the length is 2.
Input: nums = [1,5,7,8,5,3,4,2,1], diff = -2
Output: 4
Explanation: The longest increasing subsequence with a difference of -2 is [7, 5, 3, 1]. Its length is 4.

'''

# Solution
def solution():
    def longest_increasing_subsequence_with_diff(nums, diff):
        """
        Finds the length of the longest increasing subsequence with a specific difference.

        Args:
            nums: A list of integers.
            diff: The required difference between consecutive elements in the subsequence.

        Returns:
            The length of the longest increasing subsequence with the specified difference.
        """

        # Use a dictionary to store the length of the longest increasing subsequence
        # ending at each number.  Key is the number, value is the length.
        dp = {}

        # Iterate through the numbers in the input array
        for num in nums:
            # If the number minus the difference is already in the dp dictionary,
            # it means we can extend an existing subsequence.
            if num - diff in dp:
                # The length of the longest increasing subsequence ending at the current number
                # is one more than the length of the longest increasing subsequence ending at
                # the previous number (num - diff).
                dp[num] = dp[num - diff] + 1
            else:
                # If the number minus the difference is not in the dp dictionary,
                # it means we are starting a new subsequence.
                dp[num] = 1

        # Return the maximum value in the dp dictionary, which represents the
        # length of the longest increasing subsequence with the specified difference.
        if not dp:
            return 0
        return max(dp.values())

    return longest_increasing_subsequence_with_diff

# Test cases
def test_solution():
    func = solution()
    assert func([3, 0, 3, 4, 5, 6], 3) == 1 # [3,6]
    assert func([1,5,7,8,5,3,4,2,1], -2) == 4
    assert func([1,2,3,4,5], 1) == 5
    assert func([1,2,3,4,5], 2) == 1
    assert func([1,2,3,4,5], -1) == 1
    assert func([1,2,3,4,5], 0) == 1
    assert func([1,1,1,1,1], 0) == 5
    assert func([1,1,1,1,1], 1) == 1
    assert func([], 1) == 0
    assert func([5], 2) == 1
    assert func([1, 3, 5, 7, 9], 2) == 5
    assert func([9, 7, 5, 3, 1], -2) == 5
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()