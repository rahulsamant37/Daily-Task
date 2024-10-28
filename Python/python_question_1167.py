# Python Question: Longest Increasing Subsequence (LIS)
'''
Given an unsorted array of integers, find the length of the longest increasing subsequence (LIS).

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.
For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Input: [0,1,0,3,2,3]
Output: 4

Input: [7,7,7,7,7,7,7]
Output: 1
'''

# Solution
def solution():
    def longest_increasing_subsequence(nums):
        """
        Finds the length of the longest increasing subsequence (LIS) of a given array.

        Args:
            nums: A list of integers.

        Returns:
            The length of the LIS.
        """

        if not nums:
            return 0

        # tails[i] is the smallest tail of all increasing subsequences with length i+1.
        # tails is always sorted in increasing order.
        tails = []

        for num in nums:
            # If we find a number in tails that is greater than or equal to the current number,
            # it means we can replace that number with the current number to get a smaller tail
            # for an increasing subsequence of the same length. This helps us find a longer LIS later.
            # If no such number is found, it means the current number is greater than all numbers in tails,
            # so we can extend the LIS by 1.
            
            # Binary search to find the smallest tail that is greater than or equal to the current number.
            l, r = 0, len(tails) - 1
            while l <= r:
                mid = (l + r) // 2
                if tails[mid] < num:
                    l = mid + 1
                else:
                    r = mid - 1
            
            # If we found a number to replace (l < len(tails)), we replace it.
            # Otherwise, we extend the tails array.
            if l == len(tails):
                tails.append(num)
            else:
                tails[l] = num

        return len(tails)

    return longest_increasing_subsequence

# Test cases
def test_solution():
    lis = solution()
    assert lis([10,9,2,5,3,7,101,18]) == 4
    assert lis([0,1,0,3,2,3]) == 4
    assert lis([7,7,7,7,7,7,7]) == 1
    assert lis([]) == 0
    assert lis([1]) == 1
    assert lis([1,2,3,4,5]) == 5
    assert lis([5,4,3,2,1]) == 1
    assert lis([1,3,6,7,9,4,10,5,6]) == 6
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()