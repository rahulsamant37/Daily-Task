# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums`, find the length of the longest increasing subsequence (LIS) with the following constraint:
For any two consecutive numbers `nums[i]` and `nums[j]` (where i < j) in the subsequence, the absolute difference between their indices in the original array must be less than or equal to a given integer `k`.
In other words, if `nums[i]` and `nums[j]` are consecutive elements in the LIS, then `j - i <= k`.

Example:
Input: nums = [10, 22, 9, 33, 21, 50, 41, 60, 80], k = 3
Output: 6
Explanation: The longest increasing subsequence is [10, 22, 33, 50, 60, 80].
(10 at index 0, 22 at index 1, 33 at index 3, 50 at index 5, 60 at index 7, 80 at index 8)
All consecutive index differences are <= 3: 1-0 <= 3, 3-1 <= 3, 5-3 <= 3, 7-5 <= 3, 8-7 <= 3

Input: nums = [1, 3, 2, 4, 5], k = 2
Output: 4
Explanation: The longest increasing subsequence is [1, 2, 4, 5].
(1 at index 0, 2 at index 2, 4 at index 3, 5 at index 4)
All consecutive index differences are <= 2: 2-0 <= 2, 3-2 <= 2, 4-3 <= 2
'''

# Solution
def longest_increasing_subsequence_with_k_constraint(nums, k):
    """
    Finds the length of the longest increasing subsequence with the given constraint.

    Args:
        nums: A list of integers.
        k: The maximum allowed difference between the indices of consecutive elements in the subsequence.

    Returns:
        The length of the longest increasing subsequence satisfying the constraint.
    """

    n = len(nums)
    if n == 0:
        return 0

    # dp[i] stores the length of the longest increasing subsequence ending at nums[i]
    dp = [1] * n

    # Iterate through the array
    for i in range(1, n):
        # For each element nums[i], check all previous elements nums[j]
        for j in range(i):
            # If nums[i] is greater than nums[j] and the index difference is within the constraint
            if nums[i] > nums[j] and (i - j) <= k:
                # Update dp[i] if adding nums[i] to the subsequence ending at nums[j]
                # results in a longer increasing subsequence.
                dp[i] = max(dp[i], dp[j] + 1)

    # The maximum value in dp is the length of the longest increasing subsequence
    return max(dp)

# Test cases
def test_solution():
    nums1 = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    k1 = 3
    assert longest_increasing_subsequence_with_k_constraint(nums1, k1) == 6

    nums2 = [1, 3, 2, 4, 5]
    k2 = 2
    assert longest_increasing_subsequence_with_k_constraint(nums2, k2) == 4

    nums3 = [1, 2, 3, 4, 5]
    k3 = 1
    assert longest_increasing_subsequence_with_k_constraint(nums3, k3) == 2

    nums4 = [5, 4, 3, 2, 1]
    k4 = 2
    assert longest_increasing_subsequence_with_k_constraint(nums4, k4) == 1

    nums5 = [1, 5, 2, 4, 3]
    k5 = 1
    assert longest_increasing_subsequence_with_k_constraint(nums5, k5) == 2

    nums6 = []
    k6 = 5
    assert longest_increasing_subsequence_with_k_constraint(nums6, k6) == 0

    nums7 = [7]
    k7 = 1
    assert longest_increasing_subsequence_with_k_constraint(nums7, k7) == 1

    nums8 = [1, 2, 3, 4, 5]
    k8 = 5
    assert longest_increasing_subsequence_with_k_constraint(nums8, k8) == 5

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()