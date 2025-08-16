# Python Question: Longest Increasing Subsequence with Difference 1
'''
Given an array of integers, find the length of the longest subsequence such that all elements of the subsequence are sorted in increasing order, and the difference between adjacent elements is exactly 1.

Example:
Input: arr = [3, 10, 3, 11, 4, 5, 6, 7, 8, 12]
Output: 6
Explanation: The longest subsequence is [3, 4, 5, 6, 7, 8]
'''

# Solution
def longest_increasing_subsequence_with_difference_1(arr):
    """
    Finds the length of the longest increasing subsequence with a difference of 1.

    Args:
        arr: A list of integers.

    Returns:
        The length of the longest increasing subsequence with a difference of 1.
    """

    # Create a dictionary to store the length of the longest subsequence ending at each number.
    # Key: number in the array
    # Value: length of the longest subsequence ending at that number
    dp = {}

    # Iterate through the array
    for num in arr:
        # If the number - 1 exists in the dictionary, then we can extend the subsequence ending at number - 1.
        if num - 1 in dp:
            dp[num] = dp[num - 1] + 1
        # Otherwise, we start a new subsequence of length 1.
        else:
            dp[num] = 1

    # Return the maximum value in the dictionary.
    return max(dp.values()) if dp else 0

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_difference_1([3, 10, 3, 11, 4, 5, 6, 7, 8, 12]) == 6
    assert longest_increasing_subsequence_with_difference_1([1, 2, 3, 4, 5]) == 5
    assert longest_increasing_subsequence_with_difference_1([5, 4, 3, 2, 1]) == 1
    assert longest_increasing_subsequence_with_difference_1([1, 3, 5, 7, 9]) == 1
    assert longest_increasing_subsequence_with_difference_1([1, 2, 1, 2, 3, 2, 3, 4]) == 4
    assert longest_increasing_subsequence_with_difference_1([]) == 0
    assert longest_increasing_subsequence_with_difference_1([1]) == 1
    assert longest_increasing_subsequence_with_difference_1([1,1,1,1]) == 1
    assert longest_increasing_subsequence_with_difference_1([1, 2, 3, 5, 6, 7]) == 3

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()