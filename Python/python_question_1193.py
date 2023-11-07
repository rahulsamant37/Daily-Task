# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) such that the difference between consecutive elements in the subsequence is at most `k`.

Example:
Input: nums = [3, 10, 2, 1, 20], k = 3
Output: 4
Explanation: The longest increasing subsequence is [3, 2, 1, 20]. Notice that the differences are: 2-3 <= 3, 1-2 <= 3, 20-1 <=3. Another possible LIS is [3, 10, 20] where the differences are 10-3 <= 3, and 20 -10 <= 3. The length of LIS is 3. Another possible LIS is [3, 10], length is 2. Another possible LIS is [2, 20], length is 2. Another possible LIS is [1, 20], length is 2. The LIS is [1,2,3,4,5].

Input: nums = [1, 3, 5, 2, 4, 6], k = 1
Output: 3
Explanation: The longest increasing subsequence is [1, 2, 4]. Another possible LIS is [3, 4, 6].
'''

# Solution
def longest_increasing_subsequence_with_k_difference(nums, k):
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

    # Iterate through all possible ending positions for the subsequence.
    for i in range(1, n):
        # Iterate through all possible previous elements in the subsequence.
        for j in range(i):
            # If nums[i] is greater than nums[j] and the difference is at most k,
            # then we can extend the subsequence ending at nums[j] by adding nums[i].
            if nums[i] > nums[j] and nums[i] - nums[j] <= k:
                dp[i] = max(dp[i], dp[j] + 1)

    # The maximum value in dp is the length of the longest increasing subsequence.
    return max(dp)

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_k_difference([3, 10, 2, 1, 20], 3) == 4
    assert longest_increasing_subsequence_with_k_difference([1, 3, 5, 2, 4, 6], 1) == 3
    assert longest_increasing_subsequence_with_k_difference([1, 2, 3, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_k_difference([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_k_difference([1, 5, 2, 6, 3, 7], 2) == 4
    assert longest_increasing_subsequence_with_k_difference([], 2) == 0
    assert longest_increasing_subsequence_with_k_difference([1], 2) == 1
    assert longest_increasing_subsequence_with_k_difference([1,1,1,1,1], 0) == 1
    assert longest_increasing_subsequence_with_k_difference([1, 2, 3, 4, 5], 0) == 1
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()