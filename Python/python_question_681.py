# Python Question: Longest Increasing Subsequence Length
'''
Given an unsorted array of integers, find the length of the longest increasing subsequence (LIS).

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.  For example, [3,6,2,7] is a subsequence of [0,3,1,6,2,2,7].

Example:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Input: nums = [0,1,0,3,2,3]
Output: 4

Input: nums = [7,7,7,7,7,7,7]
Output: 1
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
        tails = []

        # Iterate through the input array
        for num in nums:
            # If we find a number in 'tails' that is greater than or equal to the current number,
            # it means we can potentially create a shorter increasing subsequence with the same length
            # by replacing that number with the current number.  We use binary search to find the smallest
            # such number.
            l, r = 0, len(tails) - 1
            while l <= r:
                mid = (l + r) // 2
                if tails[mid] < num:
                    l = mid + 1
                else:
                    r = mid - 1

            # If we didn't find any number in 'tails' that is greater than or equal to the current number,
            # it means the current number extends the longest increasing subsequence by 1.
            if l == len(tails):
                tails.append(num)
            # Otherwise, we replace the smallest number in 'tails' that is greater than or equal to the current number with the current number.
            else:
                tails[l] = num

        # The length of 'tails' is the length of the LIS.
        return len(tails)
    return longest_increasing_subsequence

# Test cases
def test_solution():
    lis = solution()
    assert lis([10,9,2,5,3,7,101,18]) == 4
    assert lis([0,1,0,3,2,3]) == 4
    assert lis([7,7,7,7,7,7,7]) == 1
    assert lis([1,3,6,7,9,4,10,5,6]) == 6
    assert lis([]) == 0
    assert lis([1]) == 1
    assert lis([1,2]) == 2
    assert lis([2,1]) == 1
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()