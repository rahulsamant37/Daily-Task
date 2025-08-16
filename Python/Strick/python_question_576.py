# Python Question: Find the Longest Increasing Subsequence with Difference 1
'''
Given an array of integers `arr`, find the length of the longest increasing subsequence where the difference between consecutive elements is exactly 1.

Example:
Input: arr = [3, 10, 3, 11, 4, 5, 6, 7, 8, 12]
Output: 6
Explanation: The longest increasing subsequence with a difference of 1 is [3, 4, 5, 6, 7, 8]. Its length is 6.

Input: arr = [1, 2, 3, 4, 5]
Output: 5

Input: arr = [5, 4, 3, 2, 1]
Output: 1
'''

# Solution
def solution():
    def longest_increasing_subsequence_with_difference_one(arr):
        """
        Finds the length of the longest increasing subsequence with a difference of 1.

        Args:
            arr: A list of integers.

        Returns:
            The length of the longest increasing subsequence with a difference of 1.
        """
        if not arr:
            return 0

        # dp[i] stores the length of the longest increasing subsequence ending at arr[i]
        dp = {}

        max_len = 0
        for num in arr:
            # If the number before the current number exists in the sequence
            if num - 1 in dp:
                dp[num] = dp[num - 1] + 1  # Extend the existing subsequence
            else:
                dp[num] = 1  # Start a new subsequence

            max_len = max(max_len, dp[num])

        return max_len
    
    return longest_increasing_subsequence_with_difference_one
    

# Test cases
def test_solution():
    lis_diff_one = solution()

    # Test case 1
    arr1 = [3, 10, 3, 11, 4, 5, 6, 7, 8, 12]
    expected1 = 6
    assert lis_diff_one(arr1) == expected1, f"Test Case 1 Failed: Expected {expected1}, Got {lis_diff_one(arr1)}"

    # Test case 2
    arr2 = [1, 2, 3, 4, 5]
    expected2 = 5
    assert lis_diff_one(arr2) == expected2, f"Test Case 2 Failed: Expected {expected2}, Got {lis_diff_one(arr2)}"

    # Test case 3
    arr3 = [5, 4, 3, 2, 1]
    expected3 = 1
    assert lis_diff_one(arr3) == expected3, f"Test Case 3 Failed: Expected {expected3}, Got {lis_diff_one(arr3)}"

    # Test case 4
    arr4 = []
    expected4 = 0
    assert lis_diff_one(arr4) == expected4, f"Test Case 4 Failed: Expected {expected4}, Got {lis_diff_one(arr4)}"
    
    # Test case 5
    arr5 = [1, 1, 1, 1]
    expected5 = 1
    assert lis_diff_one(arr5) == expected5, f"Test Case 5 Failed: Expected {expected5}, Got {lis_diff_one(arr5)}"

    # Test case 6
    arr6 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    expected6 = 1
    assert lis_diff_one(arr6) == expected6, f"Test Case 6 Failed: Expected {expected6}, Got {lis_diff_one(arr6)}"

    # Test case 7
    arr7 = [1, 3, 5, 7, 9]
    expected7 = 1
    assert lis_diff_one(arr7) == expected7, f"Test Case 7 Failed: Expected {expected7}, Got {lis_diff_one(arr7)}"
    
    # Test case 8
    arr8 = [1, 2, 1, 2, 3, 2, 3, 4]
    expected8 = 4
    assert lis_diff_one(arr8) == 4, f"Test Case 8 Failed: Expected {4}, Got {lis_diff_one(arr8)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()