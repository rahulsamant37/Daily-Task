# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums`, find the length of the longest increasing subsequence (LIS) with a twist. The "twist" is that you can only append to the subsequence if the new element is strictly greater than the *last* element in the subsequence *and* the *index* of the new element in the original array is strictly greater than the *index* of the last element in the subsequence.

For example:
Input: nums = [10, 9, 2, 5, 3, 7, 101, 18]
Output: 4
Explanation: The longest increasing subsequence is [2, 3, 7, 101], where their indices are [2, 4, 5, 6] respectively.

Input: nums = [0, 1, 0, 3, 2, 3]
Output: 4
Explanation: One possible LIS is [0, 1, 2, 3]

Input: nums = [10,22,9,33,21,50,41,60,80]
Output: 6
Explanation: One possible LIS is [10, 22, 33, 50, 60, 80]
'''

# Solution
def longest_increasing_subsequence_with_index(nums):
    """
    Calculates the length of the longest increasing subsequence with index constraints.

    Args:
        nums: A list of integers.

    Returns:
        The length of the longest increasing subsequence.
    """
    n = len(nums)
    if n == 0:
        return 0

    # dp[i] stores the length of the longest increasing subsequence ending at nums[i]
    dp = [1] * n

    # Iterate through the array to build the dp table
    for i in range(1, n):
        for j in range(i):
            # Check if we can append nums[i] to the subsequence ending at nums[j]
            if nums[i] > nums[j] and i > j:
                # If we can, update dp[i] if appending results in a longer subsequence
                dp[i] = max(dp[i], dp[j] + 1)

    # The maximum value in the dp table is the length of the LIS
    return max(dp)

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_index([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert longest_increasing_subsequence_with_index([0, 1, 0, 3, 2, 3]) == 4
    assert longest_increasing_subsequence_with_index([10,22,9,33,21,50,41,60,80]) == 6
    assert longest_increasing_subsequence_with_index([1, 3, 6, 7, 9, 4, 10, 5, 6]) == 6
    assert longest_increasing_subsequence_with_index([5, 4, 3, 2, 1]) == 1
    assert longest_increasing_subsequence_with_index([1, 2, 3, 4, 5]) == 5
    assert longest_increasing_subsequence_with_index([]) == 0
    assert longest_increasing_subsequence_with_index([1]) == 1
    assert longest_increasing_subsequence_with_index([1, 1, 1, 1, 1]) == 1
    assert longest_increasing_subsequence_with_index([2, 1, 5, 3, 6, 4, 8, 7]) == 5
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()