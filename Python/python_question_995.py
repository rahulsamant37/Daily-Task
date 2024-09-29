# Python Question: Longest Increasing Subsequence with Binary Search
'''
Given an unsorted array of integers, find the length of the longest increasing subsequence (LIS).

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.  For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Input: [10, 9, 2, 5, 3, 7, 101, 18]
Output: 4
Explanation: The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4.
'''

# Solution
def longest_increasing_subsequence(nums):
    """
    Finds the length of the longest increasing subsequence (LIS) of a given array.

    Args:
        nums: A list of integers.

    Returns:
        The length of the LIS.
    """

    tails = []  # Stores the smallest tail of all increasing subsequences with length i+1 in tails[i].
                 # This array will be sorted in increasing order.

    for num in nums:
        # If we find a number in tails that is greater than or equal to the current number,
        # we replace that number with the current number. This is because the current number
        # gives us a chance to create a smaller tail and potentially extend LIS later.
        # If no such number exists, it means the current number is greater than all tails,
        # and we can extend the LIS by 1.
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

    return len(tails)

# Test cases
def test_longest_increasing_subsequence():
    assert longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert longest_increasing_subsequence([0, 1, 0, 3, 2, 3]) == 4
    assert longest_increasing_subsequence([7, 7, 7, 7, 7, 7, 7]) == 1
    assert longest_increasing_subsequence([1, 3, 6, 7, 9, 4, 10, 5, 6]) == 6
    assert longest_increasing_subsequence([4, 10, 4, 3, 8, 9]) == 3
    assert longest_increasing_subsequence([]) == 0
    assert longest_increasing_subsequence([1]) == 1
    assert longest_increasing_subsequence([1,2,3,4,5]) == 5
    assert longest_increasing_subsequence([5,4,3,2,1]) == 1
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_increasing_subsequence()