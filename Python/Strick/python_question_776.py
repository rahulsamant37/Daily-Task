# Python Question: Longest Increasing Subsequence with Specific Divisibility
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) such that each element in the subsequence is divisible by `k`.

An increasing subsequence is a sequence of numbers from the input array such that the numbers are in strictly increasing order.

Example:
Input: nums = [3, 6, 7, 12, 15, 18, 21, 24], k = 3
Output: 6
Explanation: The longest increasing subsequence divisible by 3 is [3, 6, 12, 15, 18, 21, 24], with a length of 7.

Input: nums = [2, 4, 6, 8, 10, 12, 14, 16], k = 2
Output: 8
Explanation: The longest increasing subsequence divisible by 2 is [2, 4, 6, 8, 10, 12, 14, 16], with a length of 8.

Input: nums = [1, 2, 3, 4, 5, 6, 7, 8], k = 3
Output: 2
Explanation: The longest increasing subsequence divisible by 3 is [3, 6], with a length of 2.

Input: nums = [1, 5, 2, 4, 3], k = 2
Output: 2
Explanation: The longest increasing subsequence divisible by 2 is [2, 4], with a length of 2.
'''

# Solution
def longest_increasing_subsequence_divisible_by_k(nums, k):
    """
    Finds the length of the longest increasing subsequence (LIS) such that each element in the subsequence is divisible by `k`.

    Args:
        nums: A list of integers.
        k: An integer representing the divisor.

    Returns:
        The length of the LIS divisible by k.
    """

    # Filter the numbers divisible by k
    divisible_nums = [num for num in nums if num % k == 0]

    # If there are no numbers divisible by k, return 0
    if not divisible_nums:
        return 0

    # dp[i] stores the smallest tail of all increasing subsequences of length i+1.
    # Initialize dp with infinity for all lengths.
    dp = [float('inf')] * (len(divisible_nums) + 1)
    dp[0] = float('-inf')

    # Iterate through the filtered numbers
    for num in divisible_nums:
        # Find the smallest index i such that dp[i] >= num using binary search.
        # This means we can extend the subsequence of length i to length i+1 by adding num.
        l, r = 0, len(divisible_nums)
        while l <= r:
            mid = (l + r) // 2
            if dp[mid] < num:
                l = mid + 1
            else:
                r = mid - 1

        # Update dp[l] to num, because we found a subsequence of length l+1 with a smaller tail (num).
        # This ensures that dp[i] always stores the smallest tail for subsequences of length i+1.
        dp[l] = num

    # The length of the LIS is the largest index i such that dp[i] is not infinity.
    # This is because dp[i] stores the smallest tail for subsequences of length i+1.
    lis_length = 0
    for i in range(len(dp)):
        if dp[i] != float('inf'):
            lis_length = i

    return lis_length
    

# Test cases
def test_longest_increasing_subsequence_divisible_by_k():
    assert longest_increasing_subsequence_divisible_by_k([3, 6, 7, 12, 15, 18, 21, 24], 3) == 7
    assert longest_increasing_subsequence_divisible_by_k([2, 4, 6, 8, 10, 12, 14, 16], 2) == 8
    assert longest_increasing_subsequence_divisible_by_k([1, 2, 3, 4, 5, 6, 7, 8], 3) == 2
    assert longest_increasing_subsequence_divisible_by_k([1, 5, 2, 4, 3], 2) == 2
    assert longest_increasing_subsequence_divisible_by_k([1, 3, 5, 7, 9], 2) == 0
    assert longest_increasing_subsequence_divisible_by_k([2, 4, 6, 3, 5, 7, 8], 2) == 4
    assert longest_increasing_subsequence_divisible_by_k([5, 10, 3, 6, 2, 4], 2) == 3
    assert longest_increasing_subsequence_divisible_by_k([1, 2, 3, 4, 5, 6], 1) == 6
    assert longest_increasing_subsequence_divisible_by_k([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 2) == 1
    assert longest_increasing_subsequence_divisible_by_k([2, 1, 4, 3, 6, 5], 2) == 3
    assert longest_increasing_subsequence_divisible_by_k([4, 8, 1, 3, 5, 7, 12, 16], 4) == 4
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_increasing_subsequence_divisible_by_k()