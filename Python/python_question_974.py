# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) where the difference between consecutive elements in the subsequence is at most `k`.

Example:
Input: nums = [3, 10, 2, 1, 20], k = 3
Output: 4
Explanation: The longest increasing subsequence is [3, 2, 1, 20] with length 4 because:
- 2 - 3 <= 3 (absolute difference)
- 1 - 2 <= 3 (absolute difference)
- 20 - 1 <= 3 (absolute difference)

Input: nums = [1, 3, 2, 4, 5], k = 1
Output: 3
Explanation: The longest increasing subsequence is [1, 2, 4] with length 3 because:
- 2 - 1 <= 1 (absolute difference)
- 4 - 2 <= 1 (absolute difference)
'''

# Solution
def longest_increasing_subsequence_with_k(nums, k):
    """
    Finds the length of the longest increasing subsequence with a maximum difference of k between consecutive elements.

    Args:
        nums: A list of integers.
        k: The maximum allowed difference between consecutive elements.

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
        # Iterate through all previous elements to find potential predecessors.
        for j in range(i):
            # Check if nums[i] can extend the subsequence ending at nums[j].
            if nums[i] > nums[j] and abs(nums[i] - nums[j]) <= k:
                # Update dp[i] if a longer subsequence is found.
                dp[i] = max(dp[i], dp[j] + 1)

    # The maximum value in dp is the length of the longest increasing subsequence.
    return max(dp)

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_k([3, 10, 2, 1, 20], 3) == 4
    assert longest_increasing_subsequence_with_k([1, 3, 2, 4, 5], 1) == 3
    assert longest_increasing_subsequence_with_k([1, 2, 3, 4, 5], 0) == 1
    assert longest_increasing_subsequence_with_k([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_k([1, 5, 2, 4, 3], 2) == 3
    assert longest_increasing_subsequence_with_k([], 5) == 0
    assert longest_increasing_subsequence_with_k([1], 5) == 1
    assert longest_increasing_subsequence_with_k([1, 2, 3, 4, 5], 1) == 2
    assert longest_increasing_subsequence_with_k([10, 20, 1, 3, 5, 15], 5) == 4
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()