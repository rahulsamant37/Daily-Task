# Python Question: Longest Increasing Subsequence with Modification
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) you can obtain after modifying at most `k` elements of the array. You can modify an element to any integer value.

Example:
Input: nums = [4, 2, 3, 6, 10, 1, 12], k = 2
Output: 6
Explanation: We can modify 4 -> 1, 1 -> 5 so the array becomes [1, 2, 3, 6, 10, 5, 12]. Then the LIS is [1, 2, 3, 6, 10, 12] which has length 6.

Input: nums = [3, 2, 1], k = 0
Output: 1
Explanation: No modifications allowed, the LIS is either [3], [2], or [1] which has length 1.

Input: nums = [3, 2, 1], k = 1
Output: 2
Explanation: We can modify 3 -> 0. Array becomes [0, 2, 1]. LIS is [0, 1] or [0,2] which has length 2.

Input: nums = [1, 5, 2, 4, 3], k = 1
Output: 4
Explanation: We can modify 5 -> 2. Array becomes [1, 2, 2, 4, 3]. LIS is [1, 2, 4] or [1,2,3] which has length 3 (incorrect). We can modify 3 -> 5. Array becomes [1, 5, 2, 4, 5]. LIS is [1, 2, 4, 5] which has length 4. Or modify 5 -> 1, array is [1,1,2,4,3], LIS is [1,2,4].
'''

# Solution
def longest_increasing_subsequence_with_modification(nums, k):
    """
    Finds the length of the longest increasing subsequence after modifying at most k elements.

    Args:
        nums: The input array of integers.
        k: The maximum number of modifications allowed.

    Returns:
        The length of the longest increasing subsequence.
    """

    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(k + 1):
            # Case 1: Don't include nums[i-1] in the LIS
            dp[i][j] = dp[i - 1][j]

            # Case 2: Include nums[i-1] in the LIS
            for p in range(i):
                # If p == 0, then there is no preceding element, so we consider it a valid start
                if p == 0:
                    if j >= 0:
                        dp[i][j] = max(dp[i][j], 1)
                else:
                    # If nums[i-1] > nums[p-1], we can directly extend the LIS
                    if nums[i - 1] > nums[p - 1]:
                        dp[i][j] = max(dp[i][j], dp[p][j] + 1)
                    # If nums[i-1] <= nums[p-1], we need to modify nums[p-1] or nums[i-1]
                    else:
                        if j > 0:
                            dp[i][j] = max(dp[i][j], dp[p][j - 1] + 1)

    # Find the maximum length of LIS across all possible modifications
    max_len = 0
    for j in range(k + 1):
        max_len = max(max_len, dp[n][j])

    return max_len

# Test cases
def test_longest_increasing_subsequence_with_modification():
    assert longest_increasing_subsequence_with_modification([4, 2, 3, 6, 10, 1, 12], 2) == 6
    assert longest_increasing_subsequence_with_modification([3, 2, 1], 0) == 1
    assert longest_increasing_subsequence_with_modification([3, 2, 1], 1) == 2
    assert longest_increasing_subsequence_with_modification([1, 5, 2, 4, 3], 1) == 4
    assert longest_increasing_subsequence_with_modification([1, 2, 3, 4, 5], 0) == 5
    assert longest_increasing_subsequence_with_modification([5, 4, 3, 2, 1], 5) == 5
    assert longest_increasing_subsequence_with_modification([5, 4, 3, 2, 1], 2) == 3
    assert longest_increasing_subsequence_with_modification([1, 3, 2, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_modification([1, 3, 2, 4, 5], 0) == 4
    assert longest_increasing_subsequence_with_modification([10, 22, 9, 33, 21, 50, 41, 60, 80], 0) == 6
    assert longest_increasing_subsequence_with_modification([10, 22, 9, 33, 21, 50, 41, 60, 80], 2) == 8
    assert longest_increasing_subsequence_with_modification([1, 1, 1, 1, 1], 2) == 5
    assert longest_increasing_subsequence_with_modification([1, 1, 1, 1, 1], 0) == 1
    assert longest_increasing_subsequence_with_modification([1, 1, 1, 1, 1], 4) == 5
    assert longest_increasing_subsequence_with_modification([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 5) == 6
    assert longest_increasing_subsequence_with_modification([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 0) == 1
    assert longest_increasing_subsequence_with_modification([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 9) == 10
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_increasing_subsequence_with_modification()