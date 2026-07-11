# Python Question: Longest Increasing Subsequence (LIS)
'''
Given an unsorted array of integers, find the length of the longest increasing subsequence (LIS).

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

A strictly increasing subsequence is a subsequence where the elements are strictly increasing.

Example:
Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
'''

# Solution
def solution():
    def longest_increasing_subsequence(nums):
        """
        Calculates the length of the longest increasing subsequence (LIS) of a given list of numbers.

        Args:
            nums: A list of integers.

        Returns:
            The length of the LIS.
        """

        if not nums:
            return 0

        # tails[i] is the smallest tail of all increasing subsequences with length i+1.
        # For example, if tails = [2, 3, 7, 101], it means we have increasing subsequences
        # with lengths 1, 2, 3, and 4, and the smallest tails of these subsequences are 2, 3, 7, and 101, respectively.
        tails = []

        # Iterate through each number in the input list.
        for num in nums:
            # If we find a number in 'tails' that is greater than or equal to the current 'num',
            # we replace that number with 'num'.  This is because 'num' can potentially extend
            # an existing subsequence to a longer one, and it also gives us a smaller tail value,
            # which is beneficial for future extensions.
            # We use binary search to find the smallest number in 'tails' that is >= 'num'.
            l, r = 0, len(tails) - 1
            while l <= r:
                mid = (l + r) // 2
                if tails[mid] < num:
                    l = mid + 1
                else:
                    r = mid - 1

            # If we didn't find a number >= 'num' in 'tails' (i.e., 'num' is greater than all numbers in 'tails'),
            # it means we can extend the longest increasing subsequence by 1. We append 'num' to 'tails'.
            # Otherwise, we replace the number at index 'l' with 'num'.
            if l == len(tails):
                tails.append(num)
            else:
                tails[l] = num

        # The length of 'tails' is the length of the longest increasing subsequence.
        return len(tails)

    return longest_increasing_subsequence

# Test cases
def test_solution():
    lis = solution()
    assert lis([]) == 0
    assert lis([10,9,2,5,3,7,101,18]) == 4
    assert lis([0,1,0,3,2,3]) == 4
    assert lis([1,3,6,7,9,4,10,5,6]) == 6
    assert lis([4,10,4,3,8,9]) == 3
    assert lis([2,2]) == 1
    assert lis([1,3,5,2,4,6]) == 4
    assert lis([1]) == 1
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()