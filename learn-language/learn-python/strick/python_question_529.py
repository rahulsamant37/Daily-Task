# Python Question: Largest Sum Contiguous Subarray
'''
Given an array of integers, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: [4, -1, 2, 1] has the largest sum = 6.
'''

# Solution
def solution():
    def maxSubArray(nums):
        """
        Finds the contiguous subarray with the largest sum.

        Args:
            nums: A list of integers.

        Returns:
            The largest sum of a contiguous subarray.
        """

        # Initialize max_so_far to the first element of the array. This handles the case where all numbers are negative.
        max_so_far = nums[0]
        # Initialize current_max to the first element as well.
        current_max = nums[0]

        # Iterate through the array starting from the second element.
        for i in range(1, len(nums)):
            # current_max is either the current element or the sum of the current element and the previous current_max.
            # We choose the larger of the two.  If the previous current_max was negative, it's better to start a new subarray at the current element.
            current_max = max(nums[i], current_max + nums[i])

            # Update max_so_far if the current_max is greater.
            max_so_far = max(max_so_far, current_max)

        return max_so_far

    return maxSubArray

# Test cases
def test_solution():
    maxSubArray = solution()
    # Test case 1: Basic test case
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    expected1 = 6
    assert maxSubArray(nums1) == expected1, f"Test Case 1 Failed: Expected {expected1}, Got {maxSubArray(nums1)}"

    # Test case 2: All negative numbers
    nums2 = [-1, -2, -3, -4, -5]
    expected2 = -1
    assert maxSubArray(nums2) == expected2, f"Test Case 2 Failed: Expected {expected2}, Got {maxSubArray(nums2)}"

    # Test case 3: All positive numbers
    nums3 = [1, 2, 3, 4, 5]
    expected3 = 15
    assert maxSubArray(nums3) == expected3, f"Test Case 3 Failed: Expected {expected3}, Got {maxSubArray(nums3)}"

    # Test case 4: Single element array
    nums4 = [5]
    expected4 = 5
    assert maxSubArray(nums4) == expected4, f"Test Case 4 Failed: Expected {expected4}, Got {maxSubArray(nums4)}"

    # Test case 5: Array with a single large positive number surrounded by negative numbers
    nums5 = [-100, -1, -50, 1000, -200, -300]
    expected5 = 1000
    assert maxSubArray(nums5) == expected5, f"Test Case 5 Failed: Expected {expected5}, Got {maxSubArray(nums5)}"
    
    # Test case 6: Array starting with large positive number
    nums6 = [5, -4, 3]
    expected6 = 5
    assert maxSubArray(nums6) == 5, f"Test case 6 failed"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()