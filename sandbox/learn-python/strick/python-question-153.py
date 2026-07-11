# Python Question: Longest Increasing Subsequence (LIS)
'''
Given an unsorted array of integers, find the length of the longest increasing subsequence (LIS).
An increasing subsequence is a sequence of numbers within the array that are strictly increasing.
The numbers don't have to be consecutive.

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
        Finds the length of the longest increasing subsequence (LIS) in the given array.

        Args:
            nums: An unsorted array of integers.

        Returns:
            The length of the LIS.
        """

        if not nums:
            return 0

        # tails[i] is the smallest tail of all increasing subsequences with length i+1.
        tails = []

        # Iterate through each number in the input array.
        for num in nums:
            # If we find a number in tails that is greater than or equal to the current number,
            # it means we can replace that number with the current number to form an increasing
            # subsequence of the same length but with a smaller tail. This allows us to potentially
            # extend the LIS later. We use binary search to find the smallest number >= num.
            l, r = 0, len(tails) - 1
            while l <= r:
                mid = (l + r) // 2
                if tails[mid] < num:
                    l = mid + 1
                else:
                    r = mid - 1

            # If we didn't find a number >= num, it means the current number is greater than all
            # numbers in tails, so we can extend the LIS by one.
            if l == len(tails):
                tails.append(num)
            # Otherwise, we replace the smallest number >= num with the current number.
            else:
                tails[l] = num

        # The length of tails is the length of the LIS.
        return len(tails)
    return longest_increasing_subsequence

# Test cases
def test_solution():
    longest_increasing_subsequence = solution()
    assert longest_increasing_subsequence([10,9,2,5,3,7,101,18]) == 4
    assert longest_increasing_subsequence([0,1,0,3,2,3]) == 4
    assert longest_increasing_subsequence([7,7,7,7,7,7,7]) == 1
    assert longest_increasing_subsequence([1,3,6,7,9,4,10,5,6]) == 6
    assert longest_increasing_subsequence([]) == 0
    assert longest_increasing_subsequence([1]) == 1
    assert longest_increasing_subsequence([1,2,3,4,5]) == 5
    assert longest_increasing_subsequence([5,4,3,2,1]) == 1
    assert longest_increasing_subsequence([4,10,4,3,8,9]) == 3
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()