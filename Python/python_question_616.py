# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums`, find the length of the longest increasing subsequence such that the difference between any two consecutive elements in the subsequence is at most `k`.

Example:
Input: nums = [1, 3, 2, 4, 5], k = 1
Output: 4
Explanation: The longest increasing subsequence is [1, 2, 3, 4] or [2, 3, 4, 5]. The length is 4.

Input: nums = [1, 5, 2, 6, 3, 7, 4, 8], k = 2
Output: 4
Explanation: The longest increasing subsequence is [1, 2, 3, 4]. The length is 4.  Another possible subsequence is [5, 6, 7, 8].

Input: nums = [1, 5, 2, 6, 3, 7, 4, 8], k = 1
Output: 2
Explanation: Possible subsequences are [1,2], [2,3], [3,4], [5,6], [6,7], [7,8]

'''

# Solution
def longest_increasing_subsequence_with_k_difference(nums, k):
    """
    Finds the length of the longest increasing subsequence with a maximum difference of k between consecutive elements.

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

    # Iterate through the array to build the dp array
    for i in range(1, n):
        # Iterate through the elements before nums[i]
        for j in range(i):
            # If nums[i] is greater than nums[j] and the difference is within the limit k
            if nums[i] > nums[j] and nums[i] - nums[j] <= k:
                # Update dp[i] if adding nums[i] to the subsequence ending at nums[j] results in a longer subsequence
                dp[i] = max(dp[i], dp[j] + 1)

    # The maximum value in the dp array is the length of the longest increasing subsequence
    return max(dp)

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_k_difference([1, 3, 2, 4, 5], 1) == 4
    assert longest_increasing_subsequence_with_k_difference([1, 5, 2, 6, 3, 7, 4, 8], 2) == 4
    assert longest_increasing_subsequence_with_k_difference([1, 5, 2, 6, 3, 7, 4, 8], 1) == 2
    assert longest_increasing_subsequence_with_k_difference([1, 2, 3, 4, 5], 0) == 1
    assert longest_increasing_subsequence_with_k_difference([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_k_difference([1, 1, 1, 1, 1], 0) == 1
    assert longest_increasing_subsequence_with_k_difference([], 1) == 0
    assert longest_increasing_subsequence_with_k_difference([1], 1) == 1
    assert longest_increasing_subsequence_with_k_difference([1,3,5,2,4], 2) == 3
    assert longest_increasing_subsequence_with_k_difference([10, 22, 9, 33, 21, 50, 41, 60, 80], 3) == 3

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()