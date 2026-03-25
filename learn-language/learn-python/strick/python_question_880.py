# Python Question: Longest Increasing Subsequence with Modification
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) of `nums` after applying at most `k` modifications. In a single modification, you can change the value of any element in `nums` to any other integer.

Example:
Input: nums = [4, 2, 3, 6, 10, 1, 12], k = 2
Output: 7
Explanation: We can change 4 to 1, and 1 to 5. The LIS becomes [2, 3, 6, 10, 12], which has length 5.
However, we can modify 4 to -1 and 1 to 5, resulting in [-1, 2, 3, 6, 10, 12], which has length 7.

Input: nums = [1, 5, 2, 3, 4, 9], k = 1
Output: 6
Explanation: The original LIS is [1, 2, 3, 4, 9], which has length 5. We can change 5 to 0 to get [0, 1, 2, 3, 4, 9], which has length 6.
'''

# Solution
def longest_increasing_subsequence_with_modification(nums, k):
    """
    Finds the length of the longest increasing subsequence (LIS) of nums after applying at most k modifications.

    Args:
        nums: A list of integers.
        k: The maximum number of modifications allowed.

    Returns:
        The length of the LIS after at most k modifications.
    """

    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]  # dp[i][j] is the length of LIS ending at nums[i] with j modifications used.

    for i in range(n):
        for j in range(k + 1):
            dp[i][j] = 1  # Initialize with 1 (the element itself).

            # Iterate through previous elements
            for p in range(i):
                # If nums[i] >= nums[p], we can extend the LIS without modification.
                if nums[i] >= nums[p]:
                    dp[i][j] = max(dp[i][j], dp[p][j] + 1)
                # If nums[i] < nums[p], we can extend the LIS with one modification (if modifications are available)
                elif j > 0:
                    dp[i][j] = max(dp[i][j], dp[p][j - 1] + 1)

    # Find the maximum length among all possible ending indices and modification counts.
    max_len = 0
    for i in range(n):
        for j in range(k + 1):
            max_len = max(max_len, dp[i][j])

    return max_len


# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_modification([4, 2, 3, 6, 10, 1, 12], 2) == 7
    assert longest_increasing_subsequence_with_modification([1, 5, 2, 3, 4, 9], 1) == 6
    assert longest_increasing_subsequence_with_modification([1, 2, 3, 4, 5], 0) == 5
    assert longest_increasing_subsequence_with_modification([5, 4, 3, 2, 1], 2) == 3
    assert longest_increasing_subsequence_with_modification([5, 4, 3, 2, 1], 5) == 5
    assert longest_increasing_subsequence_with_modification([1, 1, 1, 1, 1], 2) == 5
    assert longest_increasing_subsequence_with_modification([10, 22, 9, 33, 21, 50, 41, 60, 80], 0) == 6
    assert longest_increasing_subsequence_with_modification([10, 22, 9, 33, 21, 50, 41, 60, 80], 1) == 7
    assert longest_increasing_subsequence_with_modification([1, 3, 2, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_modification([1, 3, 2, 4, 5], 0) == 4
    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()