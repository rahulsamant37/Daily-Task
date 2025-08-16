# Python Question: Find the Longest Increasing Subsequence Length
'''
Given an unsorted array of integers, find the length of the longest increasing subsequence (LIS).
An increasing subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements, such that the elements in the subsequence are strictly increasing.

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
        tails = []

        # Iterate through each number in the input array.
        for num in nums:
            # If we find a number in 'tails' that is greater than or equal to the current number,
            # it means we can replace that number with the current number to potentially create
            # a smaller tail for an increasing subsequence of the same length.
            # We use binary search to efficiently find the first number in 'tails' that is
            # greater than or equal to the current number.

            l, r = 0, len(tails) - 1
            while l <= r:
                mid = (l + r) // 2
                if tails[mid] < num:
                    l = mid + 1
                else:
                    r = mid - 1

            # If we found a number to replace (l < len(tails)), we replace it.
            # Otherwise, it means the current number is greater than all numbers in 'tails',
            # so we extend the longest increasing subsequence by adding the current number
            # to the end of 'tails'.
            if l == len(tails):
                tails.append(num)
            else:
                tails[l] = num

        # The length of 'tails' is the length of the longest increasing subsequence.
        return len(tails)

    return longest_increasing_subsequence_length


# Test cases
def test_solution():
    lis = solution()
    assert lis([]) == 0
    assert lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert lis([1, 3, 2, 4, 5]) == 4
    assert lis([10, 22, 9, 33, 21, 50, 41, 60, 80]) == 6
    assert lis([0, 1, 0, 3, 2, 3]) == 4
    assert lis([7, 7, 7, 7, 7, 7, 7]) == 1
    assert lis([4, 10, 4, 3, 8, 9]) == 3
    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()