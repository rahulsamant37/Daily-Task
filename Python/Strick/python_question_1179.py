# Python Question: Find the Longest Increasing Subsequence Length
'''
Given an unsorted array of integers, find the length of the longest increasing subsequence (LIS).

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

An increasing subsequence is a subsequence where the elements are strictly increasing.

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
    def longest_increasing_subsequence_length(nums):
        """
        Calculates the length of the longest increasing subsequence (LIS) in a given array of integers.

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
            # it means we can potentially form a shorter increasing subsequence that ends with the current number.
            # We use binary search to find the smallest such number and replace it with the current number.
            # This maintains the increasing property of the 'tails' array.
            l, r = 0, len(tails) - 1
            while l <= r:
                mid = (l + r) // 2
                if tails[mid] < num:
                    l = mid + 1
                else:
                    r = mid - 1

            # If we didn't find any number in 'tails' that is greater than or equal to the current number,
            # it means the current number can extend the longest increasing subsequence by 1.
            # We append the current number to the 'tails' array.
            if l == len(tails):
                tails.append(num)
            else:
                tails[l] = num

        # The length of the 'tails' array is the length of the LIS.
        return len(tails)
    return longest_increasing_subsequence_length

# Test cases
def test_solution():
    longest_increasing_subsequence_length = solution()
    assert longest_increasing_subsequence_length([10,9,2,5,3,7,101,18]) == 4
    assert longest_increasing_subsequence_length([0,1,0,3,2,3]) == 4
    assert longest_increasing_subsequence_length([7,7,7,7,7,7,7]) == 1
    assert longest_increasing_subsequence_length([1,3,6,7,9,4,10,5,6]) == 6
    assert longest_increasing_subsequence_length([]) == 0
    assert longest_increasing_subsequence_length([1]) == 1
    assert longest_increasing_subsequence_length([1,2,3,4,5]) == 5
    assert longest_increasing_subsequence_length([5,4,3,2,1]) == 1
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()