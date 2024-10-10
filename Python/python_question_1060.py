# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence where the difference between consecutive elements is exactly `k`.

Example:
Input: nums = [3, 10, 3, 11, 4, 5, 6, 7, 8, 9], k = 1
Output: 6
Explanation: The longest increasing subsequence with a difference of 1 is [4, 5, 6, 7, 8, 9], which has a length of 6.

Input: nums = [4, 12, 10, 0, -2, 10, 7, -8, 9, -9, -1, -3, 4, -5, -6], k = -2
Output: 4
Explanation: The longest increasing subsequence with a difference of -2 is [4, 2, 0, -2], or [0, -2, -4, -6], or [7, 5, 3, 1] after adding 2 repeatedly, etc. The length is 4.
'''

# Solution
def longest_increasing_subsequence_with_difference(nums, k):
    """
    Finds the length of the longest increasing subsequence with a specific difference k.

    Args:
        nums: A list of integers.
        k: The required difference between consecutive elements.

    Returns:
        The length of the longest increasing subsequence with difference k.
    """

    # Use a dictionary to store the length of the longest increasing subsequence ending at each number.
    dp = {}  # dp[num] = length of longest increasing subsequence ending at num

    max_len = 0  # Initialize the maximum length to 0

    for num in nums:
        # If num - k is already in the dictionary, it means we can extend an existing subsequence.
        if num - k in dp:
            dp[num] = dp[num - k] + 1  # Extend the subsequence ending at num - k
        else:
            dp[num] = 1  # Start a new subsequence with length 1

        max_len = max(max_len, dp[num])  # Update the maximum length

    return max_len  # Return the maximum length found


# Test cases
def test_solution():
    nums1 = [3, 10, 3, 11, 4, 5, 6, 7, 8, 9]
    k1 = 1
    expected1 = 6
    assert longest_increasing_subsequence_with_difference(nums1, k1) == expected1

    nums2 = [4, 12, 10, 0, -2, 10, 7, -8, 9, -9, -1, -3, 4, -5, -6]
    k2 = -2
    expected2 = 4
    assert longest_increasing_subsequence_with_difference(nums2, k2) == expected2

    nums3 = [1, 2, 3, 4, 5]
    k3 = 1
    expected3 = 5
    assert longest_increasing_subsequence_with_difference(nums3, k3) == expected3

    nums4 = [5, 4, 3, 2, 1]
    k4 = -1
    expected4 = 5
    assert longest_increasing_subsequence_with_difference(nums4, k4) == expected4

    nums5 = [1, 5, 1, 5, 1, 5]
    k5 = 4
    expected5 = 2
    assert longest_increasing_subsequence_with_difference(nums5, k5) == expected5

    nums6 = [1, 2, 3, 4, 5]
    k6 = 2
    expected6 = 3
    assert longest_increasing_subsequence_with_difference(nums6, k6) == 3

    nums7 = []
    k7 = 1
    expected7 = 0
    assert longest_increasing_subsequence_with_difference(nums7, k7) == 0

    nums8 = [1]
    k8 = 1
    expected8 = 1
    assert longest_increasing_subsequence_with_difference(nums8, k8) == 1

    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()