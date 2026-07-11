# Python Question: Find the Longest Increasing Subsequence Length with a Twist
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) where the difference between consecutive elements in the subsequence must be at most `k`.

For example:
Input: nums = [3, 10, 2, 1, 20], k = 5
Output: 3
Explanation: One of the longest increasing subsequences with the given constraint is [3, 2, 1]. Another is [3, 2, 20]. The length is 3.

Input: nums = [1, 3, 2, 4, 5], k = 2
Output: 5
Explanation: The longest increasing subsequence is [1, 2, 4, 5]. [1, 3, 4, 5] is also a valid solution.

Input: nums = [1, 5, 7, 9, 2, 3, 4], k = 3
Output: 4
Explanation: One valid LIS is [1, 2, 3, 4]

'''

# Solution
def longest_increasing_subsequence_k(nums, k):
    """
    Finds the length of the longest increasing subsequence in nums such that the difference
    between consecutive elements is at most k.

    Args:
        nums: A list of integers.
        k: The maximum difference allowed between consecutive elements in the subsequence.

    Returns:
        The length of the longest increasing subsequence.
    """

    n = len(nums)
    if n == 0:
        return 0

    # dp[i] stores the length of the longest increasing subsequence ending at nums[i]
    dp = [1] * n

    # Iterate through the array to build the dp table
    for i in range(1, n):
        for j in range(i):
            # Check if nums[i] is greater than nums[j] and the difference is at most k
            if nums[i] > nums[j] and nums[i] - nums[j] <= k:
                # If so, update dp[i] to be the maximum of its current value and dp[j] + 1
                dp[i] = max(dp[i], dp[j] + 1)

    # The maximum value in the dp table is the length of the longest increasing subsequence
    return max(dp)

# Test cases
def test_longest_increasing_subsequence_k():
    assert longest_increasing_subsequence_k([3, 10, 2, 1, 20], 5) == 3
    assert longest_increasing_subsequence_k([1, 3, 2, 4, 5], 2) == 5
    assert longest_increasing_subsequence_k([1, 5, 7, 9, 2, 3, 4], 3) == 4
    assert longest_increasing_subsequence_k([1, 2, 3, 4, 5], 0) == 1
    assert longest_increasing_subsequence_k([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_k([], 5) == 0
    assert longest_increasing_subsequence_k([1], 5) == 1
    assert longest_increasing_subsequence_k([1, 2], 0) == 1
    assert longest_increasing_subsequence_k([1, 2], 1) == 2
    assert longest_increasing_subsequence_k([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1) == 10
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_increasing_subsequence_k()