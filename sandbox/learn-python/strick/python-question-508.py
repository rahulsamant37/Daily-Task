# Python Question: Longest Increasing Subsequence (LIS)
'''
Given an unsorted array of integers, find the length of the longest increasing subsequence (LIS).

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

An increasing subsequence is a subsequence where the elements are strictly increasing.

Example:
Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
'''

# Solution
def longest_increasing_subsequence(nums):
    """
    Finds the length of the longest increasing subsequence (LIS) in a given array.

    Args:
        nums: A list of integers.

    Returns:
        The length of the LIS.
    """
    if not nums:
        return 0

    # tails[i] is the smallest tail of all increasing subsequences with length i+1.
    tails = []

    # Iterate through each number in the input array
    for num in nums:
        # If we find a number in 'tails' that is greater than or equal to the current number,
        # we replace that number with the current number. This is because the current number
        # allows us to form an increasing subsequence of the same length but with a smaller tail,
        # which is more likely to be extended later.
        l, r = 0, len(tails)
        while l < r:
            mid = (l + r) // 2
            if tails[mid] < num:
                l = mid + 1
            else:
                r = mid

        # If the current number is greater than all numbers in 'tails', it means we can extend
        # the longest increasing subsequence by 1. We append the current number to 'tails'.
        if l == len(tails):
            tails.append(num)
        else:
            tails[l] = num  # Replace the smallest number >= num in tails with num

    # The length of 'tails' is the length of the longest increasing subsequence.
    return len(tails)

# Test cases
def test_longest_increasing_subsequence():
    assert longest_increasing_subsequence([10,9,2,5,3,7,101,18]) == 4
    assert longest_increasing_subsequence([0,1,0,3,2,3]) == 4
    assert longest_increasing_subsequence([7,7,7,7,7,7,7]) == 1
    assert longest_increasing_subsequence([1,3,6,7,9,4,10,5,6]) == 6
    assert longest_increasing_subsequence([]) == 0
    assert longest_increasing_subsequence([1]) == 1
    assert longest_increasing_subsequence([1,2,3,4,5]) == 5
    assert longest_increasing_subsequence([5,4,3,2,1]) == 1

if __name__ == "__main__":
    test_longest_increasing_subsequence()