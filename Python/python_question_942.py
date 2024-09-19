# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums`, find the length of the longest increasing subsequence (LIS) where the difference between consecutive elements in the subsequence must be less than or equal to a given integer `k`.

Example:
Input: nums = [3, 10, 2, 1, 20], k = 5
Output: 3
Explanation: The longest increasing subsequence satisfying the condition is [3, 10, 20] which has length 3 (difference between 3 and 10 is 7 > 5, 10 and 20 is 10 > 5. So it is not valid). The valid subsequence is [3, 10] or [2, 20] of length 2. The subsequence [1, 2, 3, 4, 5, 6] is an increasing sequence. The sequence [1, 2, 2, 3] is not strictly increasing. A valid LIS with k=5 is [3, 10, 15, 20]. [1, 2, 20] is also a valid LIS with k=19.
Another valid LIS for input nums = [3, 10, 2, 1, 20], k = 5 is [1, 2] with length 2. [1, 20] is invalid because 20-1 > 5.
The longest subsequence is [1, 2, 3, 4, 5] where each subsequent value is greater than the previous.
Input: nums = [1, 5, 2, 4, 3], k = 2
Output: 3
Explanation: The longest increasing subsequence satisfying the condition is [1, 2, 3] which has length 3.
'''

# Solution
def longest_increasing_subsequence_with_k(nums, k):
    """
    Finds the length of the longest increasing subsequence (LIS) where the difference
    between consecutive elements in the subsequence must be less than or equal to k.

    Args:
        nums: A list of integers.
        k: An integer representing the maximum allowed difference between consecutive elements.

    Returns:
        The length of the longest increasing subsequence satisfying the condition.
    """

    n = len(nums)
    if n == 0:
        return 0

    # dp[i] stores the length of the longest increasing subsequence ending at nums[i]
    dp = [1] * n

    # Iterate through the array
    for i in range(1, n):
        # For each element nums[i], iterate through the elements before it
        for j in range(i):
            # If nums[i] is greater than nums[j] and the difference between them is less than or equal to k
            if nums[i] > nums[j] and nums[i] - nums[j] <= k:
                # Update dp[i] if a longer subsequence is found
                dp[i] = max(dp[i], dp[j] + 1)

    # Return the maximum value in the dp array, which represents the length of the LIS
    return max(dp)


# Test cases
def test_longest_increasing_subsequence_with_k():
    assert longest_increasing_subsequence_with_k([3, 10, 2, 1, 20], 5) == 2
    assert longest_increasing_subsequence_with_k([1, 5, 2, 4, 3], 2) == 3
    assert longest_increasing_subsequence_with_k([1, 2, 3, 4, 5], 1) == 2
    assert longest_increasing_subsequence_with_k([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_k([1, 1, 1, 1, 1], 0) == 1
    assert longest_increasing_subsequence_with_k([1, 2, 3, 4, 5], 5) == 5
    assert longest_increasing_subsequence_with_k([10, 20, 30, 40, 50], 10) == 5
    assert longest_increasing_subsequence_with_k([10, 20, 30, 40, 50], 5) == 1
    assert longest_increasing_subsequence_with_k([], 5) == 0
    assert longest_increasing_subsequence_with_k([5], 5) == 1
    assert longest_increasing_subsequence_with_k([1, 3, 2, 4, 5], 1) == 2
    assert longest_increasing_subsequence_with_k([1, 3, 2, 4, 5], 2) == 3
    assert longest_increasing_subsequence_with_k([1, 3, 2, 4, 5], 3) == 4
    assert longest_increasing_subsequence_with_k([1, 3, 2, 4, 5], 4) == 5
    assert longest_increasing_subsequence_with_k([1, 10, 2, 9, 3, 8, 4, 7, 5, 6], 3) == 4
    print("All test cases passed!")


if __name__ == "__main__":
    test_longest_increasing_subsequence_with_k()