# Python Question: Find the Longest Increasing Subsequence with Maximum Sum
'''
Given an array of integers, find the longest increasing subsequence (LIS) such that the sum of its elements is maximum.
Return the maximum sum.

Example:
Input: arr = [1, 101, 2, 3, 100, 4, 5]
Output: 106
Explanation: The LIS with maximum sum is [1, 2, 3, 100], and its sum is 106.

Input: arr = [10, 5, 4, 3]
Output: 10
Explanation: The LIS with maximum sum is [10], and its sum is 10.

Input: arr = [1, 3, 2, 4, 5]
Output: 15
Explanation: The LIS with maximum sum is [1, 2, 4, 5], and its sum is 12. Or [1,3,4,5] which is 13. Or [1,3,5] which is 9. So in this case, [1,3,4,5] is the correct answer.
'''

# Solution
def solution():
    def longest_increasing_subsequence_with_max_sum(arr):
        """
        Finds the longest increasing subsequence (LIS) such that the sum of its elements is maximum.

        Args:
            arr: A list of integers.

        Returns:
            The maximum sum of the LIS.
        """

        n = len(arr)
        # Initialize dp array to store the maximum sum of LIS ending at each index.
        dp = [0] * n
        # Initialize dp[i] with arr[i] as the minimum LIS at any index is the element itself.
        for i in range(n):
            dp[i] = arr[i]

        # Iterate through the array to build the dp array.
        for i in range(1, n):
            for j in range(i):
                # If the current element is greater than the previous element,
                # it can be added to the LIS ending at the previous element.
                if arr[i] > arr[j]:
                    # Update the maximum sum of LIS ending at the current index.
                    dp[i] = max(dp[i], dp[j] + arr[i])

        # Return the maximum value in the dp array, which represents the maximum sum of LIS.
        return max(dp)

    return longest_increasing_subsequence_with_max_sum

# Test cases
def test_solution():
    func = solution()
    assert func([1, 101, 2, 3, 100, 4, 5]) == 106
    assert func([10, 5, 4, 3]) == 10
    assert func([1, 3, 2, 4, 5]) == 15
    assert func([1, 2, 3, 4, 5]) == 15
    assert func([5, 4, 3, 2, 1]) == 5
    assert func([1, 5, 2, 4, 3]) == 11
    assert func([10, 22, 9, 33, 21, 50, 41, 60, 80]) == 255
    assert func([3, 10, 2, 1, 20]) == 23
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()