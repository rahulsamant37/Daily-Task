# Python Question: Find the Longest Increasing Subsequence Length
'''
Given an unsorted array of integers, find the length of the longest increasing subsequence (LIS).

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.
An increasing subsequence is a subsequence where the elements are in strictly increasing order.

Example:
Input: [10, 9, 2, 5, 3, 7, 101, 18]
Output: 4
Explanation: The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4.
'''

# Solution
def solution():
    def longest_increasing_subsequence_length(nums):
        """
        Calculates the length of the longest increasing subsequence in a given array of integers.

        Args:
            nums: A list of integers.

        Returns:
            The length of the longest increasing subsequence.
        """

        if not nums:
            return 0

        # tails[i] is the smallest tail of all increasing subsequences with length i+1.
        tails = []

        # Iterate through each number in the input array.
        for num in nums:
            # If we find a number in `tails` that is greater than or equal to the current number,
            # we replace it with the current number. This is because the current number allows
            # us to form an increasing subsequence of the same length but with a smaller tail.
            # This makes it more likely to extend the subsequence later.
            # If no such number is found, it means the current number is larger than all numbers in `tails`,
            # so we can extend the longest increasing subsequence by 1.
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

        # The length of `tails` is the length of the longest increasing subsequence.
        return len(tails)

    return longest_increasing_subsequence_length

# Test cases
def test_solution():
    longest_increasing_subsequence_length = solution()

    # Test case 1
    nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
    expected1 = 4
    assert longest_increasing_subsequence_length(nums1) == expected1, f"Test Case 1 Failed: Expected {expected1}, got {longest_increasing_subsequence_length(nums1)}"

    # Test case 2
    nums2 = [0, 1, 0, 3, 2, 3]
    expected2 = 4
    assert longest_increasing_subsequence_length(nums2) == expected2, f"Test Case 2 Failed: Expected {expected2}, got {longest_increasing_subsequence_length(nums2)}"

    # Test case 3
    nums3 = [7, 7, 7, 7, 7, 7, 7]
    expected3 = 1
    assert longest_increasing_subsequence_length(nums3) == expected3, f"Test Case 3 Failed: Expected {expected3}, got {longest_increasing_subsequence_length(nums3)}"

    # Test case 4
    nums4 = []
    expected4 = 0
    assert longest_increasing_subsequence_length(nums4) == expected4, f"Test Case 4 Failed: Expected {expected4}, got {longest_increasing_subsequence_length(nums4)}"

    # Test case 5
    nums5 = [1]
    expected5 = 1
    assert longest_increasing_subsequence_length(nums5) == expected5, f"Test Case 5 Failed: Expected {expected5}, got {longest_increasing_subsequence_length(nums5)}"

    # Test case 6: Decreasing order
    nums6 = [5, 4, 3, 2, 1]
    expected6 = 1
    assert longest_increasing_subsequence_length(nums6) == expected6, f"Test Case 6 Failed: Expected {expected6}, got {longest_increasing_subsequence_length(nums6)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()