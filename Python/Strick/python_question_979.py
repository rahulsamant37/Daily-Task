# Python Question: Maximum Subarray Sum with K Concatenations
'''
Given an array `arr` of integers and an integer `k`, you need to find the maximum possible sum of a subarray of the given array after concatenating the array `k` times.

For example, if `arr = [1, -2, 1]` and `k = 3`, the concatenated array would be `[1, -2, 1, 1, -2, 1, 1, -2, 1]`.  You need to find the maximum sum of any contiguous subarray within this concatenated array.

Input:
arr: A list of integers.
k: An integer representing the number of concatenations.

Output:
The maximum subarray sum after k concatenations.

Constraints:
1 <= len(arr) <= 10^5
-10^4 <= arr[i] <= 10^4
1 <= k <= 10^5

Example:
Input: arr = [1, 2, 3], k = 2
Output: 12
Explanation: The concatenated array is [1, 2, 3, 1, 2, 3]. The maximum subarray is [1, 2, 3, 1, 2, 3] with a sum of 12.

Input: arr = [-1, -2], k = 2
Output: -1
Explanation: The concatenated array is [-1, -2, -1, -2]. The maximum subarray is [-1] with a sum of -1.

Input: arr = [1, -2, 1], k = 5
Output: 2
'''

# Solution
def solution(arr, k):
    """
    Calculates the maximum subarray sum after k concatenations of the array.

    Args:
        arr: A list of integers.
        k: The number of concatenations.

    Returns:
        The maximum subarray sum after k concatenations.
    """

    def max_subarray_sum(arr):
        """
        Finds the maximum subarray sum using Kadane's Algorithm.
        """
        max_so_far = float('-inf')
        current_max = 0
        for num in arr:
            current_max = max(num, current_max + num)
            max_so_far = max(max_so_far, current_max)
        return max_so_far

    n = len(arr)

    # Handle cases where k is small efficiently
    if k == 1:
        return max_subarray_sum(arr)

    if k == 2:
        extended_arr = arr + arr
        return max_subarray_sum(extended_arr)

    # Calculate the sum of the entire array
    arr_sum = sum(arr)

    # Calculate the maximum subarray sum for one concatenation
    max_sum_one = max_subarray_sum(arr)

    # If the array sum is positive, we can potentially increase the maximum subarray sum by adding more concatenations
    if arr_sum > 0:
        # Calculate the maximum subarray sum for two concatenations
        extended_arr = arr + arr
        max_sum_two = max_subarray_sum(extended_arr)

        # The maximum subarray sum for k concatenations can be calculated as:
        # max_sum_two + (k - 2) * arr_sum, but we need to take the maximum possible value
        return max(max_sum_one, max_sum_two + (k - 2) * arr_sum)
    else:
        # If the array sum is not positive, simply concatenating twice is enough
        extended_arr = arr + arr
        return max(max_sum_one, max_subarray_sum(extended_arr))


# Test cases
def test_solution():
    assert solution([1, 2, 3], 2) == 12
    assert solution([-1, -2], 2) == -1
    assert solution([1, -2, 1], 5) == 2
    assert solution([-1, 0, -2], 3) == 0
    assert solution([10, -10, 20, -10, -10], 2) == 20
    assert solution([1, -2, 1, -2], 3) == 2
    assert solution([1, -2, 1, -2], 1) == 1
    assert solution([1, -2, 1, -2], 2) == 2
    assert solution([-5, 4, -3, 5, -1], 2) == 9
    assert solution([-5, 4, -3, 5, -1], 3) == 13
    assert solution([-5, 4, -3, 5, -1], 1) == 6
    assert solution([1,2], 3) == 9
    assert solution([-1, -2, -3], 2) == -1
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()