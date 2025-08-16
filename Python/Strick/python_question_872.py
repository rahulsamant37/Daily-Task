# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums`, find the length of the longest increasing subsequence with a twist. The twist is that you are allowed to skip *at most one* element in the subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.
An increasing subsequence is a subsequence in which the elements are strictly increasing.

For example:
Input: nums = [1, 3, 2, 4, 5]
Output: 4
Explanation: The longest increasing subsequence is [1, 2, 4, 5] (skipping 3).

Input: nums = [1, 2, 3, 4, 5]
Output: 5
Explanation: The longest increasing subsequence is [1, 2, 3, 4, 5] (no skip needed).

Input: nums = [5, 4, 3, 2, 1]
Output: 2
Explanation: The longest increasing subsequence is [5, x, 4] where 'x' is skipped, or [4, x, 3], and so on. We can choose any two consecutive elements.

Input: nums = [1, 5, 2, 6, 3, 7]
Output: 4
Explanation: The longest increasing subsequence is [1, 2, 6, 7] (skipping 5 and 3). Or [1, 5, 6, 7] skipping 2 and 3. Or [1, 2, 3, 7] skipping 5 and 6.
'''

# Solution
def solution(nums):
    """
    Finds the length of the longest increasing subsequence with at most one skip.

    Args:
        nums: A list of integers.

    Returns:
        The length of the longest increasing subsequence with at most one skip.
    """
    n = len(nums)
    if n <= 1:
        return n

    # dp[i][0] is the length of the LIS ending at nums[i] without any skip.
    # dp[i][1] is the length of the LIS ending at nums[i] with one skip.
    dp = [[1, 1] for _ in range(n)]

    max_len = 1

    for i in range(1, n):
        for j in range(i):
            # Case 1: No skip at nums[i]
            if nums[i] > nums[j]:
                dp[i][0] = max(dp[i][0], dp[j][0] + 1)
                dp[i][1] = max(dp[i][1], dp[j][1] + 1) # can still continue skip chain.

            # Case 2: Skip nums[j] when building subsequence up to nums[i].
            # We only skip one element.
            # Condition: dp[j][0] > 1 to ensure we have at least 2 elements before the skip.
            # Otherwise, skipping the first element doesn't make sense in the LIS.
            if dp[j][0] > 1 and nums[i] > nums[j]:
                dp[i][1] = max(dp[i][1], dp[j][0]) # We're skipping nums[j], so we take the length without skip ending at j.

        max_len = max(max_len, dp[i][0], dp[i][1])

    return max_len

# Test cases
def test_solution():
    assert solution([1, 3, 2, 4, 5]) == 4
    assert solution([1, 2, 3, 4, 5]) == 5
    assert solution([5, 4, 3, 2, 1]) == 2
    assert solution([1, 5, 2, 6, 3, 7]) == 4
    assert solution([10, 22, 9, 33, 21, 50, 41, 60, 80]) == 6
    assert solution([1, 2]) == 2
    assert solution([2, 1]) == 2
    assert solution([1]) == 1
    assert solution([]) == 0
    assert solution([3,10,2,1,20]) == 4
    assert solution([7,8,9,1,2,3,4,5,6]) == 7
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()