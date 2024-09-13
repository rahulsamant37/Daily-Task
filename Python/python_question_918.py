# Python Question: Find the Longest Increasing Subsequence Length
'''
Given an array of integers, find the length of the longest strictly increasing subsequence.
A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.
For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Example:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Input: nums = [0,1,0,3,2,3]
Output: 4
Explanation: The longest increasing subsequence is [0,1,2,3], therefore the length is 4.

Input: nums = [7,7,7,7,7,7,7]
Output: 1
'''

# Solution
def solution(nums):
    """
    Finds the length of the longest increasing subsequence in a given array.

    Args:
        nums: A list of integers.

    Returns:
        The length of the longest increasing subsequence.
    """

    # tails[i] is the smallest tail of all increasing subsequences with length i+1.
    # tails is always an increasing array.
    tails = []

    # Iterate through each number in the input array.
    for num in nums:
        # If we find a number in tails that is greater than or equal to the current number,
        # we replace that number with the current number. This is because the current number
        # can potentially form a shorter increasing subsequence with the same length.
        # If no such number is found, it means the current number is greater than all numbers in tails,
        # so we extend the longest increasing subsequence by 1.
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

    # The length of tails is the length of the longest increasing subsequence.
    return len(tails)

# Test cases
def test_solution():
    assert solution([10,9,2,5,3,7,101,18]) == 4
    assert solution([0,1,0,3,2,3]) == 4
    assert solution([7,7,7,7,7,7,7]) == 1
    assert solution([1,3,6,7,9,4,10,5,6]) == 6
    assert solution([4,10,4,3,8,9]) == 3
    assert solution([2,2,2,2,2]) == 1
    assert solution([1]) == 1
    assert solution([]) == 0
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()