# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) with the following constraint:
- For any two consecutive elements `nums[i]` and `nums[j]` in the subsequence (where i < j), `nums[j] - nums[i] <= k`.

Example:
Input: nums = [3, 10, 2, 1, 20], k = 5
Output: 3
Explanation: The longest increasing subsequence that satisfies the condition is [3, 2, 1]. Note that the elements don't need to be in the same order as in the input array, but must be increasing. Since 10-3 > 5 and 20-3 > 5, 10 and 20 cannot be added to the subsequence starting with 3. Valid subsequences of length 3 are [1,2,3] and [2,3,10].
Input: nums = [1, 2, 3, 4, 5], k = 1
Output: 2
Explanation: [1,2], [2,3], [3,4], [4,5] are valid subsequences. No subsequence with length 3 or more is possible because the difference between the first and last element will be greater than k.
'''

# Solution
def longest_increasing_subsequence_with_k(nums, k):
    """
    Finds the length of the longest increasing subsequence with a maximum difference k.

    Args:
        nums: A list of integers.
        k: The maximum difference between consecutive elements in the subsequence.

    Returns:
        The length of the longest increasing subsequence.
    """
    n = len(nums)
    if n == 0:
        return 0

    # dp[i] stores the length of the longest increasing subsequence ending at nums[i]
    dp = [1] * n

    # Iterate through the array
    for i in range(1, n):
        # Iterate through the previous elements
        for j in range(i):
            # Check if the current element is greater than the previous element
            # and if the difference between them is less than or equal to k
            if nums[i] > nums[j] and nums[i] - nums[j] <= k:
                # If both conditions are met, update the length of the LIS ending at nums[i]
                dp[i] = max(dp[i], dp[j] + 1)

    # Return the maximum length of the LIS
    return max(dp)

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_k([3, 10, 2, 1, 20], 5) == 3
    assert longest_increasing_subsequence_with_k([1, 2, 3, 4, 5], 1) == 2
    assert longest_increasing_subsequence_with_k([5, 4, 3, 2, 1], 2) == 1
    assert longest_increasing_subsequence_with_k([1, 5, 2, 4, 3], 3) == 3
    assert longest_increasing_subsequence_with_k([10, 20, 30, 40, 50], 10) == 2
    assert longest_increasing_subsequence_with_k([1, 2, 3, 4, 5], 0) == 1
    assert longest_increasing_subsequence_with_k([], 5) == 0
    assert longest_increasing_subsequence_with_k([1], 5) == 1
    assert longest_increasing_subsequence_with_k([1,1,1,1,1], 1) == 1
    assert longest_increasing_subsequence_with_k([1, 3, 2, 4, 5], 2) == 3
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()