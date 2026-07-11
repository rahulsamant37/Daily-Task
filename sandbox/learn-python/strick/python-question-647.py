# Python Question: Find the Longest Increasing Subsequence Length
'''
Given an array of integers, find the length of the longest increasing subsequence (LIS).

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.  An increasing subsequence is a subsequence where the elements are in strictly increasing order.

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
        Finds the length of the longest increasing subsequence in a given array.

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
            # it means we can potentially extend an existing subsequence with the current number
            # to create a smaller tail for a subsequence of the same length. We use binary search
            # to find the smallest number in tails that is greater than or equal to the current number.
            l, r = 0, len(tails) - 1
            while l <= r:
                mid = (l + r) // 2
                if tails[mid] < num:
                    l = mid + 1
                else:
                    r = mid - 1

            # If we find a number in tails that is greater than or equal to the current number,
            # we replace it with the current number. Otherwise, it means the current number is
            # greater than all numbers in tails, so we extend the tails array by adding the
            # current number to the end.
            if l == len(tails):
                tails.append(num)
            else:
                tails[l] = num

        # The length of the tails array is the length of the longest increasing subsequence.
        return len(tails)

    return longest_increasing_subsequence
# Test cases
def test_solution():
    longest_increasing_subsequence = solution()

    # Test case 1
    nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
    expected1 = 4
    assert longest_increasing_subsequence(nums1) == expected1, f"Test Case 1 Failed: Expected {expected1}, Got {longest_increasing_subsequence(nums1)}"

    # Test case 2
    nums2 = [0, 1, 0, 3, 2, 3]
    expected2 = 4
    assert longest_increasing_subsequence(nums2) == expected2, f"Test Case 2 Failed: Expected {expected2}, Got {longest_increasing_subsequence(nums2)}"

    # Test case 3
    nums3 = [7, 7, 7, 7, 7, 7, 7]
    expected3 = 1
    assert longest_increasing_subsequence(nums3) == expected3, f"Test Case 3 Failed: Expected {expected3}, Got {longest_increasing_subsequence(nums3)}"

    # Test case 4
    nums4 = [1, 3, 6, 7, 9, 4, 10, 5, 6]
    expected4 = 6
    assert longest_increasing_subsequence(nums4) == expected4, f"Test Case 4 Failed: Expected {expected4}, Got {longest_increasing_subsequence(nums4)}"

    # Test case 5: Empty list
    nums5 = []
    expected5 = 0
    assert longest_increasing_subsequence(nums5) == expected5, f"Test Case 5 Failed: Expected {expected5}, Got {longest_increasing_subsequence(nums5)}"

    # Test case 6: Single element list
    nums6 = [5]
    expected6 = 1
    assert longest_increasing_subsequence(nums6) == expected6, f"Test Case 6 Failed: Expected {expected6}, Got {longest_increasing_subsequence(nums6)}"

    # Test case 7: Decreasing list
    nums7 = [5, 4, 3, 2, 1]
    expected7 = 1
    assert longest_increasing_subsequence(nums7) == expected7, f"Test Case 7 Failed: Expected {expected7}, Got {longest_increasing_subsequence(nums7)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()