# Python Question: Find the Longest Increasing Subsequence Length
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
def longest_increasing_subsequence_length(nums):
    """
    Finds the length of the longest increasing subsequence (LIS) in an array.

    Args:
        nums: A list of integers.

    Returns:
        The length of the LIS.
    """
    if not nums:
        return 0

    # tails[i] is the smallest tail of all increasing subsequences with length i+1.
    # For example, if tails = [2, 3, 7, 101], it means we have increasing subsequences
    # with lengths 1, 2, 3, and 4, and the smallest tails are 2, 3, 7, and 101 respectively.
    tails = []

    # Iterate through each number in the input array.
    for num in nums:
        # If we find a number in `tails` that is greater than or equal to the current number,
        # we replace that number with the current number. This is because the current number
        # allows us to potentially build a longer increasing subsequence later on.
        # We use binary search to find the smallest number in `tails` that is greater than or equal to the current number.
        l, r = 0, len(tails) - 1
        while l <= r:
            mid = (l + r) // 2
            if tails[mid] < num:
                l = mid + 1
            else:
                r = mid - 1

        # If `l` is equal to the length of `tails`, it means the current number is greater than
        # all numbers in `tails`, so we append it to `tails`, extending the length of the longest
        # increasing subsequence found so far.
        if l == len(tails):
            tails.append(num)
        # Otherwise, we replace the number at index `l` with the current number.
        else:
            tails[l] = num

    # The length of `tails` is the length of the longest increasing subsequence.
    return len(tails)

# Test cases
def test_solution():
    assert longest_increasing_subsequence_length([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert longest_increasing_subsequence_length([0, 1, 0, 3, 2, 3]) == 4
    assert longest_increasing_subsequence_length([7, 7, 7, 7, 7, 7, 7]) == 1
    assert longest_increasing_subsequence_length([1, 3, 6, 7, 9, 4, 10, 5, 6]) == 6
    assert longest_increasing_subsequence_length([]) == 0
    assert longest_increasing_subsequence_length([1]) == 1
    assert longest_increasing_subsequence_length([2, 2]) == 1
    assert longest_increasing_subsequence_length([4,10,4,3,8,9]) == 3
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()