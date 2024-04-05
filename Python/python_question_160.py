# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) of `nums` with the following constraint:

For any two consecutive elements `nums[i]` and `nums[j]` in the subsequence (where `i < j`), the absolute difference between their indices in the original array must be less than or equal to `k`. In other words, `j - i <= k`.

Example:
Input: nums = [1, 3, 2, 4, 5], k = 2
Output: 4
Explanation: The longest increasing subsequence satisfying the constraint is [1, 2, 4, 5]. The indices are [0, 2, 3, 4] and the difference between consecutive indices is at most 2.

Input: nums = [10, 22, 9, 33, 21, 50, 41, 60, 80], k = 3
Output: 6
Explanation: The longest increasing subsequence satisfying the constraint is [10, 22, 33, 50, 60, 80]. The indices are [0, 1, 3, 5, 7, 8] and the difference between consecutive indices is at most 3.

Input: nums = [5, 4, 3, 2, 1], k = 1
Output: 1
Explanation: The longest increasing subsequence satisfying the constraint is any single element.
'''

# Solution
def longest_increasing_subsequence_with_k(nums, k):
    """
    Finds the length of the longest increasing subsequence (LIS) of nums with the constraint that the absolute difference between the indices of consecutive elements in the subsequence is at most k.

    Args:
        nums: A list of integers.
        k: An integer representing the maximum allowed difference between indices.

    Returns:
        The length of the longest increasing subsequence.
    """
    n = len(nums)
    if n == 0:
        return 0

    # dp[i] stores the length of the longest increasing subsequence ending at index i.
    dp = [1] * n

    # Iterate through the array to build the dp array.
    for i in range(1, n):
        # Iterate through the elements before index i.
        for j in range(i):
            # Check if nums[i] can extend the LIS ending at index j.
            if nums[i] > nums[j] and (i - j <= k):
                # Update dp[i] if extending the LIS at j gives a longer sequence.
                dp[i] = max(dp[i], dp[j] + 1)

    # The maximum value in the dp array is the length of the LIS.
    return max(dp)

# Test cases
def test_solution():
    nums1 = [1, 3, 2, 4, 5]
    k1 = 2
    assert longest_increasing_subsequence_with_k(nums1, k1) == 4

    nums2 = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    k2 = 3
    assert longest_increasing_subsequence_with_k(nums2, k2) == 6

    nums3 = [5, 4, 3, 2, 1]
    k3 = 1
    assert longest_increasing_subsequence_with_k(nums3, k3) == 1

    nums4 = [1, 2, 3, 4, 5]
    k4 = 1
    assert longest_increasing_subsequence_with_k(nums4, k4) == 2

    nums5 = [1, 2, 3, 4, 5]
    k5 = 4
    assert longest_increasing_subsequence_with_k(nums5, k5) == 5

    nums6 = []
    k6 = 5
    assert longest_increasing_subsequence_with_k(nums6, k6) == 0

    nums7 = [7]
    k7 = 1
    assert longest_increasing_subsequence_with_k(nums7, k7) == 1

    nums8 = [1, 5, 2, 4, 3]
    k8 = 2
    assert longest_increasing_subsequence_with_k(nums8, k8) == 3

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()