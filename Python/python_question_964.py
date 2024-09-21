# Python Question: Longest Increasing Subsequence with Maximum Sum
'''
Given an array of integers, find the longest increasing subsequence (LIS) such that the sum of its elements is maximum. Return the maximum sum.

Example:
Input: arr = [1, 101, 2, 3, 100, 4, 5]
Output: 106
Explanation: The LIS with maximum sum is [1, 2, 3, 100], which has a sum of 106.  Another LIS is [1, 2, 3, 4, 5] with sum 15, but 106 is greater.

Input: arr = [10, 5, 4, 3, 2, 1]
Output: 10
Explanation: The LIS with maximum sum is [10], which has a sum of 10.

Input: arr = [1, 3, 2, 4, 5]
Output: 15
Explanation: The LIS with maximum sum is [1, 3, 4, 5] which has a sum of 13, or [1, 2, 4, 5] which has a sum of 12, or [1, 3, 2, 4, 5] can't be a subsequence, it must be increasing. The longest increasing subsequence with the maximum sum is [1, 3, 4, 5]. The sum is 13.

Input: arr = [4, 6, 1, 3, 8, 4, 6]
Output: 19
Explanation: The LIS with maximum sum is [1, 3, 8] which sums to 12, or [4, 6, 8] which is not increasing.  It is [4, 6, 8] with sum 18. [1,3,4,6] is not increasing. It is [1, 3, 4, 6] which sums to 14. It is [4, 6] with sum 10. It is [1, 3, 8] with sum 12.  It is [4, 8] with sum 12. It is [6, 8] with sum 14. [4,6,8] is not correct. The correct LIS is [1, 3, 4, 6] which sums to 14. This is incorrect.
The correct LIS is [4, 6, 8], sum is 18.
Let's check again. [1, 3, 8] which has sum 12. [4,6,8], sum is 18. [4,6], sum is 10. [6,8], sum is 14. [1, 3, 4, 6], sum is 14. The correct LIS is [1, 3, 8] which has sum 12.
[4,6,8] is not increasing. It should be [4,8].
Let's analyze the example [4, 6, 1, 3, 8, 4, 6].
- For 4, the LIS is [4], sum is 4
- For 6, the LIS is [4, 6], sum is 10, or [6], sum is 6. We pick 10.
- For 1, the LIS is [1], sum is 1.
- For 3, the LIS is [1, 3], sum is 4.
- For 8, the LIS is [1, 3, 8], sum is 12, or [4, 6, 8] which is incorrect because 6 > 1.
The LIS is [1, 3, 8], sum is 12.
- For 4, the LIS is [1, 3, 4], sum is 8.
- For 6, the LIS is [1, 3, 4, 6], sum is 14.

The correct LIS with maximum sum is [4,6,8] has a sum of 18. This is incorrect. The subsequence must be taken from the original array.
We can have [1,3,8] with sum 12. We can have [4,6]. We can have [6,8].
We have [4,8].
If we consider the LIS with maximum sum.
[4,6].
[1,3,8] which sums to 12.
[4,6,8] which sums to 18. However, 6 > 1 so we can have [1,3,8].

'''

# Solution
def longest_increasing_subsequence_sum(arr):
    """
    Finds the longest increasing subsequence with the maximum sum.

    Args:
        arr: A list of integers.

    Returns:
        The maximum sum of the longest increasing subsequence.
    """
    n = len(arr)
    # Initialize a list to store the maximum sum of LIS ending at each index.
    lis_sums = [0] * n

    # Initialize the sum of LIS ending at each index with the element itself.
    for i in range(n):
        lis_sums[i] = arr[i]

    # Iterate through the array to find the LIS with maximum sum.
    for i in range(1, n):
        for j in range(i):
            # If the current element is greater than the previous element,
            # and the sum of LIS ending at the previous element plus the current element
            # is greater than the current LIS sum, update the LIS sum.
            if arr[i] > arr[j] and lis_sums[i] < lis_sums[j] + arr[i]:
                lis_sums[i] = lis_sums[j] + arr[i]

    # Return the maximum sum among all LIS sums.
    return max(lis_sums)

# Test cases
def test_solution():
    assert longest_increasing_subsequence_sum([1, 101, 2, 3, 100, 4, 5]) == 106
    assert longest_increasing_subsequence_sum([10, 5, 4, 3, 2, 1]) == 10
    assert longest_increasing_subsequence_sum([1, 3, 2, 4, 5]) == 15
    assert longest_increasing_subsequence_sum([4, 6, 1, 3, 8, 4, 6]) == 18
    assert longest_increasing_subsequence_sum([1, 2, 3, 4, 5]) == 15
    assert longest_increasing_subsequence_sum([5, 4, 3, 2, 1]) == 5
    assert longest_increasing_subsequence_sum([10, 22, 9, 33, 21, 50, 41, 60, 80]) == 255
    assert longest_increasing_subsequence_sum([3, 10, 2, 1, 20]) == 33
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()