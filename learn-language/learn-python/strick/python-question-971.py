# Python Question: Longest Increasing Subsequence Length
'''
Given an unsorted array of integers, find the length of the longest increasing subsequence (LIS).

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

An increasing subsequence is a subsequence where the elements are in strictly increasing order.

Example:
Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Note:
There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n log n) complexity.
'''

# Solution
def solution():
    def longest_increasing_subsequence_length(nums):
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
        # For example, if tails = [2, 3, 7], then
        # there is an increasing subsequence of length 1 whose smallest tail is 2,
        # there is an increasing subsequence of length 2 whose smallest tail is 3,
        # there is an increasing subsequence of length 3 whose smallest tail is 7.
        tails = []

        # Iterate through each number in the input array
        for num in nums:
            # If we find a number in 'tails' that is greater than or equal to the current number,
            # we replace that number with the current number. This is because the current number
            # can potentially create a longer increasing subsequence.
            # If no such number is found, it means the current number is greater than all numbers in 'tails',
            # and we append it to 'tails', extending the length of the LIS by 1.

            # Binary search to find the smallest tail that is greater than or equal to the current number
            l, r = 0, len(tails) - 1
            while l <= r:
                mid = (l + r) // 2
                if tails[mid] < num:
                    l = mid + 1
                else:
                    r = mid - 1

            # If we found a number to replace, replace it. Otherwise, append the current number to 'tails'.
            if l == len(tails):
                tails.append(num)
            else:
                tails[l] = num

        # The length of 'tails' is the length of the LIS
        return len(tails)

    return longest_increasing_subsequence_length

# Test cases
def test_solution():
    longest_increasing_subsequence_length = solution()

    # Test case 1
    nums1 = [10,9,2,5,3,7,101,18]
    expected1 = 4
    assert longest_increasing_subsequence_length(nums1) == expected1, f"Test Case 1 Failed: Expected {expected1}, Got {longest_increasing_subsequence_length(nums1)}"

    # Test case 2
    nums2 = [0,1,0,3,2,3]
    expected2 = 4
    assert longest_increasing_subsequence_length(nums2) == expected2, f"Test Case 2 Failed: Expected {expected2}, Got {longest_increasing_subsequence_length(nums2)}"

    # Test case 3
    nums3 = [7,7,7,7,7,7,7]
    expected3 = 1
    assert longest_increasing_subsequence_length(nums3) == expected3, f"Test Case 3 Failed: Expected {expected3}, Got {longest_increasing_subsequence_length(nums3)}"

    # Test case 4
    nums4 = [1,3,6,7,9,4,10,5,6]
    expected4 = 6
    assert longest_increasing_subsequence_length(nums4) == 6, f"Test Case 4 Failed: Expected 6, Got {longest_increasing_subsequence_length(nums4)}"

    # Test case 5: Empty array
    nums5 = []
    expected5 = 0
    assert longest_increasing_subsequence_length(nums5) == expected5, f"Test Case 5 Failed: Expected {expected5}, Got {longest_increasing_subsequence_length(nums5)}"

    # Test case 6: Single element array
    nums6 = [5]
    expected6 = 1
    assert longest_increasing_subsequence_length(nums6) == expected6, f"Test Case 6 Failed: Expected {expected6}, Got {longest_increasing_subsequence_length(nums6)}"

    # Test case 7: Already sorted array
    nums7 = [1, 2, 3, 4, 5]
    expected7 = 5
    assert longest_increasing_subsequence_length(nums7) == expected7, f"Test Case 7 Failed: Expected {expected7}, Got {longest_increasing_subsequence_length(nums7)}"

    # Test case 8: Reverse sorted array
    nums8 = [5, 4, 3, 2, 1]
    expected8 = 1
    assert longest_increasing_subsequence_length(nums8) == expected8, f"Test Case 8 Failed: Expected {expected8}, Got {longest_increasing_subsequence_length(nums8)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()