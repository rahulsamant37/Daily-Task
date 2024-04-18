# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) of `nums` such that the difference between consecutive elements in the subsequence is at most `k`.

Example:
Input: nums = [3, 10, 2, 1, 20], k = 5
Output: 3
Explanation: One possible LIS is [3, 2, 1], but it's decreasing. An increasing subsequence with a max difference of 5 is [3, 20], length 2. Another is [2, 1], decreasing. One possible LIS is [1, 2, 3], but needs sorting.  An LIS with difference <= k is [3, 10, 20]. The LIS [1,2] has length 2, and difference 1. The LIS [2,3] has length 2, but [3,2] is not increasing. The LIS [1,2,3] would require sorting. So, the longest is [3,10,20] (not increasing). [1,2] has length 2. [2,3] has length 2. [1,20] is not increasing. [2,20] is not increasing. [10,20] has length 2.  [1,2,3] (need to sort first). [1,2,3,10,20] (sort first).  So, we need to find the LIS while maintaining the order in the original array. The LIS [3, 10, 20] satisfies the condition. The length is 3.

Input: nums = [4,2,1,4,3,1,5,6], k = 1
Output: 3
Explanation: One possible LIS is [1, 1, 1], but it's not increasing. [1, 1, 1, ...] will not do. [4,5,6] is the correct LIS. Length is 3. Another possible LIS is [2,3]. [4,3] is not increasing. [1,3]. [1,3,5,6] is not valid since 1,3 are not next to each other.

Input: nums = [1, 5, 2, 4, 3], k = 2
Output: 3
Explanation: [1, 2, 3] is a valid LIS.

Input: nums = [1, 3, 2, 4, 5], k = 1
Output: 2
Explanation: [1, 2] or [3, 4] or [4, 5]
'''

# Solution
def longest_increasing_subsequence_with_k_difference(nums, k):
    """
    Finds the length of the longest increasing subsequence of nums such that the difference
    between consecutive elements in the subsequence is at most k.

    Args:
        nums: A list of integers.
        k: An integer representing the maximum difference between consecutive elements.

    Returns:
        The length of the longest increasing subsequence.
    """

    n = len(nums)
    if n == 0:
        return 0

    # dp[i] stores the length of the longest increasing subsequence ending at nums[i]
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j] and nums[i] - nums[j] <= k:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_k_difference([3, 10, 2, 1, 20], 5) == 3
    assert longest_increasing_subsequence_with_k_difference([4, 2, 1, 4, 3, 1, 5, 6], 1) == 3
    assert longest_increasing_subsequence_with_k_difference([1, 5, 2, 4, 3], 2) == 3
    assert longest_increasing_subsequence_with_k_difference([1, 3, 2, 4, 5], 1) == 2
    assert longest_increasing_subsequence_with_k_difference([1, 2, 3, 4, 5], 1) == 2
    assert longest_increasing_subsequence_with_k_difference([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_k_difference([1, 1, 1, 1, 1], 0) == 1
    assert longest_increasing_subsequence_with_k_difference([], 5) == 0
    assert longest_increasing_subsequence_with_k_difference([1], 5) == 1
    assert longest_increasing_subsequence_with_k_difference([1, 2], 1) == 2
    assert longest_increasing_subsequence_with_k_difference([1, 3], 1) == 1

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()