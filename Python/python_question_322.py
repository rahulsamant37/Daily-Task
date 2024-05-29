# Python Question: Longest Increasing Subsequence with Minimum Last Element
'''
Given an array of integers `nums`, find the length of the longest increasing subsequence (LIS).
If there are multiple LIS with the same length, return the one with the minimum last element.
For example, if there are two LIS of length 3, [1, 3, 5] and [1, 2, 4], return 3 (the length).

Example:
Input: nums = [1, 3, 2, 4, 5]
Output: 5
Explanation: The longest increasing subsequence is [1, 2, 4, 5].

Input: nums = [1, 3, 2, 4, 5, 2, 3]
Output: 5
Explanation: The longest increasing subsequence is [1, 2, 3].

Input: nums = [10, 9, 2, 5, 3, 7, 101, 18]
Output: 18
Explanation: The longest increasing subsequence is [2, 3, 7, 18].

Input: nums = [4, 10, 4, 3, 8, 9]
Output: 9
Explanation: The longest increasing subsequence is [4, 8, 9] or [3, 8, 9].

Input: nums = [5,4,3,2,1]
Output: 1
Explanation: The longest increasing subsequence is [1] or [2] or ... [5].

'''

# Solution
def solution(nums):
    """
    Finds the length of the longest increasing subsequence (LIS) and returns the minimum last element of the LIS.
    If there are multiple LIS with the same length, return the one with the minimum last element.

    Args:
      nums: A list of integers.

    Returns:
      The minimum last element of the LIS.
    """

    if not nums:
        return 0

    tails = []  # tails[i] is the smallest tail of all increasing subsequences with length i+1.

    for num in nums:
        # If we find a number in tails that is greater than or equal to the current number,
        # we replace that number with the current number. This is because the current number
        # can extend the LIS with a smaller tail, which is better.
        # If we don't find such a number, it means the current number is greater than all numbers in tails,
        # which means we can extend the LIS by 1.

        l, r = 0, len(tails)
        while l < r:
            mid = (l + r) // 2
            if tails[mid] < num:
                l = mid + 1
            else:
                r = mid

        if l == len(tails):
            tails.append(num)
        else:
            tails[l] = num

    return tails[-1]


# Test cases
def test_solution():
    assert solution([1, 3, 2, 4, 5]) == 5
    assert solution([1, 3, 2, 4, 5, 2, 3]) == 3
    assert solution([10, 9, 2, 5, 3, 7, 101, 18]) == 18
    assert solution([4, 10, 4, 3, 8, 9]) == 9
    assert solution([5,4,3,2,1]) == 1
    assert solution([1,2,3,4,5]) == 5
    assert solution([1]) == 1
    assert solution([]) == 0
    assert solution([2,2,2,2,2]) == 2
    assert solution([1, 5, 2, 4, 3]) == 3
    assert solution([0, 1, 0, 3, 2, 3]) == 3

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()