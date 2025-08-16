# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) where the difference between adjacent elements in the subsequence is at most `k`.

Example:
Input: nums = [3, 10, 2, 1, 20], k = 5
Output: 4
Explanation: One possible LIS is [3, 2, 1, 20] because:
- 2 - 3 = -1 <= 5
- 1 - 2 = -1 <= 5
- 20 - 1 = 19 > 5. The subsequence must be [3,2,1]. Then we can have [1,20], so [3,2,1,20].
Another LIS is [3, 10, 20] (10-3 <=5 and 20-10<=5).
Another LIS is [3,2,20].
The longest is [3, 10, 20] with length 3. Other LIS is [3,2,1,20].
Correct solution is [3,2,1].
Another LIS is [3,10].

Input: nums = [1, 5, 2, 4, 3], k = 1
Output: 3
Explanation: One possible LIS is [1, 2, 3] because:
- 2 - 1 = 1 <= 1
- 3 - 2 = 1 <= 1

Input: nums = [4, 2, 1, 4, 3, 5], k = 2
Output: 4
Explanation: One possible LIS is [4,3,5]. Another one is [2,1,3,5].
'''

# Solution
def longest_increasing_subsequence_with_k_diff(nums, k):
    """
    Finds the length of the longest increasing subsequence with a maximum difference of k between adjacent elements.

    Args:
        nums: A list of integers.
        k: The maximum difference allowed between adjacent elements in the subsequence.

    Returns:
        The length of the longest increasing subsequence with a maximum difference of k.
    """
    n = len(nums)
    if n == 0:
        return 0

    # dp[i] stores the length of the longest increasing subsequence ending at nums[i]
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j] and abs(nums[i] - nums[j]) <= k:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_k_diff([3, 10, 2, 1, 20], 5) == 4
    assert longest_increasing_subsequence_with_k_diff([1, 5, 2, 4, 3], 1) == 3
    assert longest_increasing_subsequence_with_k_diff([4, 2, 1, 4, 3, 5], 2) == 4
    assert longest_increasing_subsequence_with_k_diff([1, 2, 3, 4, 5], 0) == 1
    assert longest_increasing_subsequence_with_k_diff([5, 4, 3, 2, 1], 5) == 1
    assert longest_increasing_subsequence_with_k_diff([1, 2, 3, 4, 5], 1) == 2
    assert longest_increasing_subsequence_with_k_diff([], 5) == 0
    assert longest_increasing_subsequence_with_k_diff([1], 5) == 1
    assert longest_increasing_subsequence_with_k_diff([1, 1, 1, 1, 1], 0) == 1
    assert longest_increasing_subsequence_with_k_diff([1, 1, 1, 1, 1], 1) == 1
    assert longest_increasing_subsequence_with_k_diff([1, 3, 2, 4, 5], 2) == 4
    assert longest_increasing_subsequence_with_k_diff([10, 22, 9, 33, 21, 50, 41, 60, 80], 10) == 3

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()