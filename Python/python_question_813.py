# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence where the difference between consecutive elements is exactly `diff`.

Example:
Input: nums = [3, 0, 3, 4, 5, 6], diff = 3
Output: 4
Explanation: The longest increasing subsequence with a difference of 3 is [0, 3, 6], which has length 3. Another one is [3, 6] which has length 2. Another possible sequence is [3, 3, 6] with length 3 (3 appearing twice). We need to find the longest possible subsequence. Another possible sequence is [3,0,3,6] which is not valid. Another possible sequence is [3,4,5,6] which is not valid. The sequence [3, 3, 4, 5, 6] is not valid since the difference between consecutive elements needs to be exactly diff. Another valid sequence is [3,6] of length 2. Another valid sequence is [0,3,6] of length 3. The longest valid sequence is [3, 0, 3, 6] which is not valid. The longest subsequence is [3, 0, 3, 4, 5, 6]. The valid subsequences are [3,6], [0,3,6].
However, if nums = [1,5,7,8,5,3,4,2,1] and diff = -2, the answer is 4 since [7,5,3,1] is a valid subsequence.

Input: nums = [1, 2, 3, 4, 5], diff = 1
Output: 5

Input: nums = [1, 3, 5, 7], diff = 2
Output: 4

Input: nums = [1, 5, 7, 8, 5, 3, 4, 2, 1], diff = -2
Output: 4
'''

# Solution
def longest_increasing_subsequence_with_difference(nums, diff):
    """
    Finds the length of the longest increasing subsequence with a specific difference.

    Args:
        nums: A list of integers.
        diff: The difference between consecutive elements in the subsequence.

    Returns:
        The length of the longest increasing subsequence.
    """

    # dp[num] stores the length of the longest increasing subsequence ending with num
    dp = {}

    max_len = 0

    for num in nums:
        # If num - diff exists in dp, it means we can extend the subsequence
        if num - diff in dp:
            dp[num] = dp[num - diff] + 1
        else:
            # Otherwise, the subsequence ending with num has length 1
            dp[num] = 1

        # Update the maximum length
        max_len = max(max_len, dp[num])

    return max_len

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_difference([3, 0, 3, 4, 5, 6], 3) == 4
    assert longest_increasing_subsequence_with_difference([1, 2, 3, 4, 5], 1) == 5
    assert longest_increasing_subsequence_with_difference([1, 3, 5, 7], 2) == 4
    assert longest_increasing_subsequence_with_difference([1, 5, 7, 8, 5, 3, 4, 2, 1], -2) == 4
    assert longest_increasing_subsequence_with_difference([4,12,10,0,-2,7,-8,9,-9,-12,-3,10,10,6,0,4,-1,-5,13,-14,7,12,-6,14,15,3,-12,10,11,0], 8) == 2
    assert longest_increasing_subsequence_with_difference([1,6,4,5,3,3,7,3,5,7,6,5,4,5,3,6,8,4,8,8,0,6,3,1,0,3,8,2,3,3,2,4,5,3,3,0,7,2,3,5,4,2,4,0,5,8,2,8,0,6], 2) == 2
    assert longest_increasing_subsequence_with_difference([9,8,7,6,5,4,3,2,1], -1) == 9
    assert longest_increasing_subsequence_with_difference([1, 2, 3, 4, 5], 2) == 3
    assert longest_increasing_subsequence_with_difference([1, 3, 5, 2, 4, 6], 2) == 3

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()