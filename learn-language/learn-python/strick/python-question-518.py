# Python Question: Find the Longest Increasing Subsequence (LIS)
'''
Given an unsorted array of integers, find the length of the longest increasing subsequence (LIS).

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

An increasing subsequence is a subsequence where the elements are in strictly increasing order.

Example:
Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Input: [0,1,0,3,2,3]
Output: 4
Explanation: The longest increasing subsequence is [0,1,2,3], therefore the length is 4.

Input: [7,7,7,7,7,7,7]
Output: 1
Explanation: The longest increasing subsequence is [7], therefore the length is 1.
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

        for num in nums:
            # If we find a number in tails that is greater than or equal to the current number,
            # we replace it with the current number. This is because the current number
            # allows us to form an increasing subsequence of the same length with a smaller tail.
            # If we don't find such a number, it means the current number is greater than all
            # tails, so we can extend the longest increasing subsequence by 1.

            # Binary search to find the smallest tail that is greater than or equal to num
            l, r = 0, len(tails)
            while l < r:
                mid = (l + r) // 2
                if tails[mid] < num:
                    l = mid + 1
                else:
                    r = mid

            if l == len(tails):
                # Extend the longest increasing subsequence
                tails.append(num)
            else:
                # Replace the tail
                tails[l] = num

        # The length of the tails array is the length of the LIS.
        return len(tails)

    return longest_increasing_subsequence

# Test cases
def test_solution():
    lis = solution()

    # Test case 1
    nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
    expected1 = 4
    assert lis(nums1) == expected1, f"Test Case 1 Failed: Expected {expected1}, Got {lis(nums1)}"

    # Test case 2
    nums2 = [0, 1, 0, 3, 2, 3]
    expected2 = 4
    assert lis(nums2) == expected2, f"Test Case 2 Failed: Expected {expected2}, Got {lis(nums2)}"

    # Test case 3
    nums3 = [7, 7, 7, 7, 7, 7, 7]
    expected3 = 1
    assert lis(nums3) == expected3, f"Test Case 3 Failed: Expected {expected3}, Got {lis(nums3)}"

    # Test case 4
    nums4 = []
    expected4 = 0
    assert lis(nums4) == expected4, f"Test Case 4 Failed: Expected {expected4}, Got {lis(nums4)}"

    # Test case 5
    nums5 = [1, 3, 6, 7, 9, 4, 10, 5, 6]
    expected5 = 6
    assert lis(nums5) == 6, f"Test Case 5 Failed: Expected {6}, Got {lis(nums5)}"

    # Test case 6
    nums6 = [4,10,4,3,8,9]
    expected6 = 3
    assert lis(nums6) == 3, f"Test Case 6 Failed: Expected {3}, Got {lis(nums6)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()