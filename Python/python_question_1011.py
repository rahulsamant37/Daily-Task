# Python Question: Find the Longest Increasing Subsequence Length
'''
Given an unsorted array of integers, find the length of the longest increasing subsequence (LIS).

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.
An increasing subsequence is a subsequence where the elements are strictly increasing.

Example:
Input: [10, 9, 2, 5, 3, 7, 101, 18]
Output: 4
Explanation: The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4.
'''

# Solution
def solution():
    def longest_increasing_subsequence_length(nums):
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
        # It is maintained in sorted order.
        tails = []

        # Iterate through each number in the input array
        for num in nums:
            # If we find a number in 'tails' that is greater than or equal to the current 'num',
            # it means we can potentially replace the existing number with 'num' to create a
            # smaller tail for an increasing subsequence of the same length. This helps in
            # building the LIS more efficiently.
            # We use binary search to find the smallest number in 'tails' that is >= 'num'.
            l, r = 0, len(tails) - 1
            while l <= r:
                mid = (l + r) // 2
                if tails[mid] < num:
                    l = mid + 1
                else:
                    r = mid - 1

            # If 'num' is greater than all numbers in 'tails', it means we can extend the LIS
            # by appending 'num' to the end.
            if l == len(tails):
                tails.append(num)
            else:
                # Otherwise, we replace the existing number at index 'l' with 'num'.
                # This maintains the property that 'tails' is always sorted and contains the
                # smallest tails for increasing subsequences of different lengths.
                tails[l] = num

        # The length of 'tails' is the length of the LIS.
        return len(tails)

    return longest_increasing_subsequence_length

# Test cases
def test_solution():
    lis = solution()
    assert lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert lis([0, 1, 0, 3, 2, 3]) == 4
    assert lis([7, 7, 7, 7, 7, 7, 7]) == 1
    assert lis([]) == 0
    assert lis([1]) == 1
    assert lis([1, 2, 3, 4, 5]) == 5
    assert lis([5, 4, 3, 2, 1]) == 1
    assert lis([4,10,4,3,8,9]) == 3
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()