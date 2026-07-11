# Python Question: Longest Increasing Subsequence (LIS)
'''
Given an unsorted array of integers, find the length of the longest increasing subsequence (LIS).

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.  For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

An increasing subsequence is a subsequence where the elements are strictly increasing.

Example:
Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
'''

# Solution
def solution():
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
        # It's always a sorted array in increasing order.
        tails = []

        # Iterate through each number in the input array
        for num in nums:
            # If we find a number in `tails` that is greater than or equal to the current number,
            # it means we can potentially replace that number with the current number to
            # form a shorter increasing subsequence with the same length but a smaller tail.
            # This helps us maintain the property that `tails` always contains the smallest tails
            # for all increasing subsequences of a given length.
            l, r = 0, len(tails)
            while l < r:
                mid = (l + r) // 2
                if tails[mid] < num:
                    l = mid + 1
                else:
                    r = mid
            
            # If we didn't find any number in `tails` that is greater than or equal to the current number,
            # it means the current number is greater than all numbers in `tails`, so we can extend
            # the longest increasing subsequence by 1.
            if l == len(tails):
                tails.append(num)
            # Otherwise, we replace the number at index `l` with the current number.
            else:
                tails[l] = num

        # The length of `tails` is the length of the longest increasing subsequence.
        return len(tails)
    
    return longest_increasing_subsequence

# Test cases
def test_solution():
    lis = solution()
    assert lis([]) == 0
    assert lis([10,9,2,5,3,7,101,18]) == 4
    assert lis([1,3,6,7,9,4,10,5,6]) == 6
    assert lis([5,4,3,2,1]) == 1
    assert lis([1,2,3,4,5]) == 5
    assert lis([1,3,5,2,4,6]) == 4
    assert lis([4,10,4,3,8,9]) == 3
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()