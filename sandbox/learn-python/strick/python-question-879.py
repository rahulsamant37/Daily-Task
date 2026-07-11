# Python Question: Longest Increasing Subsequence with Maximum Sum
'''
Given an array of integers, find the longest increasing subsequence (LIS) such that the sum of its elements is maximized. Return the maximum sum.

Example:
Input: [1, 101, 2, 3, 100, 4, 5]
Output: 106 (The LIS is [1, 2, 3, 100], and the sum is 106)

Input: [10, 5, 4, 3]
Output: 10 (The LIS is [10], and the sum is 10)

Input: [1, 3, 2, 4, 5]
Output: 15 (The LIS is [1, 3, 4, 5], and the sum is 15)
'''

# Solution
def solution(arr):
    """
    Finds the longest increasing subsequence with the maximum sum.

    Args:
        arr: A list of integers.

    Returns:
        The maximum sum of the elements in the longest increasing subsequence.
    """
    n = len(arr)

    # Initialize sums array with the same values as the input array.
    # sums[i] will store the maximum sum of an increasing subsequence ending at index i.
    sums = arr[:]

    # Iterate through the array to build up the sums array.
    for i in range(1, n):
        # Iterate through the elements before the current element.
        for j in range(i):
            # If the current element is greater than the previous element,
            # it can be added to the increasing subsequence ending at index j.
            if arr[i] > arr[j]:
                # Update the sums[i] if adding the current element to the
                # subsequence ending at index j results in a larger sum.
                sums[i] = max(sums[i], sums[j] + arr[i])

    # The maximum value in the sums array is the maximum sum of any increasing subsequence.
    return max(sums) if sums else 0

# Test cases
def test_solution():
    assert solution([1, 101, 2, 3, 100, 4, 5]) == 106
    assert solution([10, 5, 4, 3]) == 10
    assert solution([1, 3, 2, 4, 5]) == 15
    assert solution([1, 2, 3, 4, 5]) == 15
    assert solution([5, 4, 3, 2, 1]) == 5
    assert solution([1]) == 1
    assert solution([]) == 0
    assert solution([1, 1, 1, 1, 1]) == 1
    assert solution([10, 22, 9, 33, 21, 50, 41, 60, 80]) == 255
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()