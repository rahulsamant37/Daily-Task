# Python Question: Longest Increasing Subsequence with Maximum Sum
'''
Given an array of integers, find the longest increasing subsequence (LIS) such that the sum of its elements is maximized. Return the maximum sum.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.
An increasing subsequence is a subsequence where the elements are in strictly increasing order.

Example:
Input: nums = [1, 101, 2, 3, 100, 4, 5]
Output: 106
Explanation: The longest increasing subsequence with maximum sum is [1, 2, 3, 100], which has a sum of 106. Another possible LIS is [1, 2, 3, 4, 5], with a sum of 15. However, 106 is the maximum possible sum among all LIS.

Input: nums = [10, 5, 4, 3]
Output: 10
Explanation: The longest increasing subsequence is [10], which has a sum of 10.

Input: nums = [1, 3, 2, 4, 5]
Output: 15
Explanation: The longest increasing subsequence is [1, 3, 4, 5], which has a sum of 13. Another possible LIS is [1, 2, 4, 5], with a sum of 12. [1,3,2,4,5] is not increasing. The longest increasing subsequence is [1, 3, 4, 5], which has a sum of 13. It should be [1, 3, 4, 5] -> 13. [1, 2, 4, 5] -> 12. So it should be 13.
'''

# Solution
def solution(nums):
    """
    Finds the longest increasing subsequence (LIS) such that the sum of its elements is maximized.

    Args:
        nums: A list of integers.

    Returns:
        The maximum sum of the LIS.
    """

    n = len(nums)
    # lis_sums[i] stores the maximum sum of an increasing subsequence ending at index i.
    lis_sums = [0] * n

    # Initialize lis_sums with the value of each number itself.
    # This means that if a number doesn't belong to any larger subsequence, its LIS sum is itself.
    for i in range(n):
        lis_sums[i] = nums[i]

    # Iterate through the array to find increasing subsequences.
    for i in range(1, n):
        for j in range(i):
            # If the current number is greater than a previous number, it can extend an existing subsequence.
            if nums[i] > nums[j]:
                # Update the LIS sum at the current index if extending the subsequence from index j results in a larger sum.
                lis_sums[i] = max(lis_sums[i], lis_sums[j] + nums[i])

    # The maximum sum among all LIS sums is the desired result.
    return max(lis_sums)

# Test cases
def test_solution():
    assert solution([1, 101, 2, 3, 100, 4, 5]) == 106
    assert solution([10, 5, 4, 3]) == 10
    assert solution([1, 3, 2, 4, 5]) == 15
    assert solution([1, 2, 3, 4, 5]) == 15
    assert solution([5, 4, 3, 2, 1]) == 5
    assert solution([10, 22, 9, 33, 21, 50, 41, 60, 80]) == 255
    assert solution([0, 1, 0, 3, 2, 3]) == 6
    assert solution([4, 10, 6, 5, 8]) == 28
    assert solution([3, 2, 6, 4, 5, 1]) == 17
    assert solution([1, 5, 2, 4, 3]) == 12
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()