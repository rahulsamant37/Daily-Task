# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) with the following twist:
Elements `nums[i]` and `nums[j]` can only be included in the same increasing subsequence if `abs(nums[i] - nums[j]) <= k`.

Example:
Input: nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], k = 2
Output: 4
Explanation: One possible LIS is [3, 4, 5, 6]. Another is [1, 2, 3, 5].
'''

# Solution
def longest_increasing_subsequence_with_twist(nums, k):
    """
    Finds the length of the longest increasing subsequence with the given twist.

    Args:
        nums: A list of integers.
        k: An integer representing the maximum absolute difference between consecutive elements in the subsequence.

    Returns:
        The length of the longest increasing subsequence with the twist.
    """

    n = len(nums)
    if n == 0:
        return 0

    # dp[i] stores the length of the longest increasing subsequence ending at nums[i]
    dp = [1] * n

    # Iterate through the array to build the dp table
    for i in range(1, n):
        # For each element nums[i], check all previous elements nums[j]
        for j in range(i):
            # If nums[j] < nums[i] and the absolute difference is within k,
            # then we can extend the subsequence ending at nums[j]
            if nums[j] < nums[i] and abs(nums[i] - nums[j]) <= k:
                dp[i] = max(dp[i], dp[j] + 1)

    # The maximum value in the dp table is the length of the LIS
    return max(dp)

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_twist([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 2) == 4
    assert longest_increasing_subsequence_with_twist([1, 2, 3, 4, 5], 1) == 0
    assert longest_increasing_subsequence_with_twist([1, 2, 3, 4, 5], 2) == 0
    assert longest_increasing_subsequence_with_twist([1, 3, 5, 7, 9], 2) == 0
    assert longest_increasing_subsequence_with_twist([1, 3, 5, 7, 9], 3) == 0
    assert longest_increasing_subsequence_with_twist([1, 2, 3, 4, 5], 0) == 0
    assert longest_increasing_subsequence_with_twist([1, 3, 2, 4, 5], 1) == 0
    assert longest_increasing_subsequence_with_twist([1, 2, 3, 4, 5], 3) == 0
    assert longest_increasing_subsequence_with_twist([1, 2, 3], 1) == 0
    assert longest_increasing_subsequence_with_twist([1, 3, 2, 4, 5], 2) == 0
    assert longest_increasing_subsequence_with_twist([10, 22, 9, 33, 21, 50, 41, 60, 80], 5) == 0
    assert longest_increasing_subsequence_with_twist([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 2) == 1
    assert longest_increasing_subsequence_with_twist([1, 2, 3, 4, 5], 6) == 0
    assert longest_increasing_subsequence_with_twist([1, 5, 2, 6, 3, 7, 4, 8], 3) == 0
    assert longest_increasing_subsequence_with_twist([1, 5, 2, 6, 3, 7, 4, 8], 1) == 1
    assert longest_increasing_subsequence_with_twist([], 5) == 0
    assert longest_increasing_subsequence_with_twist([5], 5) == 1
    assert longest_increasing_subsequence_with_twist([1,1,1,1,1], 0) == 1
    assert longest_increasing_subsequence_with_twist([1,1,1,1,1], 1) == 1
    assert longest_increasing_subsequence_with_twist([1, 2, 3, 4, 5], 10) == 0

    def longest_increasing_subsequence_with_twist_modified(nums, k):
      n = len(nums)
      if n == 0:
          return 0

      dp = [1] * n

      for i in range(1, n):
          for j in range(i):
              if nums[j] < nums[i] and abs(nums[i] - nums[j]) <= k:
                  dp[i] = max(dp[i], dp[j] + 1)

      max_len = 0
      for i in range(n):
        max_len = max(max_len, dp[i])

      return max_len

    assert longest_increasing_subsequence_with_twist_modified([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 2) == 4
    assert longest_increasing_subsequence_with_twist_modified([1, 2, 3, 4, 5], 1) == 0
    assert longest_increasing_subsequence_with_twist_modified([1, 2, 3, 4, 5], 2) == 0
    assert longest_increasing_subsequence_with_twist_modified([1, 3, 5, 7, 9], 2) == 0
    assert longest_increasing_subsequence_with_twist_modified([1, 3, 5, 7, 9], 3) == 0
    assert longest_increasing_subsequence_with_twist_modified([1, 2, 3, 4, 5], 0) == 0
    assert longest_increasing_subsequence_with_twist_modified([1, 3, 2, 4, 5], 1) == 0
    assert longest_increasing_subsequence_with_twist_modified([1, 2, 3, 4, 5], 3) == 0
    assert longest_increasing_subsequence_with_twist_modified([1, 2, 3], 1) == 0
    assert longest_increasing_subsequence_with_twist_modified([1, 3, 2, 4, 5], 2) == 0
    assert longest_increasing_subsequence_with_twist_modified([10, 22, 9, 33, 21, 50, 41, 60, 80], 5) == 0
    assert longest_increasing_subsequence_with_twist_modified([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 2) == 1
    assert longest_increasing_subsequence_with_twist_modified([1, 2, 3, 4, 5], 6) == 0
    assert longest_increasing_subsequence_with_twist_modified([1, 5, 2, 6, 3, 7, 4, 8], 3) == 0
    assert longest_increasing_subsequence_with_twist_modified([1, 5, 2, 6, 3, 7, 4, 8], 1) == 1
    assert longest_increasing_subsequence_with_twist_modified([], 5) == 0
    assert longest_increasing_subsequence_with_twist_modified([5], 5) == 1
    assert longest_increasing_subsequence_with_twist_modified([1,1,1,1,1], 0) == 1
    assert longest_increasing_subsequence_with_twist_modified([1,1,1,1,1], 1) == 1
    assert longest_increasing_subsequence_with_twist_modified([1, 2, 3, 4, 5], 10) == 0

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()