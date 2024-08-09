# Python Question: Longest Increasing Subsequence with Specific End Digit
'''
Given a list of integers `nums` and a digit `end_digit`, find the length of the longest increasing subsequence (LIS) of `nums` that ends with the digit `end_digit`.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
An increasing subsequence is a subsequence where the elements are in strictly increasing order.

Example:
Input: nums = [1, 10, 2, 3, 20, 4, 5, 25], end_digit = 5
Output: 3
Explanation: The longest increasing subsequence ending with 5 is [1, 2, 5] or [1, 3, 5] or [1, 4, 5].  The length is 3.
'''

# Solution
def longest_increasing_subsequence_with_end_digit(nums, end_digit):
    """
    Finds the length of the longest increasing subsequence (LIS) of `nums` that ends with the digit `end_digit`.

    Args:
        nums: A list of integers.
        end_digit: The digit that the LIS must end with.

    Returns:
        The length of the LIS.
    """

    # dp[i] stores the length of the longest increasing subsequence ending at nums[i].
    dp = [1] * len(nums)

    # Iterate through the nums list.
    for i in range(1, len(nums)):
        # Iterate through the previous elements of nums.
        for j in range(i):
            # If nums[i] is greater than nums[j], it can potentially extend the LIS ending at nums[j].
            if nums[i] > nums[j]:
                # Update dp[i] if extending the subsequence ending at nums[j] results in a longer LIS.
                dp[i] = max(dp[i], dp[j] + 1)

    # Find the maximum LIS length among subsequences that end with the specified end_digit.
    max_len = 0
    for i in range(len(nums)):
        # Check if the last digit of nums[i] matches the specified end_digit.
        if nums[i] % 10 == end_digit:
            # Update max_len with the maximum LIS length found so far.
            max_len = max(max_len, dp[i])

    return max_len

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_end_digit([1, 10, 2, 3, 20, 4, 5, 25], 5) == 3
    assert longest_increasing_subsequence_with_end_digit([1, 2, 3, 4, 5], 5) == 5
    assert longest_increasing_subsequence_with_end_digit([5, 4, 3, 2, 1], 5) == 1
    assert longest_increasing_subsequence_with_end_digit([1, 2, 3, 4, 6], 5) == 0
    assert longest_increasing_subsequence_with_end_digit([1, 11, 21, 31, 41], 1) == 5
    assert longest_increasing_subsequence_with_end_digit([1, 10, 2, 3, 20, 4, 5, 25], 0) == 2
    assert longest_increasing_subsequence_with_end_digit([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0) == 1
    assert longest_increasing_subsequence_with_end_digit([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 0) == 1
    assert longest_increasing_subsequence_with_end_digit([10, 20, 30, 40, 50], 0) == 5
    assert longest_increasing_subsequence_with_end_digit([1, 2, 10, 3, 4, 20, 5, 6, 30], 0) == 3
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()