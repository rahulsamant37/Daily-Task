# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) with the following constraint:
For any two consecutive elements `nums[i]` and `nums[j]` in the subsequence (where i < j), `nums[j] - nums[i] >= k`.

Example:
Input: nums = [3, 10, 2, 1, 20], k = 3
Output: 3
Explanation: The longest increasing subsequence satisfying the condition is [3, 10, 20].  Another valid subsequence is [1, 20]. The length is 3 and 2 respectively. Therefore the result is 3.

Input: nums = [1, 5, 2, 4, 3], k = 2
Output: 2
Explanation: The longest increasing subsequence satisfying the condition is [1, 5]. Another valid subsequence is [2, 4]. The length is 2 in both cases. Therefore the result is 2.
'''

# Solution
def longest_increasing_subsequence_with_k(nums, k):
    """
    Finds the length of the longest increasing subsequence in 'nums' with a difference of at least 'k'
    between consecutive elements.

    Args:
      nums: A list of integers.
      k: The minimum difference between consecutive elements in the subsequence.

    Returns:
      The length of the longest increasing subsequence.
    """
    n = len(nums)
    if n == 0:
        return 0

    # dp[i] stores the length of the longest increasing subsequence ending at nums[i].
    dp = [1] * n

    # Iterate through the array to build the dp table.
    for i in range(1, n):
        # For each element, check all previous elements to see if they can be part of the subsequence.
        for j in range(i):
            # If nums[i] can extend the subsequence ending at nums[j] (i.e., nums[i] > nums[j] and nums[i] - nums[j] >= k)
            if nums[i] > nums[j] and nums[i] - nums[j] >= k:
                # Update dp[i] if extending the subsequence at j results in a longer subsequence.
                dp[i] = max(dp[i], dp[j] + 1)

    # The maximum value in the dp table is the length of the longest increasing subsequence.
    return max(dp)

# Test cases
def test_longest_increasing_subsequence_with_k():
    assert longest_increasing_subsequence_with_k([3, 10, 2, 1, 20], 3) == 3
    assert longest_increasing_subsequence_with_k([1, 5, 2, 4, 3], 2) == 2
    assert longest_increasing_subsequence_with_k([1, 2, 3, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_k([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_k([1, 1, 1, 1, 1], 1) == 1
    assert longest_increasing_subsequence_with_k([1, 4, 2, 5, 3], 2) == 2
    assert longest_increasing_subsequence_with_k([], 2) == 0
    assert longest_increasing_subsequence_with_k([1], 2) == 1
    assert longest_increasing_subsequence_with_k([1, 5], 4) == 2
    assert longest_increasing_subsequence_with_k([1, 5, 9, 13], 4) == 4

if __name__ == "__main__":
    test_longest_increasing_subsequence_with_k()