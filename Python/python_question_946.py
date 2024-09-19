# Python Question: Longest Increasing Subsequence (LIS)
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
        Calculates the length of the longest increasing subsequence (LIS) in the given array.

        Args:
            nums: A list of integers.

        Returns:
            The length of the LIS.
        """

        # tails[i] is the smallest tail of all increasing subsequences with length i+1.
        # We maintain tails as a sorted array.
        tails = []

        # Iterate through each number in the input array
        for num in nums:
            # If we find a number in tails that is greater than or equal to the current number,
            # we replace that number with the current number. This is because the current number
            # allows us to potentially build a longer increasing subsequence later.
            # If no such number is found, it means the current number is greater than all the numbers
            # in tails, so we append it to tails, extending the LIS by 1.
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

        # The length of tails is the length of the LIS.
        return len(tails)
    
    return longest_increasing_subsequence

# Test cases
def test_solution():
    lis = solution()

    # Test case 1
    nums1 = [10,9,2,5,3,7,101,18]
    expected1 = 4
    assert lis(nums1) == expected1, f"Test Case 1 Failed: Expected {expected1}, got {lis(nums1)}"

    # Test case 2
    nums2 = [0,1,0,3,2,3]
    expected2 = 4
    assert lis(nums2) == expected2, f"Test Case 2 Failed: Expected {expected2}, got {lis(nums2)}"

    # Test case 3
    nums3 = [7,7,7,7,7,7,7]
    expected3 = 1
    assert lis(nums3) == expected3, f"Test Case 3 Failed: Expected {expected3}, got {lis(nums3)}"

    # Test case 4
    nums4 = [1,3,6,7,9,4,10,5,6]
    expected4 = 6
    assert lis(nums4) == 6, f"Test Case 4 Failed: Expected {6}, got {lis(nums4)}"

    # Test case 5
    nums5 = []
    expected5 = 0
    assert lis(nums5) == expected5, f"Test Case 5 Failed: Expected {expected5}, got {lis(nums5)}"

    # Test case 6
    nums6 = [1]
    expected6 = 1
    assert lis(nums6) == expected6, f"Test Case 6 Failed: Expected {expected6}, got {lis(nums6)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()