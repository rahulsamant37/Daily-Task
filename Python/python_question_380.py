# Python Question: Longest Increasing Subsequence Length
'''
Given an array of integers `nums`, find the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

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

        # Iterate through each number in the input array
        for num in nums:
            # If we find a number in 'tails' that is greater than or equal to the current number,
            # it means we can potentially create a new increasing subsequence with the same length
            # but a smaller tail.  We replace that number in tails with the current number.
            # This is done using binary search for efficiency.
            l, r = 0, len(tails) - 1
            while l <= r:
                mid = (l + r) // 2
                if tails[mid] < num:
                    l = mid + 1
                else:
                    r = mid - 1

            # If we didn't find any number in 'tails' greater than or equal to the current number,
            # it means we can extend the longest increasing subsequence by 1.
            # We append the current number to 'tails'.
            if l == len(tails):
                tails.append(num)
            else:
                tails[l] = num

        # The length of 'tails' is the length of the longest increasing subsequence.
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
    nums4 = [1, 3, 6, 7, 9, 4, 10, 5, 6]
    expected4 = 6
    assert lis(nums4) == 6, f"Test Case 4 Failed: Expected 6, Got {lis(nums4)}"

    # Test case 5: Empty array
    nums5 = []
    expected5 = 0
    assert lis(nums5) == 0, f"Test Case 5 Failed: Expected {expected5}, Got {lis(nums5)}"

    # Test case 6: Single element array
    nums6 = [5]
    expected6 = 1
    assert lis(nums6) == 1, f"Test Case 6 Failed: Expected {expected6}, Got {lis(nums6)}"

    # Test case 7: Decreasing sequence
    nums7 = [5, 4, 3, 2, 1]
    expected7 = 1
    assert lis(nums7) == 1, f"Test Case 7 Failed: Expected {expected7}, Got {lis(nums7)}"

    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()