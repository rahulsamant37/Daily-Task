# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence where the difference between consecutive elements in the subsequence is exactly `diff`.

Example:
Input: nums = [3, 0, 3, 2, 4, 5], diff = 1
Output: 3
Explanation: The longest increasing subsequence with a difference of 1 is [2, 3, 4] or [3, 4, 5], with a length of 3.

Input: nums = [1, 5, 7, 8, 5, 3, 4, 2, 1], diff = -2
Output: 4
Explanation: The longest increasing subsequence with a difference of -2 is [8, 6, 4, 2] which is [8, 5, 3, 1] in the input array, with a length of 4. Note that 6 is not present but it is just to express the difference.

Input: nums = [4, 12, 10, 0, -2, 10, 8, -9, 5, -1, 3, -6], diff = -6
Output: 5
Explanation: The longest increasing subsequence with a difference of -6 is [12, 6, 0, -6, -12] which is [12, 0, -6] in the input array, with a length of 3. Another one is [10, 4, -2, -8, -14] which is [10, 4, -2] in the input array, with a length of 3. The longest one is [10, 4, -2, -8, -14] which maps to [10, 4, -2, -8, -14] and we have [10, 4, -2, -8, -14]. We can also have [5, -1, -7, -13, -19]. The longest subsequence is [4, -2, -8, -14, -20] which is [4, -2] with length 2.
'''

# Solution
def longest_arithmetic_subsequence(nums, diff):
    """
    Finds the length of the longest increasing subsequence with a specific difference.

    Args:
        nums: A list of integers.
        diff: The difference between consecutive elements in the subsequence.

    Returns:
        The length of the longest increasing subsequence.
    """
    # dp[num] stores the length of the longest arithmetic subsequence ending with num
    dp = {}

    max_len = 0
    for num in nums:
        # If num - diff exists in the dp table, it means we can extend the subsequence
        if num - diff in dp:
            dp[num] = dp[num - diff] + 1
        # Otherwise, this is the start of a new subsequence of length 1
        else:
            dp[num] = 1
        # Update the maximum length found so far
        max_len = max(max_len, dp[num])

    return max_len

# Test cases
def test_solution():
    nums1 = [3, 0, 3, 2, 4, 5]
    diff1 = 1
    assert longest_arithmetic_subsequence(nums1, diff1) == 3

    nums2 = [1, 5, 7, 8, 5, 3, 4, 2, 1]
    diff2 = -2
    assert longest_arithmetic_subsequence(nums2, diff2) == 4

    nums3 = [4, 12, 10, 0, -2, 10, 8, -9, 5, -1, 3, -6]
    diff3 = -6
    assert longest_arithmetic_subsequence(nums3, diff3) == 2

    nums4 = [1,2,3,4]
    diff4 = 1
    assert longest_arithmetic_subsequence(nums4, diff4) == 4

    nums5 = [1,3,5,7]
    diff5 = 2
    assert longest_arithmetic_subsequence(nums5, diff5) == 4

    nums6 = [1,5,9,13]
    diff6 = 4
    assert longest_arithmetic_subsequence(nums6, diff6) == 4

    nums7 = [1, 2, 3, 4, 5, 6]
    diff7 = 2
    assert longest_arithmetic_subsequence(nums7, diff7) == 3

    nums8 = [1,5,7,8,5,3,4,2,1]
    diff8 = 0
    assert longest_arithmetic_subsequence(nums8, diff8) == 2

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()