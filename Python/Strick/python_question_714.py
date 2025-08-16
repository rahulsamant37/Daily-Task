# Python Question: Longest Increasing Subsequence Length
'''
Given an unsorted array of integers, find the length of the longest increasing subsequence (LIS).

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

A strictly increasing subsequence is a subsequence where each element is strictly greater than the previous element.

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
        Finds the length of the longest increasing subsequence (LIS) in an array.

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
            # it means we can potentially replace it with a smaller tail, leading to a potentially
            # longer increasing subsequence later on.  We use binary search for efficiency.
            l, r = 0, len(tails) - 1
            while l <= r:
                mid = (l + r) // 2
                if tails[mid] < num:
                    l = mid + 1
                else:
                    r = mid - 1

            # If we didn't find any number in 'tails' that is greater than or equal to the current number,
            # it means the current number can extend the longest increasing subsequence by 1.
            if l == len(tails):
                tails.append(num)
            # Otherwise, we replace the smallest number in 'tails' that is greater than or equal to the
            # current number with the current number. This doesn't change the length of the longest
            # increasing subsequence, but it allows us to potentially build a longer increasing subsequence
            # later on.
            else:
                tails[l] = num

        # The length of 'tails' is the length of the longest increasing subsequence.
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
    nums4 = []
    expected4 = 0
    assert longest_increasing_subsequence(nums4) == expected4, f"Test Case 4 Failed: Expected {expected4}, Got {longest_increasing_subsequence(nums4)}"

    # Test case 5
    nums5 = [1]
    expected5 = 1
    assert longest_increasing_subsequence(nums5) == expected5, f"Test Case 5 Failed: Expected {expected5}, Got {longest_increasing_subsequence(nums5)}"

    # Test case 6
    nums6 = [1, 3, 6, 7, 9, 4, 10, 5, 6]
    expected6 = 6
    assert longest_increasing_subsequence(nums6) == 6, f"Test Case 6 Failed: Expected {6}, Got {longest_increasing_subsequence(nums6)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()