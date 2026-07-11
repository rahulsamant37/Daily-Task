# Python Question: Find the Longest Increasing Subsequence with Specific End Value
'''
Given an array of integers `nums` and a target integer `target`, find the length of the longest increasing subsequence (LIS) in `nums` that ends with the `target` value. If no such LIS exists, return 0.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.

An increasing subsequence is a subsequence where the elements are in strictly increasing order.

Example:
Input: nums = [1, 3, 2, 4, 5], target = 5
Output: 4
Explanation: The longest increasing subsequence ending with 5 is [1, 2, 4, 5], which has a length of 4.

Input: nums = [1, 3, 2, 4, 5], target = 6
Output: 0
Explanation: There is no increasing subsequence ending with 6.

Input: nums = [10, 22, 9, 33, 21, 50, 41, 60, 80], target = 60
Output: 5
Explanation: The longest increasing subsequence ending with 60 is [10, 22, 33, 50, 60], which has a length of 5.
'''

# Solution
def longest_increasing_subsequence_with_target(nums, target):
    """
    Finds the length of the longest increasing subsequence (LIS) in nums that ends with the target value.

    Args:
        nums: A list of integers.
        target: The target integer.

    Returns:
        The length of the longest increasing subsequence ending with the target value, or 0 if no such LIS exists.
    """

    n = len(nums)
    # dp[i] stores the length of the longest increasing subsequence ending with nums[i]
    dp = [0] * n

    for i in range(n):
        # Iterate through all elements before nums[i]
        for j in range(i):
            # If nums[i] is greater than nums[j], it can potentially extend the subsequence ending at nums[j]
            if nums[i] > nums[j]:
                # Update dp[i] with the maximum length found so far, by extending LIS ending at nums[j]
                dp[i] = max(dp[i], dp[j])

        # Increment dp[i] by 1 to include nums[i] itself in the subsequence
        dp[i] += 1

    # Find the maximum length among all LIS that end with the target value
    max_len = 0
    for i in range(n):
        if nums[i] == target:
            max_len = max(max_len, dp[i])

    return max_len


# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_target([1, 3, 2, 4, 5], 5) == 4
    assert longest_increasing_subsequence_with_target([1, 3, 2, 4, 5], 6) == 0
    assert longest_increasing_subsequence_with_target([10, 22, 9, 33, 21, 50, 41, 60, 80], 60) == 5
    assert longest_increasing_subsequence_with_target([1, 2, 3, 4, 5], 5) == 5
    assert longest_increasing_subsequence_with_target([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_target([1, 1, 1, 1, 1], 1) == 1
    assert longest_increasing_subsequence_with_target([1, 3, 5, 2, 4, 6], 6) == 4
    assert longest_increasing_subsequence_with_target([2, 2, 2, 2, 2], 2) == 1
    assert longest_increasing_subsequence_with_target([], 5) == 0
    assert longest_increasing_subsequence_with_target([5], 5) == 1
    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()