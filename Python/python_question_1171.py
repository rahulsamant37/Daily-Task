# Python Question: Find the Longest Increasing Subsequence (LIS)
'''
Given an unsorted array of integers, find the length of the longest increasing subsequence (LIS).

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.
An increasing subsequence is a subsequence where the elements are in strictly increasing order.

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
    def lengthOfLIS(nums):
        """
        Finds the length of the longest increasing subsequence.

        Args:
            nums: A list of integers.

        Returns:
            The length of the longest increasing subsequence.
        """
        if not nums:
            return 0

        # tails[i] is the smallest tail of all increasing subsequences with length i+1.
        tails = []

        # Iterate through the input array.
        for num in nums:
            # If we find a number in tails that is greater than or equal to the current number,
            # we replace that number with the current number. This is because the current number
            # can form an increasing subsequence with the same length but with a smaller tail,
            # which is more likely to be extended later.  We use binary search to find this number.
            l, r = 0, len(tails) - 1
            while l <= r:
                mid = (l + r) // 2
                if tails[mid] < num:
                    l = mid + 1
                else:
                    r = mid - 1

            # If we didn't find any number in tails that is greater than or equal to the current number,
            # it means the current number can extend the longest increasing subsequence by 1.
            if l == len(tails):
                tails.append(num)
            else:
                tails[l] = num

        # The length of tails is the length of the longest increasing subsequence.
        return len(tails)

    return lengthOfLIS

# Test cases
def test_solution():
    lengthOfLIS = solution()
    assert lengthOfLIS([10,9,2,5,3,7,101,18]) == 4
    assert lengthOfLIS([0,1,0,3,2,3]) == 4
    assert lengthOfLIS([7,7,7,7,7,7,7]) == 1
    assert lengthOfLIS([1,3,6,7,9,4,10,5,6]) == 6
    assert lengthOfLIS([10, 22, 9, 33, 21, 50, 41, 60, 80]) == 6
    assert lengthOfLIS([]) == 0
    assert lengthOfLIS([1]) == 1
    assert lengthOfLIS([2,2]) == 1
    assert lengthOfLIS([1,2]) == 2
    assert lengthOfLIS([2,1]) == 1
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()