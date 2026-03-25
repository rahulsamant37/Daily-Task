# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums`, find the length of the longest increasing subsequence where the difference between consecutive elements in the subsequence is exactly 1.

Example:
Input: nums = [3, 10, 3, 4, 2, 1, 2, 3, 4, 5]
Output: 5
Explanation: The longest increasing subsequence with difference 1 is [1, 2, 3, 4, 5].

Input: nums = [1, 2, 3, 5, 6, 7, 9]
Output: 3
Explanation: The longest increasing subsequence with difference 1 is [1, 2, 3] or [5, 6, 7].

Input: nums = [1, 5, 6, 7, 8, 9]
Output: 4
Explanation: The longest increasing subsequence with difference 1 is [5, 6, 7, 8] or [6, 7, 8, 9].
'''

# Solution
def longest_increasing_subsequence_with_difference_one(nums):
    """
    Finds the length of the longest increasing subsequence where the difference
    between consecutive elements in the subsequence is exactly 1.

    Args:
        nums: A list of integers.

    Returns:
        The length of the longest increasing subsequence with difference 1.
    """

    # Create a dictionary to store the length of the longest increasing
    # subsequence ending at each number.
    dp = {}

    # Iterate over the numbers in the input array.
    for num in nums:
        # If the number is already in the dictionary, we update its length.
        # Otherwise, we add it to the dictionary with a length of 1.
        if num - 1 in dp:
            dp[num] = dp[num - 1] + 1
        else:
            dp[num] = 1

    # Return the maximum length of any increasing subsequence.
    return max(dp.values()) if dp else 0


# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_difference_one([3, 10, 3, 4, 2, 1, 2, 3, 4, 5]) == 5
    assert longest_increasing_subsequence_with_difference_one([1, 2, 3, 5, 6, 7, 9]) == 3
    assert longest_increasing_subsequence_with_difference_one([1, 5, 6, 7, 8, 9]) == 4
    assert longest_increasing_subsequence_with_difference_one([1]) == 1
    assert longest_increasing_subsequence_with_difference_one([]) == 0
    assert longest_increasing_subsequence_with_difference_one([5, 4, 3, 2, 1]) == 1
    assert longest_increasing_subsequence_with_difference_one([1, 2, 2, 3, 4, 4, 5]) == 4

if __name__ == "__main__":
    test_solution()