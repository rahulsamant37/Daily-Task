# Python Question: Longest Increasing Subsequence Length
'''
Given an unsorted array of integers, find the length of the longest increasing subsequence (LIS).

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

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
        # It's guaranteed that tails is always sorted in increasing order.
        tails = []

        for num in nums:
            # If we find a number in tails that is greater than or equal to the current number,
            # we replace that number with the current number.  This is because the current number
            # allows us to potentially extend an existing subsequence with a smaller tail.
            # If we don't find such a number, it means that the current number is greater than
            # all numbers in tails, and we can extend the longest subsequence by 1.
            l, r = 0, len(tails)
            while l < r:
                mid = (l + r) // 2
                if tails[mid] < num:
                    l = mid + 1
                else:
                    r = mid

            if l == len(tails):
                tails.append(num)
            else:
                tails[l] = num

        return len(tails)

    return longest_increasing_subsequence

# Test cases
def test_solution():
    longest_increasing_subsequence = solution()

    # Test case 1
    nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
    expected1 = 4
    assert longest_increasing_subsequence(nums1) == expected1, f"Test Case 1 Failed: Expected {expected1}, got {longest_increasing_subsequence(nums1)}"

    # Test case 2
    nums2 = [0, 1, 0, 3, 2, 3]
    expected2 = 4
    assert longest_increasing_subsequence(nums2) == expected2, f"Test Case 2 Failed: Expected {expected2}, got {longest_increasing_subsequence(nums2)}"

    # Test case 3
    nums3 = [7, 7, 7, 7, 7, 7, 7]
    expected3 = 1
    assert longest_increasing_subsequence(nums3) == expected3, f"Test Case 3 Failed: Expected {expected3}, got {longest_increasing_subsequence(nums3)}"

    # Test case 4: Empty array
    nums4 = []
    expected4 = 0
    assert longest_increasing_subsequence(nums4) == expected4, f"Test Case 4 Failed: Expected {expected4}, got {longest_increasing_subsequence(nums4)}"

    # Test case 5: Increasing array
    nums5 = [1, 2, 3, 4, 5]
    expected5 = 5
    assert longest_increasing_subsequence(nums5) == expected5, f"Test Case 5 Failed: Expected {expected5}, got {longest_increasing_subsequence(nums5)}"

    # Test case 6: Decreasing array
    nums6 = [5, 4, 3, 2, 1]
    expected6 = 1
    assert longest_increasing_subsequence(nums6) == expected6, f"Test Case 6 Failed: Expected {expected6}, got {longest_increasing_subsequence(nums6)}"

    # Test case 7
    nums7 = [4,10,4,3,8,9]
    expected7 = 3
    assert longest_increasing_subsequence(nums7) == 3, f"Test Case 7 Failed: Expected {3}, got {longest_increasing_subsequence(nums7)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()