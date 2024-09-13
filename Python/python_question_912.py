# Python Question: Longest Increasing Subsequence (LIS)
'''
Given an unsorted array of integers, find the length of the longest increasing subsequence (LIS).
An increasing subsequence is a subsequence where the elements are in strictly increasing order.

Example:
Input: [10, 9, 2, 5, 3, 7, 101, 18]
Output: 4
Explanation: The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4.

Note:
- There may be multiple LIS combinations, it is only necessary to return the length.
- Your algorithm should run in O(n log n) time complexity.
'''

# Solution
def longest_increasing_subsequence(nums):
    """
    Finds the length of the longest increasing subsequence (LIS) in O(n log n) time.

    Args:
        nums: A list of integers.

    Returns:
        The length of the LIS.
    """

    tails = []  # tails[i] is the smallest tail of all increasing subsequences with length i+1

    for num in nums:
        # If we find a number in 'tails' that is greater than or equal to the current 'num',
        # it means we can potentially create a smaller tail for an increasing subsequence
        # of the same length. We use binary search to find the leftmost such number.
        l, r = 0, len(tails) - 1
        while l <= r:
            mid = (l + r) // 2
            if tails[mid] < num:
                l = mid + 1
            else:
                r = mid - 1

        # If we didn't find any number in 'tails' that is greater than or equal to 'num' (l == len(tails)),
        # it means 'num' is greater than all numbers in 'tails', so we can extend the longest
        # increasing subsequence by 1.
        if l == len(tails):
            tails.append(num)
        else:
            # Otherwise, we replace the smallest tail of all increasing subsequences with length l+1
            # with 'num', because 'num' is smaller and can potentially lead to a longer increasing
            # subsequence later.
            tails[l] = num

    # The length of 'tails' is the length of the LIS.
    return len(tails)


# Test cases
def test_longest_increasing_subsequence():
    assert longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert longest_increasing_subsequence([0, 1, 0, 3, 2, 3]) == 4
    assert longest_increasing_subsequence([7, 7, 7, 7, 7, 7, 7]) == 1
    assert longest_increasing_subsequence([1, 3, 6, 7, 9, 4, 10, 5, 6]) == 6
    assert longest_increasing_subsequence([]) == 0
    assert longest_increasing_subsequence([1]) == 1
    assert longest_increasing_subsequence([1, 2, 3, 4, 5]) == 5
    assert longest_increasing_subsequence([5, 4, 3, 2, 1]) == 1
    print("All test cases passed!")


if __name__ == "__main__":
    test_longest_increasing_subsequence()